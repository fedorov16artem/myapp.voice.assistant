import os, webbrowser, sys, requests, subprocess, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи

def speaker(text):
    engine.say(text)
    engine.runAndWait()

def browser():
    webbrowser.open('https://vk.com/tema16fed', new=2)
def browser1():
    webbrowser.open('', new=3)
def game():
    subprocess.Popen('C:\Program Files (x86)\Steam\Steam.exe')
def weather():
    print('weather')
def offBot():
    sys.exit()
def offpc():
    print('пк выключен')
def passive():
    pass