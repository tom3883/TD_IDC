from fastapi import FastAPI
from rdflib import Graph
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
g = Graph()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    g = Graph()
    qres = g.query(
        f"""
        PREFIX : <http://recipes-project.com/schema#>
        SELECT ?recipeName
        WHERE {{
            SERVICE <http://localhost/service/edamam/findRecipes?keyword={recipe_name}> {{
                ?recipe :name ?recipeName .
            }}
        }}
        """
    )

    results = []
    for row in qres:
        results.append(row.recipeName)
        print(row.recipeName)

    return {"results": results}