import moviepy.editor as mp
import speech_recognition as sr

# Load the video file
video = mp.VideoFileClip("harvard.mp4")
print('done1')
# Extract audio from the video
audio = video.audio
audio.write_audiofile("extracted_audio.wav")
print('done2')

# Initialize the recognizer
recognizer = sr.Recognizer()
print('done3')

# Load the audio file
with sr.AudioFile("extracted_audio.wav") as source:
    audio_data = recognizer.record(source)  # Read the entire audio file
print('done4')

# Recognize the speech in the audio
try:
    text = recognizer.recognize_google(audio_data)
    print("Extracted Text: ", text)

    # Save the extracted text to a file
    with open("extracted_text.txt", "w") as text_file:
        text_file.write(text)
       

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
print('done6')