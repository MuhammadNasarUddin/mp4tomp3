from flask import Flask, render_template, request,send_file
from moviepy.editor import *
import os

app = Flask(__name__)

def convert_mp4_to_mp3(uploaded_file, output_file):
    with open(output_file, "wb") as out_file:
        out_file.write(uploaded_file.read())

    video = VideoFileClip(output_file)
    audio = video.audio
    audio.write_audiofile(output_file.replace(".mp3", "_converted.mp3"))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            try:
                output_file_path = "output_audio.mp3"
                convert_mp4_to_mp3(uploaded_file, output_file_path)
                return render_template('mp4.html', message="Conversion completed!", converted_file=output_file_path.replace(".mp3", "_converted.mp3"))
            except Exception as e:
                return render_template('mp4.html', error_message=str(e))
    return render_template('mp4.html')

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
