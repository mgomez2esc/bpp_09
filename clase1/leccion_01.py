# Nombre: Miguel Gómez Gómez-Escalonilla
# Asignatura: Buenas practicas de programacion en Python
# Practica 1

import pandas as pd
from os.path import exists

try:
    df = pd.read_csv('finanzas2020[1].csv', sep='\t', index_col=False) # Leer CSV y separamos los valores
    list_months = df.columns 
    assert(len(list_months) == 12) # Comprueba si el Dataframe contiene 12 columnas
    assert(not df.empty) # Comprueba si el Dataframe no esta vacion
except IOError: 
    print('El archivo no existe') # En caso de no existir el fichero lanza una excepcion

max_row = len(df.index) # Numero total de filas
counter = 0
aux_min = 0
sum_ingresos = 0
sum_gastos = 0
mes = ''
my_dictionary = {'Enero': 0, 'Febrero': 0 , 'Marzo': 0, 'Abril': 0, 'Mayo': 0, 'Junio': 0,
                 'Julio': 0, 'Agosto': 0, 'Septiembre': 0, 'Octubre': 0, 'Noviembre': 0, 'Diciembre': 0 } 

'''
Bucles anidados. Recorremos primer el mes, y luego las 100 filas del mes. Comprobamos si es un caracter de tipo
numerico con el que podamos realizar operaciones. En caso afirmativo, hacemos la correspondente operacion y lo
añadimos al diccionario correspondiente al mes
'''
for month in list_months:
    monthly_expenditure = 0
    monthly_incomes = 0
    while counter < max_row:
        try:
            value = df[month][counter]
            if (value < 0):
                monthly_expenditure-=df[month][counter]
            if (value > 0):
                monthly_incomes+=df[month][counter]
            counter+=1
        except ValueError:
            print('El valor que aparece en el archivo es erroneo')
        except TypeError:
            counter+=1
    counter = 0
    my_dictionary[month] = {'Gastos': monthly_expenditure, 'Ingresos': monthly_incomes}

'''
Recorremos el diccionario para hacer las correspondientes operaciones necesarias para completar el
el ejercicio.
'''

for month, info in my_dictionary.items():
    for key in info: 
        if key == 'Gastos':
            if info[key] > aux_min:
                aux_min = info[key]
                mes = month
        sum_gastos -= info[key]
        if key == 'Ingresos':
            sum_ingresos += info[key]

# Pregunta 1: ¿Qué mes se ha gastado más?
print(f'El mes que mas se ha gastado ha sido {mes} con un gasto total {aux_min}')

# Pregunta 2: ¿Qué mes se ha ahorrado más?
mes_ahorro = df.describe().loc['mean'].idxmax()
mes_ahorro_valor = df.describe().loc['mean'].max()
print(f'El mes que mas se ha ahorrado ha sido {mes_ahorro} con una media {mes_ahorro_valor}')

# Pregunta 3: ¿Cuál es la media de gastos al año?
media_gastos_año = df.describe().loc['mean'].mean()
print(f'La media de gastos al año es: {media_gastos_año}')

# Pregunta 4: ¿Cuál ha sido el gasto total a lo largo del año?
print(f'El total de gastos al año es de {sum_gastos}')

# Pregunta 5: ¿Cuáles han sido los ingresos totales a lo largo del año?
print(f'El total de ingresos al año es de {sum_ingresos}')

