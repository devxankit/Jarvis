import pyttsx3
import datetime
import sys
import os
import wikipedia
import pyjokes
import serial
import speech_recognition as sr
from googletrans import Translator
import openai
import PyQt5.QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

import requests
import bs4
import pyautogui
import pywhatkit
import webbrowser

from plyer import notification  
import requests 
from bs4 import BeautifulSoup  


from jarvis_mark5_GUI import Ui_JarvisOverlayGUI

# Set your OpenAI API key
openai.api_key = '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'

# conversation = [
#     {"role": "system", "content": "Your name is Jarvis and your purpose is to be Ankit's AI assistant"},
# ]


dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome",
           "vscode": "code", "powerpoint": "powerpnt"}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    if startExecution.muteState == 'yes':
        pass
    else:
        ui.updateGIFsDynamically('speaking')
        engine.say(audio)
        engine.runAndWait()


class jarvisMainClass(QThread):
    def __init__(self):
        super(jarvisMainClass, self).__init__()
        self.muteState = None

    def run(self):
        self.runJarvis()

    def ToggleMute(self, state):
        if state:
            self.muteState = 'yes'
            ui.terminalPrint('Muted')
            ui.updateGIFsDynamically('sleeping')
            speak('Muted Sir')
        else: #un-mute 
            self.muteState = 'no'
            ui.updateGIFsDynamically('speaking')
            ui.terminalPrint('Active and Online sir')
            speak('Active and Online Sir')
            ui.updateGIFsDynamically('listening')
            
    
    def checkMuteStatus(self):
        checkMute = ui.jarvisUI.muteCB.checkState()
        if checkMute == 0:
            return False
        else:
            return True
        

    def commands(self):
        ui.terminalPrint("Listening...")
        ui.updateGIFsDynamically('listening')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            checkMuteState = self.checkMuteStatus()
            if checkMuteState:
                cmd = 'none'
                ui.updateGIFsDynamically('sleeping')
                pass
            else:
                try:
                    ui.updateGIFsDynamically('loading')
                    cmd = r.recognize_google(audio, language='en-in')
                    ui.terminalPrint(f"You just said: {cmd}\n")
                except:
                    ui.terminalPrint("please tell me again")
                    speak("please tell me again")
                    cmd = 'none'
        return cmd


    def googleSearch(self, gquery):
        gquery = gquery.replace("search", "")      
        gquery = gquery.replace("google", "")      
        gquery = gquery.replace("find", "")      
        gquery = gquery.replace("wikipedia", "")      
        gquery = gquery.replace("about", "")      
        gquery = gquery.replace("tell", "")      
        gquery = gquery.replace("me", "")      

        URL = "https://www.google.co.in/search?q=" + gquery

        headers = {
                 
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }

        page = requests.get(URL, headers=headers)
        soup = bs4.BeautifulSoup(page.content,'html.parser' )
        try:
            res = soup.find(class_ = 'Z0LcW t2b5Cf CfV8xf').get_text()
            ui.terminalPrint(res)
            speak("According to Google, " + res)
        except Exception:
            speak("No Results found Sir...")
            ui.terminalPrint("No Results Found")  


    def searchYoutube(self, yquery):
        speak("This is what I found for your search!")
        yquery = yquery.replace("youtube search","")
        yquery = yquery.replace("youtube","")
        yquery = yquery.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + yquery
        webbrowser.open(web)
        pywhatkit.playonyt(yquery)
        speak("Done, Sir")

 

    def convaiCHAT(self, cquery, sessionID):
        ui.terminalPrint("jarvis is Thinking...")
        AI_url = "https://api.convai.com/character/getResponse"
        payload = {
            'userText': f'q{cquery}',
            'charID': '736dc994-edba-11ee-9841-42010a7be00e',
            'sessionID': sessionID
        }
        headers = {
              'CONVAI-API-KEY': 'e76f1c1bba9fe966ba5ee29630b6d681'
              
          }
        response = requests.request("post", AI_url, headers= headers, data= payload)
        data = response.json()
        character_res = data['text']
        sessionID = data['sessionID']


        ui.terminalPrint(character_res)
        speak(character_res)

        return sessionID



    def Translation(self, tquery):
        tquery = tquery.replace('translate', '')
        translator = Translator()
        try:
            textToTranslate = translator.translate(tquery, src='en', dest='hi')
            text = textToTranslate.text
            pro = textToTranslate.pronunciation
            ui.terminalPrint(pro + '=>' + text)
            speak(pro)
        
        except Exception as e:
            ui.terminalPrint('Unable to Translate')
            ui.terminalPrint(e)
            speak('Unable to Translate')



    def chatgpt(self, wquery):
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo", 
                prompt=wquery,
                max_tokens=100
            )
            answer = response.choices[0].text.strip()
            ui.terminalPrint(f"ChatGPT: {answer}")
            speak(answer)
        except Exception as e:
            ui.terminalPrint('Error while accessing ChatGPT')
            ui.terminalPrint(str(e))
            speak('Error while accessing ChatGPT')


    def iplScore(self, iquery):
         url = "https://www.cricbuzz.com/"
         page = requests.get(url)
         soup = BeautifulSoup(page.text, "html.parser")
         team1 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
         team2 = soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
         team1_score = soup.find_all(class_="cb-ovr-flo")[8].get_text()
         team2_score = soup.find_all(class_="cb-ovr-flo")[10].get_text()

         a = print(f"{team1} : {team1_score}")
         b = print(f"{team2} : {team2_score}")

         notification.notify(
             title="IPL SCORE :- ",
             message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
             timeout=15
         )

   

    def openappweb(self, oquery):
     speak("Launching, sir")
     ui.terminalPrint("Launching, sir")
     if ".com" in oquery or ".co.in" in oquery or ".org" in oquery:
        oquery = oquery.replace("open", "")
        oquery = oquery.replace("jarvis", "")
        oquery = oquery.replace("launch", "")
        oquery = oquery.replace(" ", "")
        webbrowser.open(f"https://www.{oquery}")
     else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in oquery:
                os.system(f"start {dictapp[app]}")




    def runJarvis(self):
        sesID = '-1'
        while True:
            checkMute = self.checkMuteStatus()
            if not checkMute:
                self.query = self.commands().lower()
                if 'time' in self.query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    ui.terminalPrint(f"Sir, the time is {strTime}")
                    speak(f"Sir, the time is {strTime}")
                
                elif 'translate' in self.query:
                    self.Translation(self.query)

                elif 'search' in self.query or 'google' in self.query:
                    self.googleSearch(self.query)
                
                elif 'youtube' in self.query:
                    self.searchYoutube(self.query)

                elif 'chat gpt' in self.query:
                    self.chatgpt(self.query)


                elif "ipl score" in self.query:
                    self.iplScore(self.query)
                
                elif 'start' in self.query:
                    self.openappweb(self.query)

                else:
                    self.convaiCHAT(self.query, sesID)
                
            else:
                pass


startExecution = jarvisMainClass()

class Ui_Jarvis(QMainWindow):
    def __init__(self):
        super(Ui_Jarvis, self).__init__()
        self.oldPosition = PyQt5.QtCore.QPoint()
        self.jarvisUI = Ui_JarvisOverlayGUI()
        self.jarvisUI.setupUi(self)
        
        self.showStatusIcons = True
        self.jarvisUI.ShowIconCB.stateChanged.connect(self.showIconToggle)
        self.jarvisUI.showTerminalCB.stateChanged.connect(self.showTerminalToggle)
        self.jarvisUI.muteCB.stateChanged.connect(self.ToggleMuteBTN)
        self.jarvisUI.customSearchCB.stateChanged.connect(self.showsearchToggle)


        self.jarvisUI.jarvisMainButton.clicked.connect(lambda: self.changeWinSize('full'))
        self.jarvisUI.closeButton.clicked.connect(self.close)
        self.jarvisUI.minButton.clicked.connect(lambda: self.changeWinSize('min'))
        self.jarvisUI.sendButton.clicked.connect(lambda: self.manualCodeFromTerminal())  # Connect using lambda
        self.runAllGIFs() 


    

    def showsearchToggle(self, checked):
        if checked:
            self.showSearch = True
            self.jarvisUI.searchFram.show()
        else:
            self.showSearch = False
            self.jarvisUI.searchFram.hide()
            

    def ToggleMuteBTN(self, checked):
        if checked:
            jarvisMainClass.ToggleMute(self, True)
        else:
            jarvisMainClass.ToggleMute(self, False)

     
    def showTerminalToggle(self, checked):
        if checked:
            self.showTerminal = True
            self.changeWinSize('full')
        else:
            self.showTerminal = True
            self.resize(398,180)


    def showIconToggle(self, checked):
        if checked:
            self.showStatusIcons = True
        else:
            self.showStatusIcons = False


    def changeWinSize (self, type):
        if type == 'full':
            self.resize(402, 351)
        elif type == 'min':
            if not self.showStatusIcons:
               self.resize(151, 60)        # don't show any icon
            else:
              self.resize(148, 180)       # just show overlay and hide everything
 

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()
    

    def  mouseMoveEvent(self, event):
        d = PyQt5.QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + d.x(), self.y() + d.y())
        self.oldPosition = event.globalPos()


    def runAllGIFs(self):
        self.jarvisUI.listeningMovie = QtGui.QMovie(
            "E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_lis_mic.gif")
        self.jarvisUI.listeningLabel.setMovie(self.jarvisUI.listeningMovie)
        self.jarvisUI.listeningMovie.start()

        self.jarvisUI.speakingMovie = QtGui.QMovie(
            "E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_speaking.gif")
        self.jarvisUI.speakingLabel.setMovie(self.jarvisUI.speakingMovie)
        self.jarvisUI.speakingMovie.start()

        self.jarvisUI.loadingMovie = QtGui.QMovie(
            "E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_loading.gif")
        self.jarvisUI.loadingLabel.setMovie(self.jarvisUI.loadingMovie)
        self.jarvisUI.loadingMovie.start()

        self.jarvisUI.sleepingMovie = QtGui.QMovie(
            "E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_lis2.gif")
        self.jarvisUI.sleepingLabel.setMovie(self.jarvisUI.sleepingMovie)
        self.jarvisUI.sleepingMovie.start()

        startExecution.start()


    def terminalPrint(self, text):
        self.jarvisUI.terminalText.appendPlainText(text)


    def updateGIFsDynamically(self, state):
         if state == 'speaking':
             self.jarvisUI.speakingLabel.raise_()
             self.jarvisUI.speakingLabel.show()
             self.jarvisUI.listeningLabel.hide()
             self.jarvisUI.loadingLabel.hide()
             self.jarvisUI.sleepingLabel.hide()

         elif state == "listening":
             self.jarvisUI.listeningLabel.raise_()
             self.jarvisUI.listeningLabel.show()
             self.jarvisUI.speakingLabel.hide()
             self.jarvisUI.loadingLabel.hide()
             self.jarvisUI.sleepingLabel.hide()

         elif state == "loading":
             self.jarvisUI.loadingLabel.raise_()
             self.jarvisUI.loadingLabel.show()
             self.jarvisUI.speakingLabel.hide()
             self.jarvisUI.listeningLabel.hide()
             self.jarvisUI.sleepingLabel.hide()

         elif state == "sleeping":
             self.jarvisUI.sleepingLabel.raise_()
             self.jarvisUI.sleepingLabel.show()
             self.jarvisUI.speakingLabel.hide()
             self.jarvisUI.loadingLabel.hide()
   


    def manualCodeFromTerminal(self):
        if self.jarvisUI.searchTextInput.text():
            cmd = self.jarvisUI.searchTextInput.text()
            self.jarvisUI.searchTextInput.clear()
            self.jarvisUI.terminalText.appendPlainText(f"You typed->> {cmd}")

            if cmd == 'exit':
                 self.close() 
            if cmd == 'time':
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.terminalPrint(f"Sir, the time is {strTime}")
                speak(f"Sir, the time is {strTime}")

            elif "screenshot" in cmd:
                 speak("screenshot done sir")
                 im = pyautogui.screenshot()
                 im.save("ss.jpg")
                 ui.terminalPrint("screenshot done sir") 
                 pass 
            
            elif "click my photo" in cmd:
                 pyautogui.press("super")
                 pyautogui.typewrite("camera")
                 pyautogui.press("enter")
                 pyautogui.sleep(2)
                 speak("SMILE")
                 pyautogui.press("enter")
                 ui.terminalPrint("your photo is clicked sir")
                 speak("I took your photo sir")
                 pass
            


            # elif "GPT" "search on chat gpt" "chat gpt" in cmd:
            #      cmd.append({"role": "user", "content": cmd})
            #      response = openai.ChatCompletion.create(
            #      model="gpt-3.5-turbo",
            #      messages=cmd
            #      )

            #      message = response["choices"][0]["message"]["content"]
            #      cmd.append({"role": "assistant", "content": message})
            #      ui.terminalPrint(f"Assistant: {message}")

            #      speak(message)
            #      pass
            
           
            else:
                pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Jarvis()
    ui.resize(148,180)
    ui.show()
    sys.exit(app.exec_())
