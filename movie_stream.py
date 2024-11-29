import streamlit as st
import random


class Movie_Column():
    def __init__(self, key):
        if key == 1:
            index = 0
        else:
            index = 1
        st.markdown("### ΔQ-1の方式")
        mode = st.selectbox("", ("平均との差分", "前日との差分"), key=key)

        st.markdown("### -1〜1への正規化")
        normalization = st.selectbox("",("ON", "OFF"), key=key+1, index=index)

        st.markdown("### 窓の長さ")
        win_length = st.selectbox("",("15 seconds", "30 minutes"), key=key+2)

        if mode == "前日との差分":
            self.mode = "_dif"
        else:
            self.mode = ""

        if normalization == "ON":
            self.normalization = "_norm"
        else:
            self.normalization = ""

        if win_length == "15 seconds":
            self.win_length = "15s"
        else:
            self.win_length = "30m"


if "number" not in st.session_state:
    st.session_state.number = 0

col1, col2 = st.columns([1, 1])

if st.session_state.number == 0:
    st.session_state.number = 1
else:
    st.session_state.number = 0

with col1:
    mc_1 = Movie_Column(1)
    file_name = "win_" + mc_1.win_length + "/slope" + mc_1.mode + mc_1.normalization + ".mp4"
    video_file1 = open(file_name, "rb")
    video_bytes1 = video_file1.read()
    st.video(video_bytes1, muted=True, autoplay=True, start_time=st.session_state.number)

with col2:
    mc_2 = Movie_Column(4)
    file_name = "win_" + mc_2.win_length + "/slope" + mc_2.mode + mc_2.normalization + ".mp4"
    video_file2 = open(file_name, "rb")
    video_bytes2 = video_file2.read()
    st.video(video_bytes2, muted=True, autoplay=True, start_time=st.session_state.number)
