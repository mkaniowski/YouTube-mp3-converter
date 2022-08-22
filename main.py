from pytube import YouTube
import os


def main():
    url = input('Give an URL to a video: ')
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    file = stream.download(output_path='./music')

    base, ext = os.path.splitext(file)
    os.rename(file, base + '.mp3')
    print('Finished downloading')


if __name__ == '__main__':
    main()
