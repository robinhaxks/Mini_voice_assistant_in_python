import pyttsx3  
import datetime
import speech_recognition as sr  
import webbrowser
import wikipedia  
import random
import math
import smtplib  
import pywhatkit as pwt  
import json
import requests
import os
import time

def intro():

     speak("hey buddy i am your jarvis, new voice assistent ,how can i help you")

def speak(audio):
      engine = pyttsx3.init()
      rate=engine.getProperty('rate')
      engine.setProperty('rate',rate-50)
      engine.say(audio)     
      engine.runAndWait()

def wishes():  
   hour = int(datetime.datetime.now().hour)
   if hour >=0 and hour<12:
       speak("happy morning")
       speak("have an nice day ")
   elif hour >=12 and hour < 16 :
      speak("good afternoon")
   elif hour  >=16 and  hour < 20:
      speak("good evening")   
   else:
      speak("good night have an sweet dreams")   
    
def listenthecommand():

    r = sr.Recognizer()

    mic = sr.Microphone()
    with mic as source:
            print("Listening...")
            audio = r.record(source,duration=5)
            print("Recognize...")

    try:
                text = r.recognize_google(audio)
                print("your text:\n")
                print(f"user said: {text}")
                
            
    except sr.UnknownValueError:
                           
                 print("Don not hear anything")   
                 text =  listenthecommand()        
                         
    return text
            
def game():
           speak("hey , this is an number guessing game ")
           print("Hey , This is an number guessing game ")
           lower  = 0
           upper = 250
           x= random.randint(lower,upper)
           print("\n\tYou've only 8 chances to guess the number i think!\n")
           speak("You've only 8 chances to guess the number!")
           speak ("The integer is between 0 to 250")
           count = 1  
           speak("Guess a number")
           r = sr.Recognizer()
           mic = sr.Microphone()
           while count <=8:
                 count += 1
                 with mic as source:
                    print("tell the number....")
                    audio = r.record(source,duration=5)
                    print("comparing....")

                    try:
                        gues = r.recognize_google(audio)
                        print(f"Your guessing number {gues}")
                        speak(f"Your guessing number {gues}")
                        guess = int(gues)
                        if x == guess:
                                    print("Congratulations you did it in ",count, " try")
                        elif x > guess:
	                            print("ohh sorry your guess is too small")
	                            speak("your guess is too small")
                        elif x < guess:
	                            print("ohh sorry you guess id too high")
	                            speak("you guess id too high")               
            
                    except sr.UnknownValueError:
                        print("Didnt hear that try again")
          
           if count >= 8:
	            print("\nThe number is %d" % x)
	            speak("The number is %d" % x)
	            print("\nsorry better luck next time")
	            speak("thanks for playing with me")
              	  
def message():
     now = datetime.datetime.now()
     h = now.hour
     s1 = now.minute
     mi = s1+2
     speak("please type the number you want to send")
     nu = input("Enter the  number with country code: ")
     speak("tell the message you want to send  it")
     message = 	listenthecommand()
     pwt.sendwhatmsg(nu,message,h,mi) 
     
     
     
def  weather():    
        api_key = "41c177fb938536e752e44625b4b70425"  
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        print("Tell the city name ..........")
        speak("tell the city name you want to get an weather report")
        city_name = listenthecommand()
        print("The city name is :  ")
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                fahrenheit =  current_temperature * 9/5 - 459.67
                celsius = current_temperature- 273.15
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
	         "\n Temputer in fahrenheit = "+ 
	                                str(fahrenheit) +
	          "\n Temperature in celsius = "+
	                                str(celsius)+                      
		"\n humidity (in percentage) = " +
					str(current_humidity) +
		"\n description = " +
					str(weather_description))

        else :
           print("City not found")
           speak("unable to find a city name")

        

                 		              
	
if __name__=="__main__":
         
       wishes()
        
       intro()
         
       while True :
             
              text = listenthecommand().lower() #to get all letters in small
              
              if "youtube" in text:
                   speak("youtube opening")
                   webbrowser.open("youtube.com")
                   
              elif "facebook" in text:  
                   speak("facebook opening")
                   webbrowser.open("facebook.com")
                   
              elif "wikipedia" in text:
                   speak("Searching in wikipedia...")
                   wiki = text.replace("wikipedia","") # replace wikipedia to empty space in text 
                   result = wikipedia.summary(wiki,sentences=2)
                   print("According to wikipedia "+ wiki +" is")
                   speak("According to wikipedia "+ wiki +" is")
                   print(result)
                   speak(result)
                   
              elif "google" in text :
                   
                   speak("google opening")
                   webbrowser.open("google.com")
                   
              elif "github" in text :
                   speak("github opende")
                   webbrowser.open("github.com")
              
              elif "browser" in text:
                   speak("please tell the website you want to visit")
                   web = input("Entee the website you want to visit")
                   webbrowser.open(web)         
                   
              elif "who" and "you" in text :
                  speak ("i am your new voice assistent")
                  
              elif "game"  in text :
                        game()
                        
              elif "time"  in text :
                      strs = datetime.datetime.now().strftime("%H:%M:%S")
                      speak(f"sir ,the time is {strs}")
                      print(strs)
                      
              elif "mail"  in text :
                          mail = smtplib.SMTP('smtp.gmail.com', 587)
                          mail.ehlo()
                          mail.starttls()
                          mail.login('emai@gmail.com', 'password')
                          speak("hey , please type the email address of your friend")
                          eaddrs= input("Enter the mail id:  ")                     
                          speak("hey buddy, tell the message to send to your friend")
                          print("Listining your message.....")
                          cont = listenthecommand()
                          speak(cont)
                          mgs = ""        
                          try :
                              mail.sendmail(mgs,eaddrs,cont)
                              print("Mail sendted")
                              speak("mail sented sucesssfully")
                          except smtplib.SMTPRecipientsRefused:
                              print("plz check the mail address correct or not")
                              speak("hey buddy , please check the mail id it is vali or not ")    
                              
                          
                          
              elif  "whatsapp" in text :
                     
                          message()            
                          
              elif "climate"   in text :           
                             
                           weather()  
                          
                          
              elif  "close"  in text :
                          speak ("ok sir , i am leaveing right now ,bye ")
                          speak("have an great day  ")
                          exit()            
                          
                          
              elif "call" in text :
                     speak("use this website to make an call")
                     speak("globfone opend")                     
                     webbrowser.open("https://globfone.com/call-phone/")
               
              elif "text" in text :
                     speak("use this website to make an text message")
                     speak("globfone opend")                     
                     webbrowser.open("https://globfone.com/send-text/")
               
                          
              elif "thanks" in text :
                     speak("no mention its my duty , sir") 
                     
                     
              elif "play music" in text :
                     music_dir = 'location of folder to play music'
                     songs = os.listdir(music_dir)
                     for i in range(200): # 200 is no of song to play
                               os.startfile(os.path.join(music_dir,songs[i]))
                               time.sleep(300) #play next song after 5 mins or 300 seconds  

              
              
              else :
                      
                     speak("this function not programing for me , i will do later")            
                                         
