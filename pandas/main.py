import pandas as pd

# series
serie_uno = pd.Series([1, 2, 6, 7, 8]) # integers (dtype int64)
print(serie_uno)
print(serie_uno[0])

serie_dos = pd.Series([2.34, 5.76, 9.07]) # floats (dtype float64)
print(serie_dos)
print(serie_dos[1])

serie_tres = pd.Series([8, 4.85, 55, 82.99]) # mix de integers y floats (se convertiran a floats)
print(serie_tres)
print(serie_tres[0])
print(serie_tres[1])
print(serie_tres[2])
print(serie_tres[3])

serie_cuatro = pd.Series(["uno", "dos", "tres"]) # dtype object
print(serie_cuatro)
print(serie_cuatro[1])

serie_cinco = pd.Series([3.9, 99, "tres"]) # se convertira a dtype object
print(serie_cinco)
print(serie_cinco[1])

# data frames
datos = {'NAME': ["Alice", "Jhon", "Albert"],
'AGE': [33, 40, 31],
'CITY': ["Houston", "St Louis", "Tennesse"]}

mi_dataframe = pd.DataFrame(datos) 
print(mi_dataframe)

# read csv
pokemon_data = pd.read_csv('pokemon_data.csv')
print(pokemon_data.head())

