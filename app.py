import streamlit as st
from moviepy.editor import *
import os

def convert_mp4_to_mp3(uploaded_file, output_file):
    with open(output_file, "wb") as out_file:
        out_file.write(uploaded_file.read())

    video = VideoFileClip(output_file)
    audio = video.audio
    audio.write_audiofile(output_file.replace(".mp3", "_converted.mp3"))

def main():
    st.title("MP4 to MP3 Converter")

    uploaded_file = st.file_uploader("Upload an MP4 file", type=["mp4"])

    if uploaded_file is not None:
        output_file_path = "output_audio.mp3"

        convert_button = st.button("Convert to MP3")

        if convert_button:
            convert_mp4_to_mp3(uploaded_file, output_file_path)
            st.success("Conversion completed!")

            st.audio(output_file_path.replace(".mp3", "_converted.mp3"), format='audio/mp3')

if __name__ == "__main__":
    main()
