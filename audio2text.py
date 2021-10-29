############################################
############################################
# code by quy anh dao
# please install module
# pip install speechrecognition
# pip install pydub
# pip install ffmpeg-python

# install  FFmpeg and path file bin
# https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z

import speech_recognition as sr
import sys
import os
from pydub import AudioSegment

# Folder project
folder_path = "E:/hoc_tap/nam_4_ki_1/dspp/btl1/"
# folder storage voice
folder_name = "test_folder/voice_test"
folder_audio = os.path.join(folder_path, folder_name)

r = sr.Recognizer()
# change voice to text


def voice2text(filename):
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language="vi-VN")

    return text

# make audio longer for capture clean sound
# and more 1 second to header and footer of audio file


def adjust_audio(audio_path):
    # create 1 sec of silence audio segment
    one_sec_segment = AudioSegment.silent(duration=1000)
    # read wav file to an audio segment
    song = AudioSegment.from_wav(audio_path)
    # Add above two audio segments
    final_song = one_sec_segment + song + one_sec_segment
    # Either save modified audio
    final_song.export(audio_path, format="wav")

# Create And Write to file.txt


def caw(audio_path, content):
    # change .wav to .txt
    txt_name = os.path.splitext(audio_path)[0]+".txt"
    # create .txt file and write
    with open(txt_name, "w+", encoding="utf-8") as file:
        file.write(content)

# main file


def main():
    for audio_file_name in os.listdir(folder_audio):
        if audio_file_name.endswith(".wav"):
            print("---------------------------------------")
            # make audio path
            audio_path = os.path.join(folder_audio, audio_file_name)
            print("audio_path:", audio_path)
            # reading file
            print("Reading file:", audio_file_name)
            text = voice2text(audio_path)
            ###########################################
            # use this ONLY on the first time you run the code
            # or this will destroy your audio file
            ###########################################
            # adjust_audio(audio_path)
            caw(audio_path, text)
            print(text)
    print("complete!!!!!")


main()
# test repo
