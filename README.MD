# Aplicacion con python para descargar videos de Youtube utilizando youtube-dl
## Instalacion:
### Luego de clonar el repositorio, se debe crear un entorno virtual con el siguiente comando
    python -m venv env
### despues, se debe instalar el archivo requirements.txt con el siguiente comando
    pip install -r requirements.txt
### ahora debemos descargar la biblioteca de ffmpeg, para ello nos dirijmos a su pagina oficial y descargamos el archivo .zip, lo descomprimimos y agregamos al path la ruta donde esta la carpeta bin.
## Uso:
### Luego de instalar todos los requisitos necesarios, simplemente debemos activar nuestro entorno virtual con el comando:
    env/Scripts/activate
### Ahora ya podemos ejecutar el archivo app.py y estara todo funcionando
### El uso de la aplicacion es muy intuituvo, solo debemos ingresar la url del video que queramos descargar y darle click a buscar, en caso de el lik ser una lista de reproduccion no se mostrara el embebido pero si descargara el video seleccionado.
## Calidades:
### Video:
#### Hemos agregado 1 boton con las calidades mas comunes que son: 1080p, 720p, 480p, 360p, 240p y 144p, cualquier calidad de estas descargara el video con su maxima calidad en audio, en caso de que el video no cuente con la calidad seleccionada, se tomara la calidad anterior a esta, por ejemplo si queremos descargar un video a 1080 y este video no tiene esta calidad, se descargara a 720p.
### Audio:
#### Se proporciona 1 boton que descargara el audio de el video en formato .mp3 con la mejor calidad disponible.