import json
import pandas as pd
from SPARQLWrapper import JSON, POST, POSTDIRECTLY, SPARQLWrapper


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

    print(out)

    return 'Done'


query = '''
PREFIX : <http://recipes-project.com/schema#>

SELECT ?recipeName ?dishType ?ingredient ?productName
WHERE {
    ?product :productName ?productName .
    SERVICE <http://localhost/service/edamam/findRecipes?keyword=cake> {
        ?r :name ?recipeName ;
           :recipeCategory ?dishType ;
           :recipeIngredient ?ingredient .
    }
    FILTER (STR(?productName) = STR(?ingredient))
}
'''

wds_Corese = 'http://localhost:8080/sparql'

df = sparql_service_update(wds_Corese, query)
print(df)