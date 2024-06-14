from astrapy import DataAPIClient

def get_astra_client():
    token = "AstraCS:oOlKCcZQyKHKMotcHthdJNdR:f1899e48a075523dad5f9139177794968b78a2c483d5ab2d231ab59f3221f8a0"
    client = DataAPIClient(token)
    return client

def get_database(client, endpoint, namespace):
    try:
        db = client.get_database_by_api_endpoint(endpoint, namespace=namespace)
        return db
    except Exception as e:
        print(f"\nErro ao conectar ao banco de dados. {e}")
        return None
    
def get_collection(colecaoNome):
    client = get_astra_client()
    endpoint = "https://ca67a19b-41aa-4b80-9f80-9d0f548e7522-us-east-2.apps.astra.datastax.com"
    namespace = "mercadolivre"
    
    db = get_database(client, endpoint, namespace)
    
    if db:
        colecao = db.get_collection(colecaoNome)
        return colecao
    else:
        return None
    