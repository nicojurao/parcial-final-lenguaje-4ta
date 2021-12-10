from flask import Flask, render_template, request, redirect, flash, jsonify
import subprocess
import youtube_dl
import ffmpeg

app = Flask(__name__)



@app.get('/')
def home():
    return render_template('index.html')

@app.get("/info-video")
def infoVideo():
    url = request.args.get("url")
    output = subprocess.check_output('youtube-dl -F https://www.youtube.com/watch?v=cmWcnlWDv_I',shell=True)
    ydl_opts = {
        'listformats': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        meta = ydl.extract_info



    ydl_opts = {
        'listformats': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:

        meta = ydl.extract_info(
        url, download=False) 
        #titulo=(meta['title'])
        #formatos=(meta['format'])

        #(meta)
        print(type(meta))
        
        videoId = url.replace('https://www.youtube.com/watch?v=', '')
        return render_template('info_video.html', videoId = videoId, url = url)
        

##########################################################################

@app.get('/descargar_1080p')
def descarga_1080():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])
        print (formatos)


    ydl_opts = {
        'format': '399+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
###############################################################


app.run(debug=True)