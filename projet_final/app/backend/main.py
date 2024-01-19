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


@app.get("/v3/getProducts")
async def read_user():

    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>

        SELECT ?recipeName ?dishType ?ingredient ?productName
        WHERE {{
            ?product :productName ?productName .
            SERVICE <http://localhost/service/edamam/findRecipes?keyword=cake> {{
                ?r :name ?recipeName ;
                :recipeCategory ?dishType ;
                :recipeIngredient ?ingredient .
            }}
            FILTER (STR(?productName) = STR(?ingredient))
        }}
        """
    )

    result = []
    for row in qres:
        print(row)

    return result


@app.get("/v3/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):

    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>

        SELECT ?recipeName ?dishType ?ingredient ?productName
        WHERE {{
            ?product :productName ?productName .
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?r :name ?recipeName ;
                :recipeCategory ?dishType ;
                :recipeIngredient ?ingredient .
            }}
            FILTER (STR(?productName) = STR(?ingredient))
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