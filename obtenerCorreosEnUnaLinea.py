import os
import re

carpeta_html = "Correos en Kissflow"
archivo_salida = "codigos_html_ordenados.txt"

def convertir_html_a_una_linea(contenido):
    contenido = contenido.replace("\n", "")
    contenido = contenido.replace("\r", "")
    contenido = contenido.replace("\t", "")
    contenido = re.sub(r">\s+<", "><", contenido)
    contenido = re.sub(r"\s{2,}", " ", contenido)
    return contenido.strip()

def obtener_numero(nombre_archivo):
    numeros = re.findall(r"\d+", nombre_archivo)
    return int(numeros[0]) if numeros else 0

archivos_html = [
    archivo for archivo in os.listdir("Correos en Kissflow")
    if archivo.lower().endswith(".html")
]

# Orden descendente usando el número del nombre
#archivos_html.sort(key=obtener_numero, reverse=True)

with open(archivo_salida, "w", encoding="utf-8") as salida:
    for archivo in archivos_html:
        ruta_archivo = os.path.join(carpeta_html, archivo)

        with open(ruta_archivo, "r", encoding="utf-8") as html:
            contenido = html.read()

        contenido_limpio = convertir_html_a_una_linea(contenido)

        salida.write(f"===== {archivo} =====\n")
        salida.write(contenido_limpio)
        salida.write("\n\n")

print("Archivo TXT generado correctamente:", archivo_salida)