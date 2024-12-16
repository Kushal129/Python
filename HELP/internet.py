import requests
import pyttsx3
import time
import random
import webbrowser

def speak(message):
    """
    Converts the given text message into speech.
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust the speed of the voice
    engine.say(message)
    engine.runAndWait()

def check_internet():
    retry_count = 0 
    
    while True:
        try:
            print("Checking internet connectivity...")
            response = requests.get("https://smartlearningwithkhp.netlify.app/", timeout=5)
            
            if response.status_code == 200:
                message = "Internet is working!"
                speak(message)
                print(f"{message} Redirecting you to Smart...")
                webbrowser.open("https://smartlearningwithkhp.netlify.app/")
                break 
        except (requests.ConnectionError, requests.Timeout):
            retry_count += 1
            print(f"[Attempt {retry_count}] Internet is not working. Retrying...")
            
            if retry_count % 3 == 0:
                # Speak a custom message every 3 retries
                speak("Still trying to connect to the internet. Please wait.")
            
            # Add a dynamic delay before retrying (between 3 to 7 seconds)
            time.sleep(random.randint(3, 7))

check_internet()
