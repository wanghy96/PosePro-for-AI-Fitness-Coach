import streamlit as st


st.title('AI深蹲教练')


recorded_file = 'output_sample.mp4'
sample_vid = st.empty()
sample_vid.video(recorded_file)