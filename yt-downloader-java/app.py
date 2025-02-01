from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url'].strip()  # Elimina espacios en blanco al inicio y al final
    format_choice = request.form['format']

    # Validación en el backend
    if not url:
        return render_template('index.html', error="Error: Por favor, ingresa una URL válida de YouTube.")

    ydl_opts = {}
    if format_choice == "mp4":
        ydl_opts = {
            'format': 'bestvideo+bestaudio',
            'outtmpl': '%(title)s.%(ext)s',
        }
    elif format_choice == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': 'mp3',
            'outtmpl': '%(title)s.%(ext)s',
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)
            return send_file(file_path, as_attachment=True)
    except yt_dlp.utils.DownloadError as e:
        error_message = f"Error al descargar: {e}"
        if "HTTP Error 400" in str(e):
            error_message = "Error: No se pudo descargar el video. Intenta con otro enlace o actualiza yt-dlp."
        return render_template('index.html', error=error_message)
    except Exception as e:
        return render_template('index.html', error=f"Error inesperado: {e}")

if __name__ == '__main__':
    app.run(debug=True)