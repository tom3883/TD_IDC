from fastapi import FastAPI
from rdflib import Graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

g = Graph()
g.parse("/Users/thomaspaul/Documents/Polytech/S9/IngenierieConnaissances/TD/projet_final/recipe_schema.ttl")
g.parse("/Users/thomaspaul/Documents/Polytech/S9/IngenierieConnaissances/TD/projet_final/recipe_product_categories.ttl")
g.parse("/Users/thomaspaul/Documents/Polytech/S9/IngenierieConnaissances/TD/projet_final/recipe_categories.ttl")

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
    print("--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))
    return {"result" : "done"}

@app.get("/test")
async def root():
    return {"result" : "test ok"}

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


@app.get("/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):

    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        SELECT  ?recipeName ?dishType
        WHERE {{
            ?c a :RecipeCategory ;
            skos:prefLabel ?dishType .
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?recipe :name ?recipeName ;
                :recipeCategory ?dishType .
            }}
        }}
        """
    )

    results = []
    for row in qres:
        results.append([row.recipeName, row.dishType])

    return {"results": results}

@app.get("/v2/getRecipes/{recipe_name}")
async def read_user(recipe_name: str):

    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        SELECT ?recipeName ?dishType
        WHERE {{
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?recipe :name ?recipeName ;
                :recipeCategory ?dishType .
            }}
        }}
        """
    )

    results = []
    for row in qres:
        results.append([row.recipeName, row.dishType])

    return results

