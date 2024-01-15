
# URL-encoded query: construct where {?s ?p ?o}
CONSTRUCT=construct%20WHERE%20%7B%20%3Fs%20%3Fp%20%3Fo%20%7D%20

# Parameter "keyword" is expected by the SPARQL micro-service, whereas "query" is imposed by the SPARQL protocol
curl --header "Accept: text/turtle" "http://localhost/service/edamam/findRecipes?keyword=cake&query=${CONSTRUCT}"