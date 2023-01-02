import streamlit as st
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

st.title('Noise Reduction Web App')

# Add a file uploader widget
audio_file = st.file_uploader('Upload an audio file:', type='mp3')

if audio_file is not None:
    # Load the audio file as a waveform
    rate, data = wavfile.read(audio_file)

    # Use a median filter to reduce noise
    data = signal.medfilt(data, kernel_size=3)

    # Convert the waveform back to an audio file
    librosa.output.write_wav('noise_reduced.wav', data, rate)
    audio = AudioSegment.from_wav('noise_reduced.wav')
    audio.export('noise_reduced.mp3', format='mp3')

    # Add a button to download the resulting audio file
    if st.button('Export as mp3'):
        with open('noise_reduced.mp3', 'rb') as f:
            audio_bytes = f.read()
        st.markdown('Audio exported as **noise_reduced.mp3**')
        st.audio(audio_bytes, format='audio/mpeg')
