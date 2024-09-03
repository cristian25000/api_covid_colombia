def obtener_entrada_usuario():
    #solicita datos al usuario
    try:
        limit = int(input("Introduce el número máximo de resultados a obtener: "))
        departamento_nom = input("Introduce el nombre del departamento: ").upper()
        return limit, departamento_nom
    except ValueError:
        print("Por favor, introduce un número válido para el límite.")
        return None, None

def imprimir_datos(specific_info_df):
    #imprime el dataframe con .format 
    for index, row in specific_info_df.iterrows():
        formatted_string = "Departamento: {departamento_nom:<20} | Ciudad/Municipio: {ciudad_municipio_nom:<20} | Edad: {edad:>3} | Tipo de Recuperación: {tipo_recuperacion:<20} | Estado: {estado:<15}".format(
            ciudad_municipio_nom=row['ciudad_municipio_nom'],
            departamento_nom=row['departamento_nom'],
            edad=row['edad'],
            tipo_recuperacion=row['tipo_recuperacion'],
            estado=row['estado']
        )
        print(formatted_string)
