
def find_average(values):
    result = 0
    for v in values:
        result += v
    return result / len(values)


print("AVERAGE", find_average([5,6, 7, 8]))





import streamlit as st
from pydub import AudioSegment
from pydub.silence import split_on_silence

st.title('Noise Reduction Web App')


audio_file = st.file_uploader('Upload an audio file:', type='mp3')

if audio_file is not None:

audio = AudioSegment.from_mp3(audio_file)


segments = split_on_silence(audio, min_silence_len=1000, silence_thresh=-16)


concatenated_audio = AudioSegment.silent(duration=0)
for segment in segments:
concatenated_audio += segment


if st.button('Export as mp3'):
with open('noise_reduced.