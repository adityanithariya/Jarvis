import pyttsx3 #pyttsx3 is used to convert string to speech.


engine = pyttsx3.init('sapi5') #If you will get key error:'sapi5' then install pypiwin32.
voices= engine.getProperty('voices') #getting details of current voice.
engine.setProperty('voice', voice[0].id) #It will set the property of creating voice to the zeroth element present in voice list.
#In pyttsx3 you will get two voices one of male(named as David) and one of female(named as Zira) you can check it out using print(voices). Use according to your need.

def speak(text):
    '''This function takes string and convert it into speech.'''

    engine.say(text)
    engine.runAndWait() #Without this command speech is not audible to us.
    # Let's run it.
if __name__ == "__main__":
    speak("You did it")
