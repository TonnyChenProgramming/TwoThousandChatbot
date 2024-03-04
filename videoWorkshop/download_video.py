from pytube import YouTube
def download_video(url):
    # this function download the video in local and return the name of the mp4 file, if it file, return None
    is_pass = False
    counter = 1
    while not is_pass:
        try:
        
            yt = YouTube(url=url)
            yt_stream = yt.streams.filter(file_extension='mp4', resolution='720p').first()
            yt_stream.download('C:\\Users\\cta10\\OneDrive\\Desktop\\FancyProject\\webscrapping\\GrandGPT\\videoWorkshop')
            is_pass = True
            return str(yt.title)
        except:
            is_pass = False
            counter+=1
            if counter >= 10:
                print('fail to download the video')
                return None
if __name__ == '__main__':
    download_video('https://www.youtube.com/watch?v=rjYD2FgPUs4')