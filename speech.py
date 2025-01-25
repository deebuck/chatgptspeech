#!/bin/python
import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API key
openai.api_key = 'your-api-key'

# Initialize TTS engine
engine = pyttsx3.init()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    user_input = get_audio()
    if "exit" in user_input.lower():
        print("Exiting...")
        break
    print(f"You said: {user_input}")
    gpt_response = chat_with_gpt(user_input)
    print(f"ChatGPT: {gpt_response}")
    speak(gpt_response)
    
