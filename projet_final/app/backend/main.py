from fastapi import FastAPI
from rdflib import Graph

app = FastAPI()
g = Graph()

@app.get("/getProducts")
async def root():
    g.parse('../../csvw/walmart_products.ttl')

    q = """
        PREFIX : <http://recipes-project.com/schema/>
        select ?n where {
            ?p :productName ?n
        }
    """

    results = []
    for r in g.query(q):
        results.append(r["n"])

    return {"results": results}