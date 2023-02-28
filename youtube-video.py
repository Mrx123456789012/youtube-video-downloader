import streamlit as st
from pytube import YouTube
import os
from googletrans import Translator

def download_video(video_url):
    try:
        # create a YouTube object
        yt = YouTube(video_url)

        # get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # download the video
        video_path = stream.download()

        # show a success message
        st.success("Video downloaded successfully!")

        # display the downloaded video
        st.video(video_path)

    except Exception as e:
        # show an error message
        st.error(f"Error downloading video: {str(e)}")


def app1():
    st.title("YouTube Video Downloader")
    video_url = st.text_input("Enter the YouTube video URL:")
    if st.button("Download"):
        download_video(video_url)
    st.write("Current working directory:", os.getcwd())



# Create the mult-page app
def main():
    st.set_page_config(page_title="shadan")

    pages = {
        "YouTube Video Downloader": app1,
    }

    st.sidebar.title("Select a page")
    selection = st.sidebar.radio("", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
