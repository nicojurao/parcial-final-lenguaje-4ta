from flask import Flask, render_template, request,send_file
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

        
        videoId = url.replace('https://www.youtube.com/watch?v=', '')
        return render_template('info_video.html', videoId = videoId, url = url)
        

##########################################################################

@app.get('/descargar_1080p')
def descarga_1080p():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + ' 1080p' + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
###############################################################

@app.get('/descargar_720p')
def descarga_720p():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + ' 720p' + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
###############################################################
@app.get('/descargar_480p')
def descarga_480p():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestvideo[height<=480]+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + ' 480p' + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
###############################################################
@app.get('/descargar_360p')
def descarga_360p():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestvideo[height<=360]+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + ' 360p' + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
###############################################################
@app.get('/descargar_240p')
def descarga_240p():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestvideo[height<=240]+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + ' 240p' + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)
    
###############################################################
@app.get('/descargar_144p')
def descarga_144p():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestvideo[height<=144]+bestaudio',
        'postprocessors':[{
                'key': 'FFmpegMerger',


        }],
        'outtmpl': './static/' + titulo + ' 144p' + '.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)

###############################################################
@app.get('/descargar_mp3')
def descarga_mp3():
    url = request.args.get("url")
    formatos = request.args.get("formato")
    links = [url]
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
        url, download=False) 
        titulo=(meta['title'])



    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': './static/' + titulo + ' audio' + '.mp3',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)

    return send_file('./static/' + titulo + ' audio' + '.mp3', as_attachment=True)
###############################################################

app.run(debug=True)