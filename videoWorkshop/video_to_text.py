import ffmpeg
import os 
import speech_recognition as sr

def mp4_to_text(mp4_file,video_duration):
    # copy from https://medium.com/mlthinkbox/convert-an-mp4-video-file-into-a-text-summary-using-python-6ba0002b9987
    #video_duration parameter is in seconds
    current_directory= os.getcwd()
    ffmpeg_home = r'C:\pythonFile\ffmpeg\bin\ffmpeg'
    #convert mp4 to mp3
    object = f'{ffmpeg_home} -i "{current_directory}"/"{mp4_file}" "{current_directory}"/processed.mp3'
    print(object)
    os.system(object)
    #convert mp3 to wav
    object = f'{ffmpeg_home} -i "{current_directory}"/processed.mp3 "{current_directory}"/processed.wav'
    os.system(object)
    # declare recogniser and audio variable 
    r = sr.Recognizer()
    audio = sr.AudioFile('processed.wav')

    with audio as source:
        audio = r.record(source=source,duration=video_duration)
        text = r.recognize_google(audio)
    return text

if __name__ == '__main__':
    print(mp4_to_text(mp4_file='Thevideo.mp4',video_duration=93))