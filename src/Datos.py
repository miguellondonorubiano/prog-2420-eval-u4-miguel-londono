
def main():
    import os
import csv
import statistics
import matplotlib.pyplot as plt

# Función para listar archivos en el directorio actual o en una ruta específica
def listar_archivos(ruta='.'):
    archivos = os.listdir(ruta)
    for archivo in archivos:
        print(archivo)
##Submenú para Archivos de Texto
# Función para contar el número de palabras en un archivo de texto
def contar_palabras(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
    palabras = contenido.split()
    print(f"El archivo tiene {len(palabras)} palabras.")

# Función para reemplazar una palabra en un archivo de texto
def reemplazar_palabra(archivo, buscar, reemplazar):
    with open(archivo, 'r') as f:
        contenido = f.read()
    contenido = contenido.replace(buscar, reemplazar)
    with open(archivo, 'w') as f:
        f.write(contenido)
    print(f"Se ha reemplazado '{buscar}' por '{reemplazar}' en el archivo.")

# Función para contar el número de caracteres en un archivo de texto
def contar_caracteres(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
    total_caracteres = len(contenido)
    caracteres_sin_espacios = len(contenido.replace(' ', ''))
    print(f"Total de caracteres (incluyendo espacios): {total_caracteres}")
    print(f"Total de caracteres (sin espacios): {caracteres_sin_espacios}")
##Submenú para Archivos CSV
# Función para mostrar las primeras 15 filas de un archivo CSV
def mostrar_primeras_filas(archivo):
    with open(archivo, 'r') as f:
        lector_csv = csv.reader(f)
        filas = 0
        for fila in lector_csv:
            if filas < 15:
                print(fila)
                filas += 1
            else:
                break

# Función para calcular estadísticas en una columna de un archivo CSV
def calcular_estadisticas(archivo, columna):
    datos = []
    with open(archivo, 'r') as f:
        lector_csv = csv.DictReader(f)
        for fila in lector_csv:
            try:
                valor = float(fila[columna])
                datos.append(valor)
            except ValueError:
                continue
    
    if datos:
        print(f"Datos: {len(datos)}")
        print(f"Promedio: {statistics.mean(datos)}")
        print(f"Mediana: {statistics.median(datos)}")
        print(f"Máximo: {max(datos)}")
        print(f"Mínimo: {min(datos)}")
    else:
        print("No se encontraron datos numéricos en la columna.")

# Función para graficar una columna de un archivo CSV
def graficar_columna(archivo, columna):
    datos = []
    with open(archivo, 'r') as f:
        lector_csv = csv.DictReader(f)
        for fila in lector_csv:
            try:
                valor = float(fila[columna])
                datos.append(valor)
            except ValueError:
                continue

    if datos:
        plt.plot(datos)
        plt.title(f"Gráfico de la columna '{columna}'")
        plt.xlabel("Índice")
        plt.ylabel("Valor")
        plt.show()
    else:
        print("No se encontraron datos numéricos en la columna.")

# Función principal para mostrar el menú y manejar la selección de opciones
def main():
    while True:
        print("\n### Menú Principal ###")
        print("1. Listar archivos presentes en la ruta actual o ingresar una ruta")
        print("2. Procesar archivo de texto (.txt)")
        print("3. Procesar archivo separado por comas (.csv)")
        print("4. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == '1':
            ruta = input("Ingrese la ruta o presione Enter para usar la ruta actual: ")
            if ruta == '':
                ruta = '.'
            listar_archivos(ruta)
        
        elif opcion == '2':
            archivo_txt = input("Ingrese el nombre del archivo de texto (.txt): ")
            
            print("\n### Submenú para archivos de texto (.txt) ###")
            print("1. Contar número de palabras")
            print("2. Reemplazar una palabra por otra")
            print("3. Contar el número de caracteres")
            
            opcion_txt = input("Elija una opción: ")
            
            if opcion_txt == '1':
                contar_palabras(archivo_txt)
            elif opcion_txt == '2':
                buscar = input("Ingrese la palabra a buscar: ")
                reemplazar = input("Ingrese la palabra de reemplazo: ")
                reemplazar_palabra(archivo_txt, buscar, reemplazar)
            elif opcion_txt == '3':
                contar_caracteres(archivo_txt)
            else:
                print("Opción no válida.")
        
        elif opcion == '3':
            archivo_csv = input("Ingrese el nombre del archivo CSV (.csv): ")
            
            print("\n### Submenú para archivos CSV ###")
            print("1. Mostrar las 15 primeras filas")
            print("2. Calcular estadísticas de una columna")
            print("3. Graficar una columna completa con los datos")
            
            opcion_csv = input("Elija una opción: ")
            
            if opcion_csv == '1':
                mostrar_primeras_filas(archivo_csv)
            elif opcion_csv == '2':
                columna = input("Ingrese el nombre de la columna: ")
                calcular_estadisticas(archivo_csv, columna)
            elif opcion_csv == '3':
                columna = input("Ingrese el nombre de la columna: ")
                graficar_columna(archivo_csv, columna)
            else:
                print("Opción no válida.")
        
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
    

