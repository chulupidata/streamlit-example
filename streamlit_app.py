import streamlit as st
from pydub import AudioSegment
from pydub.silence import split_on_silence

st.title('Noise Reduction Web App')

# Add a file uploader widget
audio_file = st.file_uploader('Upload an audio file:', type='mp3')

if audio_file is not None:
    # Load the audio file as an AudioSegment object
    audio = AudioSegment.from_mp3(audio_file)

    # Split the audio file into segments based on silence
    segments = split_on_silence(audio, min_silence_len=1000, silence_thresh=-16)

    # Concatenate the segments back together
    concatenated_audio = AudioSegment.silent(duration=0)
    for segment in segments:
        concatenated_audio += segment

    # Add a button to download the resulting audio file
    if st.button('Export as mp3'):
        with open('noise_reduced.mp3', 'wb') as f:
            concatenated_audio.export(f, format='mp3')
        st.markdown('Audio exported as **noise_reduced.mp3**')
