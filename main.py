import pandas as pd
from api.api import crear_cliente, obtener_datos
from ui.ui import obtener_entrada_usuario, imprimir_datos

def main():
    # app token
    app_token = "iiEql2dA3WgV8OMOE0fONjfps"
    client = crear_cliente(app_token)

    # Obtener entrada del usuario
    limit, departamento_nom = obtener_entrada_usuario()
    
    if limit is None or departamento_nom is None:
        return

    try:
        # Solicitar datos a la API
        dataset_id = "gt2j-8ykr"
        results = obtener_datos(client, dataset_id, limit, departamento_nom)
        
        # Convertir los resultados en un DataFrame de pandas
        results_df = pd.DataFrame.from_records(results)
        
        # Filtrar DataFrame
        specific_info_df = results_df[['departamento_nom', 'ciudad_municipio_nom', 'edad', 'tipo_recuperacion', 'estado']]
        
        # Imprimir datos
        imprimir_datos(specific_info_df)
    
    except KeyError as e:
        print(f"Error: el municipio no existe en los resultados.")
    except Exception as e:
        print(f"Error: cantidad de registros invalidos")

if __name__ == "__main__":
    main()
