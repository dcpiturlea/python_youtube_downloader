# pip install git+https://github.com/nficano/pytube.git
from pytube import YouTube

while True:
    link = input("Introdu linkul: ")
    try:
        yt = YouTube(link)
        # Title of video
        print("Titlu: ", yt.title)
        # Number of views of video
        print("Numar vizualizari: ", yt.views)
        # Length of the video
        print("Lungime video: ", yt.length, " seconds")
        # Description of video
        print("Descriere: ", yt.description)
        # Rating
        print("Rating: ", yt.rating)

        # printing all the available streams
        print(yt.streams)
        print(yt.streams.filter(only_audio=True))
        print(yt.streams.filter(only_video=True))
        print(yt.streams.filter(progressive=True))
        ys = yt.streams.get_highest_resolution()
        try:
            ys.download()
        except:
            print("Nu a putut fi downloadat!")
    except:
        print("Nu ai introdus un link valid!")

