from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from SPARQLWrapper import JSON, POST, POSTDIRECTLY, SPARQLWrapper
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wds_Corese = 'http://localhost:8080/sparql'

def sparql_service_update(service, query):
    """
    Helper function to update (DELETE DATA, INSERT DATA, DELETE/INSERT) data.

    """
    sparql = SPARQLWrapper(service)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    result = sparql.query()

    processed_results = json.load(result.response)
    cols = processed_results['head']['vars']

    out = []
    for row in processed_results['results']['bindings']:
        item = []
        for c in cols:
            item.append(row.get(c, {}).get('value'))
        out.append(item)

    return out

@app.get("/")
async def root():
    return "Fast API running"

@app.get("/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):
    query = f"""
        PREFIX : <http://recipes-project.com/schema#>

        SELECT  DISTINCT ?recipeName ?dishType ?ingredient ?productName ?price ?brandName
        WHERE {{
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?r :name ?recipeName ;
                :recipeCategory ?dishType ;
                :recipeIngredient ?ingredient .
            }}
            OPTIONAL {{
                ?product :productName ?productName ;
                :price ?price ;
                :brandName ?brandName .
                FILTER (STR(?productName) = STR(?ingredient)) 
            }}
        }}
    """
    results = sparql_service_update(wds_Corese, query)

    recipes = []
    # process response
    for row in results:
        recipe_name = row[0]
        category = row[1]
        ingredient = row[2]
        product_name = row[3]
        price = row[4]
        brandName = row[5]

        existing_recipe = next((recipe for recipe in recipes if recipe['recipeName'] == recipe_name and recipe['category'] == category), None)

        if existing_recipe is None:
            new_recipe = {'recipeName': recipe_name, 'category': category, 'ingredients': [], 'products': []}
            recipes.append(new_recipe)
        else:
            new_recipe = existing_recipe

        # Append the ingredient to the 'ingredients' list
        new_recipe['ingredients'].append(ingredient)

        # Append the product and its price to the 'products' list
        if product_name is not None and price is not None:
            new_recipe['products'].append({'productName': product_name, 'price': price, 'brand' : brandName})


    return recipes
