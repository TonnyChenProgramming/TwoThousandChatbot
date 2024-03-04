from download_video import download_video
from video_to_text import mp4_to_text
from delete import delete
from filename_correction import filename_correction
def scrap_youtube():
    # this function stores video url and videod duration as in an array.
    video_list = [['https://www.youtube.com/watch?v=xxgbX9W82cg&t=25s',154],['https://www.youtube.com/watch?v=EFm8KEl-siw',95],['https://www.youtube.com/watch?v=BrmywDn4Uus',104],['https://www.youtube.com/watch?v=T83iG-imn18&t=3s',93]]
    with open('data.txt','w') as f:
        pass
    for video_data in video_list:
        downloaded_file = download_video(url=video_data[0])
        if downloaded_file is  not None:
            try:
                downloaded_file = filename_correction(downloaded_file)
                text = mp4_to_text(mp4_file=downloaded_file+'.mp4',video_duration=video_data[1])
                
                with open('data.txt','a',encoding='utf-8') as f:
                    f.write(downloaded_file + text+'\n') 
                #delete file to free up the space
                delete(downloaded_file+'.mp4')
                delete('processed.mp3')
                delete('processed.wav')
            except:
                print('fail to convert video to text')
if __name__=='__main__':
    scrap_youtube()