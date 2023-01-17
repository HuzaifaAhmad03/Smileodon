#importing the required modules
from speech_recognition import *
import pyttsx3
from datetime import *
from time import *
import random
import webbrowser
from tkinter import *

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")




#initialise the engine(speaker)
engine=pyttsx3.init()

t=""
text=""
list_greetings=["hi","hey","hello","hello,Hope youre having a nice day","hello"]


#smilodon function
def smileodon():
    
    
    global text

    #function for speech to text
    def speechtotxt():
        global text
        r=Recognizer()
        with Microphone() as source:
            print("Say Something: ")
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
            except:
                print("Sorry Could not hear. Please Say again.")
                #engine.say("Sorry Could not hear Please Say again")
            #engine.runAndWait()

    
    
    engine.say("Hello")
    engine.runAndWait()

    while text!="exit":
        speechtotxt()

        if text=="exit":
            continue
        elif text in list_greetings:
            x=random.choice(list_greetings)
            print(x)
            engine.say(x)
            engine.runAndWait()

        elif text=="how are you":
            print("I am fine Thank you")
            engine.say("I am fine Thank you")
            engine.runAndWait()

        elif text=="what are you":
            print("I am Smileodon, you can also call me Smilo")
            engine.say("I am smile o don , you can also call me smilo")
            engine.runAndWait()

        elif text=="what's the date" or text=="what is the date" or text=="date":
            x=date.today()
            text="Today is "+str(x)
            print(text)
            engine.say(text)
            engine.runAndWait()
        
        elif text=="time" or text=="what is the time" or text=="what's the time":
            x=ctime(time())
            text="Time is "+str(x)
            print(text)
            engine.say(text)
            engine.runAndWait()

        elif text[0:6]=="Search" or text[0:6]=="search":
            #taking keyword to search
            key=text[7::]
            #search url
            l=[]
            for j in search(key, tld="co.in", num=10, stop=10, pause=2):
                l.append(j)
            if key=="google" or key=="Google":
                url="https://www.google.com/"
            else:
                url=l[0]
            #OPEN IN CHROME
            webbrowser.open_new(url)
            text=""
            continue


        else:
            pass
    else:
        print("Good Bye")
        engine.say("Thank you, Good-Bye")
        engine.runAndWait()






def smilo_app():
    global t
    r=Recognizer()
    while t!="exit":
        with Microphone() as source:
            try:
                audio=r.listen(source)
                t=r.recognize_google(audio)
                print(t)
                if t=="hello smilodon" or t=="smilo" or t=="smilodon" or t=="Milo" or t=="hello":
                    smileodon()
                    #reupdation of text to not as"exit"
                    text=""
            except:
                print("Could not hear")
    w.destroy()


#tkinter window
w=Tk()
w.title('Smileodon')
w.geometry('220x220')
w.configure(bg='gray7')
b2=Button(w,height=7,width=15,text='SMILEODON',bg='#F28C28',command=smilo_app,activebackground='crimson',activeforeground='#F28C28')
b2.place(x=50,y=50)
w.mainloop()

