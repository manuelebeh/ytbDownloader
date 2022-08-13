import os
import sys
import pytube.request
from pytube import YouTube

pytube.request.default_range_size = 1048576


def create_directory(name):
    path = sys.path[0]
    if not (os.path.isdir(f'{path}/{name}')):
        path = os.path.join(sys.path[0], name)
        os.mkdir(path)


def information():
    print(f"Author: {youtubeVideo.author}")
    print(f"Title: {youtubeVideo.title}")
    print(f"Description: {youtubeVideo.description}")
    print(f"Duration: {youtubeVideo.length}s")
    print(f"Publish Date: {youtubeVideo.publish_date}\n")

    print("STREAMS:")


def download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Download progress {int(percent)}%")


print("Welcome to the YTB downloader. It's a simple tool make with Python that allow you to download video or simple "
      "audio in YouTube \n")

print("Select an option")
print(
    "1) Download Video and Audio \n2) Download Only Video \n3) Download Only Audio \n4) Help \n5) About The Creator\n")
choice = input("Your choice: ")
print('\n')

if choice == '1':
    url = input("Enter the link of the YouTube video to download: ")
    youtubeVideo = YouTube(url)
    youtubeVideo.register_on_progress_callback(download_progress)
    print('\n')
    information()
    allStream = youtubeVideo.streams.filter(progressive=True).order_by('resolution')
    print(allStream, " ", end="\n")
    print('\n')
    iTag = int(input("Choose the itag corresponding to the stream you want to download: "))
    streamChoice = youtubeVideo.streams.get_by_itag(iTag)
    print('\n')

    directoryName = 'Downloads'
    create_directory(directoryName)
    path = sys.path[0]
    print("The download begin...")
    streamChoice.download(output_path=f'{path}/{directoryName}')
    print(f"Download complete.")
    print("Thanks for using the app")
    # open(f'{path}\\{directoryName}', 'a')
