import os
import pyttsx3

while True:
    print("CHat with me with your requirement: ", end="")
    p = input().lower()

    if ("open" in p) or ("start" in p) or ("run" in p) or ("launch" in p):
        if ("do not" in p) or ("donot" in p) or ("don't" in p) or ("does not" in p) or ("doesn't" in p) or ("close" in p) or ("can not" in p) or ("can't" in p) or ("could not" in p) or ("couldn't" in p):
            print("Please give another requirement")
        elif ("chrome" in p) or ("google chrome" in p) or ("google" in p) or ("browser" in p):
            pyttsx3.speak("Google chrome is launching")
            os.system("start chrome")
        elif ("firefox" in p) or ("mozilla" in p):
            pyttsx3.speak(" firefox is launching")
            os.system("start firefox")
        elif ("vlc" in p) or ("media" in p) or ("player" in p) or ("multimedia" in p) or ("video player" in p) or ("audio player" in p):
            os.system("start VLC")
            pyttsx3.speak(" vlc is launching")
        elif ("window media player" in p) or ("windowmediaplayer" in p):
            pyttsx3.speak(" Window media player is launching")
            os.system("start wmplayer")
        elif ("calulator" in p):
            pyttsx3.speak("calculator is launching")
            os.system("start calc")
        elif ("python" in p):
            pyttsx3.speak("python is launching")
            os.system("python")
        elif ("notepad" in p) or ("textpad" in p) or ("editor" in p):
            pyttsx3.speak(" notepad is launching")
            os.system("start notepad")
        elif ("file explorer" in p) or ("this pc" in p) or ("My computer" in p):
            pyttsx3.speak("file explorer is launching")
            os.system("start explorer")
        elif ("cmd" in p) or ("command prompt" in p):
            pyttsx3.speak("command prompt is launching")
            os.system("start cmd")
        elif ("control pannel" in p):
            pyttsx3.speak("control pannel is launching")
            os.system("start control")
        elif ("paint" in p) or ("mspaint" in p) or ("microsoft paint" in p):
            pyttsx3.speak("paint is launching")
            os.system("start mspaint")
        elif ("time zone setting") or (("setting" in p) and (("date" in p) or ("time" in p))):
            pyttsx3.speak("time zone setting is opening")
            os.system("control timedate.cpl")
        elif ("date" in p):
            pyttsx3.speak("current date is showing")
            os.system("date/T")
        elif ("time" in p):
            pyttsx3.speak("current time is showing")
            os.system("time/t")
        elif ("admin tools" in p) or ("administrative tools" in p):
            pyttsx3.speak("administrative tools is opening")
            os.system("control admintools")
        elif ("device manager" in p):
            pyttsx3.speak("device manager is opening")
            os.system("control hwwiz.cpl")
        elif ("desktop setting"):
            pyttsx3.speak("desktop setting is lopening")
            os.system("control desktop")
        elif ("keyboard setting") or ("keyboard property") or ("keyboard properties"):
            pyttsx3.speak("keyboard properties is opening")
            os.system("control keyboard")
        elif ("mouse setting") or ("mouse property") or ("mouse properties"):
            pyttsx3.speak("mouse properties is opening")
            os.system("control mouse")
        elif ("network" in p) or ("network connection" in p) or ("network setting" in p):
            pyttsx3.speak("network connection setting is showing")
            os.system("control ncpa.cpl")
        elif ("power option" in p) or ("power setting"):
            pyttsx3.speak("power option setting is opening")
            os.system("control powercfg.cpl")
        elif ("system property" in p) or ("system properties" in p):
            pyttsx3.speak("system properties is showing")
            os.system("control sysdm.cpl")
        elif("chararcter map" in p):
            pyttsx3.speak("character map is showing")
            os.system("charmap")
    elif ("quit" in p):
        pyttsx3.speak("HumanChat Bot is closing thank you   have a nice day!")
        break
