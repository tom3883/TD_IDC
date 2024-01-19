from fastapi import FastAPI
from rdflib import Graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

g = Graph()
g.parse("../../recipe_schema.ttl")
g.parse("../../recipe_product_categories.ttl")
g.parse("../../recipe_categories.ttl")
g.parse("../../csvw/walmart_products_complete.ttl")

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

@app.get("/")
async def root():
    return {"result" : len(g)}


@app.get("/getProducts")
async def root():
    g.parse('../../csvw/walmart_products_reduced.ttl')

    q = """
        PREFIX : <http://recipes-project.com/schema/>
        select ?n where {
            ?p :productName ?n
        }
    """

    results = []
    for r in g.query(q):
        results.append(r["n"])

    return {"results": g.query(q)}


@app.get("/v2/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):

    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>

        SELECT  ?recipeName ?dishType ?food
        WHERE {{
            ?c a :RecipeCategory ;
            skos:prefLabel ?dishType .
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?recipe :name ?recipeName ;
                :recipeCategory ?dishType ;
                :recipeIngredient ?food .
            }}
        }}
        """
    )

    recipes_dict = {}
    for row in qres:
        recipe_name = row.recipeName
        dish_type = row.dishType
        food = row.food

        if recipe_name not in recipes_dict:
            recipes_dict[recipe_name] = {"name": recipe_name, "dishType": dish_type, "ingredients": []}

        recipes_dict[recipe_name]["ingredients"].append(food)

    recipes = list(recipes_dict.values())

    return {"results": recipes}


@app.get("/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):

    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>

        SELECT ?recipeName ?dishType ?food
        WHERE {{
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?recipe :name ?recipeName ;
                :recipeCategory ?dishType ;
                :recipeIngredient ?food .
            }}
        }}
        """
    )

    recipes_dict = {}
    for row in qres:
        recipe_name = row.recipeName
        dish_type = row.dishType
        food = row.food

        if recipe_name not in recipes_dict:
            recipes_dict[recipe_name] = {"name": recipe_name, "dishType": dish_type, "ingredients": []}

        recipes_dict[recipe_name]["ingredients"].append(food)

    recipes = list(recipes_dict.values())

    return recipes


@app.get("/v3/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):

    qres_recipes = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        CONSTRUCT {{
            ?recipe a :Recipe ;
            :name ?recipeName ;
            :recipeIngredient ?ingredient ;
            :recipeCategory ?category .
            
            ?category a :RecipeCategory ;
            skos:prefLabel ?dishType .

        }}
        WHERE {{
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?recipe :name ?recipeName ;
                :recipeCategory ?dishType ;
                :recipeIngredient ?ingredient .
            }}
        }}
        """
    )

    results = []
    for row in qres_recipes:
        print(row)
        """ recipe_data = {
            "recipeName" : row[2]
        }
        results.append(recipe_data) """

    return {"done" : results}