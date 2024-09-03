from sodapy import Socrata

def crear_cliente(app_token):
    #Crea un cliente para Socrata con el app_token
    return Socrata("www.datos.gov.co", app_token)

def obtener_datos(client, dataset_id, limit, departamento_nom):
    #solicitud tipo GET a la api
    return client.get(dataset_id, limit=limit, departamento_nom=departamento_nom)
