"""AssemblyAi Audio API and Streamlit Web"""
import assemblyai as aai
import streamlit as st

# replace with your API token
aai.settings.api_key = "ASSEMBLYAI_API_KEY"

st.title("AI Transcribe Audio/Video File/Live Stream V0.1")
st.subheader("Enter Media Link Below")

with st.form('mp3link'):
    linkurl = st.text_input("Enter Media Link")
    submit = st.form_submit_button('Transcribe')

if submit:

    # URL of the file to transcribe
    FILE_URL = linkurl
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)
    transcript_text = transcript.text
    st.write(transcript_text)

# file = open("log.txt", "a")
# file.write(str(transcript_text + "\n\n"))

# print(transcript.text)
#link1 = '[GitHub](http://github.com)'
#link2 = '[GitHub](http://github.com)'
#link3 = '[GitHub](http://github.com)'
#st.markdown(link1, unsafe_allow_html=True)
#st.markdown(link2, unsafe_allow_html=True)
#st.markdown(link3, unsafe_allow_html=True)
