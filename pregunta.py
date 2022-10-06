"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    import pandas as pd
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.drop(df.columns[0],axis = 1)
    
    df.drop_duplicates(inplace=(True))
    df.dropna(inplace=(True))

    lowerCase_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio']
    for column in lowerCase_columns:
        df[column] = df[column].apply(lambda x: x.lower())
    df['línea_credito'] = df['línea_credito'].apply(lambda x: x.lower())

    #Limpieza fecha
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(check_dates)

    #Limpieza monto
    df['monto_del_credito'] = df['monto_del_credito'].apply(check_prices)

    #Limpieza línea_crédito
    df['línea_credito'] = df['línea_credito'].apply(check_credits)

    #Otra limpieza
    df['idea_negocio'].replace({" ": '_'}, inplace=(True),  regex=True)
    df['idea_negocio'].replace({"-": '_'}, inplace=(True),  regex=True)	
    df['idea_negocio'].replace({"_": ' '}, inplace=(True),  regex=True)

    df['barrio'].replace({" ": '_'}, inplace=(True),  regex=True)
    df['barrio'].replace({"-": '_'}, inplace=(True),  regex=True)
    df['barrio'].replace({"_": ' '}, inplace=(True),  regex=True)	


    df.drop_duplicates(inplace=(True))
    
    return df

def check_prices(price):
    if(price[0] == '$'):
        price = price[2:-3]
        price = price.replace(',', '')
    return price

def check_credits(credit):
    credit = credit.replace('_',' ')
    credit = credit.replace('-',' ')
    if('diaria' in credit):
      credit = 'solidaria'
    return credit

def check_dates(date):
    if (date[1] == '/') or (date[2] == '/'):
           partes = date.split("/")
           date = "/".join(reversed(partes))
    return date
        
