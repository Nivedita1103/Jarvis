import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import pygame
import pywhatkit as kit
import sys
import webbrowser
import pyjokes
import pyautogui
from PyQt5 import QtWidgets 
from PyQt5 import QtCore
from PyQt5 import QtGui 
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis import Ui_MainWindow
import pywikihow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Nivedita!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Nivedita!")

    else:
        speak("Good Evening Nivedita!")

    speak("Jarvis this side. How may I help you ?")

class mainT(QThread):
    def __init__(self):
        super (mainT,self).__init__()
    def run(self):
        self.JARVIS()
    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=50, phrase_time_limit=30)
        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"User said: {self.query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return self.query

    def JARVIS(self):
        wishme() 
        while True:
            # if 1:
            self.query = self.takeCommand().lower()

            if 'who are you' in self.query:
                speak("I'm your virtual assistant Jarvis!")
            elif 'how are you' in self.query:
                speak("I'm great! Glad you asked")
            elif 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in self.query:
                webbrowser.open("https://www.youtube.com/")
            elif 'open google' in self.query:
                webbrowser.open("https://www.google.com/")
            elif 'open linkedin' in self.query:
                webbrowser.open("https://www.linkedin.com")
            elif 'time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif 'open word' in self.query:
                bpath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(bpath)
            elif 'open chrome' in self.query:
                npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(npath)
            elif 'song' in self.query:
                speak("which song would you like to hear?")
                ps = self.takeCommand().lower()
                kit.playonyt(f"{ps}")
            elif 'joke' in self.query:
                speak(pyjokes.get_joke())
            elif 'thank you' in self.query:
                speak("Always a pleasure!")
            elif 'close word' in self.query:
                speak('closing document')
                os.system("taskkill/f /im WINWORD.EXE")
            elif 'screenshot' in self.query:
                speak('Please tell me a name for screenshot file')
                name= self.takeCommand().lower()
                speak('hold the screen for a moment till i take the screenshot')
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak('screenshot is saved in main folder')
            elif 'exit' in self.query:
                speak("good bye Nivedita! have a good day")
                exit()
            elif 'volume up' in self.query:
                pyautogui.press("volumeup")  
            elif 'volume down' in self.query:
                pyautogui.press("volumedown")
            elif 'mute' in self.query:
                pyautogui.press("volumemute") 
            elif 'activate how to do mode' in self.query:
                speak("activated! please tell me what you want to know?")
                from pywikihow import search_wikihow
                how = self.takeCommand()
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to)==1
                how_to[0].print()
                speak(how_to[0].summary) 
            else:
                speak("Sorry I didn't get that")

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./jarvisnew.ui"))
startfunctions = mainT()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton_3.clicked.connect(self.startFunc)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close) 
    def startFunc(self):
        self.jarvis_ui.movies_2 = QtGui.QMovie("Jarvis/3.gif") 
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()  

        self.jarvis_ui.movies_3 = QtGui.QMovie("Jarvis/5.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("Jarvis/7.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_5 = QtGui.QMovie("Jarvis/Code_Template.gif")
        self.jarvis_ui.label_6.setMovie(self.jarvis_ui.movies_5)
        self.jarvis_ui.movies_5.start()

        startfunctions.start()

Gui_App = QApplication(sys.argv)
Gui_jarvis = Main()
Gui_jarvis.show()
exit(Gui_App.exec_())
