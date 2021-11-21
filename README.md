# CCat_save
Guarda las respuestas de un perfil dado de Curious Cat, bien completo o bien entre dos fechas dadas

Está probado con Python 3.6

El script tiene 3 parámetros:

1) Perfil de Curious Cat que se quiere descargar
2) Fecha mínima de la respuesta que se descarga. Si se deja a 0, descarga desde la primera existente.
3) Fecha máxima de la respuesta que se descarga. Si se deja a 0, descarga hasta la más reciente.

El script solo utiliza la librería externa requests, como se puede ver en el requirements.txt

# Ejemplo:

- Descargar completo el perfil Danielquinn_: python CC_guarda.py Danielquinn_ 0 0
- Descargar el perfil Danielquinn_ entre dos fechas: python CC_guarda.py Danielquinn_ 01/07/2017 01/12/2018

# Instalar desde un exe (sin tener Python)

- Descargar CC_guarda.zip y descomprimir la carpeta
- Dentro de esa carpeta está el ejecutable CC_guarda.exe. Se puede ejecutar directamente desde línea de comandos (cmd) con los parámetros ya comentados. Por ejemplo, para descargar el perfil Danielquinn_ completo (para especificar fechas, ponerlas en lugar de los 0s): CC_guarda.exe Danielquinn_ 0 0
