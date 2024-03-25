import requests


def sendSPARQLQuery(query):
    """
    Sends a SPARQL query to the Wikidata SPARQL endpoint and returns the response data.

    Args:
        query (str): The SPARQL query to send.

    Returns:
        dict: The response data in JSON format.
    """
    url = "https://query.wikidata.org/sparql"

    resp = requests.get(url, params={"format": "json", "query": query})
    data = resp.json()

    return data
