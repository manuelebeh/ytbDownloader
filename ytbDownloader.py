import os
import sys
import pytube.request
from pytube import YouTube
import json

pytube.request.default_range_size = 1048576


def create_yt_object():
    url = input("\nEnter the Url: ")
    global youtube_video
    youtube_video = YouTube(url)
    youtube_video.register_on_progress_callback(download_progress)
    information()


def information():
    global author, title, duration, publish_date
    author = str({youtube_video.author})
    title = str({youtube_video.title})
    duration = str({youtube_video.length})
    publish_date = str({youtube_video.publish_date})

    print(f"\nAuthor: {author}")
    print(f"Title: {title}")
    print(f"Duration: {duration}s")
    print(f"Publish Date: {publish_date}\n")
    create_json()


def download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Download progress {int(percent)}%")


def create_directory(name):
    path = sys.path[0]
    if not (os.path.isdir(f'{path}/{name}')):
        path = os.path.join(sys.path[0], name)
        os.mkdir(path)


def download():
    directory_name = 'Downloads'
    create_directory(directory_name)
    path = sys.path[0]
    print("\nThe download begin...")
    stream.download(output_path=f'{path}/{directory_name}')
    print(f"Download complete.")
    print("\nThanks for using the app")
    os.startfile(f'{path}/{directory_name}')


# function to add information about downloaded files into JSON
def create_json():
    sample_dict = {"author": author, "title": title, "duration": duration,
                   "publish_date": publish_date}
    with open("download_list.json", 'r+',  encoding='utf-8') as f:
        data = json.load(f)
        data["download"].append(sample_dict)
        f.seek(0)
        # ensure_ascii=False to encode Unicode as-is into JSON
        json.dump(data, f, indent=2, ensure_ascii=False)


def audio_video_download():
    create_yt_object()
    global stream
    print("\nChoose the quality of your downloads:\n 1) 140p\n 2) 360p\n 3) 720p")
    quality_choice = input("Choice: ")
    if quality_choice == '1':
        stream = youtube_video.streams.get_by_itag(17)
        download()
    elif quality_choice == '2':
        stream = youtube_video.streams.get_by_itag(18)
        download()
    elif quality_choice == '3':
        stream = youtube_video.streams.get_by_itag(22)
        download()


def main():
    print("Welcome to the YTB downloader.\n"
          "It's a simple tool make with Python that allow you to download video or simple audio in YouTube \n")

    print("Select an option")
    print("1) Download Video and Audio \n"
          "2) Download Only Video \n"
          "3) Download Only Audio \n"
          "4) Help \n"
          "5) About The Creator\n")
    choice = input("Your choice: ")

    if choice == '1':
        audio_video_download()


if __name__ == '__main__':
    main()
