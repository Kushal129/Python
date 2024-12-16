import time
import pyttsx3
import speech_recognition as sr
from datetime import datetime, timedelta
import re

# Initialize text-to-speech
def speak(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust voice speed
    engine.say(message)
    engine.runAndWait()

# Recognize user speech input
def listen_for_input(prompt):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening for {prompt}...")
        speak(f"Listening for {prompt}...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input.lower() 
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Please try again.")
            return listen_for_input(prompt)
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service. Please try again later.")
            return None

# Task Manager Class
class ToDoTaskReminder:
    def __init__(self):
        self.tasks = []  # List to store tasks

    # Add a new task
    def add_task(self, task_name, reminder_time):
        try:
            # If reminder time is in the form "after X minutes", calculate the correct time
            if "after" in reminder_time and ("minute" in reminder_time or "hour" in reminder_time):
                number = int(re.search(r'\d+', reminder_time).group())
                current_time = datetime.now()
                if "minute" in reminder_time:
                    reminder_time = current_time + timedelta(minutes=number)
                elif "hour" in reminder_time:
                    reminder_time = current_time + timedelta(hours=number)
                else:
                    reminder_time = current_time
                print(f"Reminder set for {reminder_time}.")
                speak(f"Reminder set for {reminder_time}.")
            else:
                # For absolute time input (YYYY-MM-DD HH:MM format)
                reminder_time = datetime.strptime(reminder_time, "%Y-%m-%d %H:%M")
                print(f"Task '{task_name}' added for {reminder_time}.")
                speak(f"Task '{task_name}' added for {reminder_time}.")

            # Store the task
            self.tasks.append({"task": task_name, "time": reminder_time})
        except ValueError:
            print("Invalid date/time format. Please use 'YYYY-MM-DD HH:MM' or 'after X minutes'.")
            speak("Invalid date or time format. Please use the correct format.")

    # Check and notify for due tasks
    def check_reminders(self):
        while True:
            current_time = datetime.now()
            for task in self.tasks:
                if current_time >= task["time"]:
                    print(f"Reminder: {task['task']} is due now!")
                    speak(f"Reminder! {task['task']} is due now!")
                    self.tasks.remove(task)
            time.sleep(60)  # Check every 60 seconds

    # Display all tasks
    def show_tasks(self):
        if not self.tasks:
            print("No tasks available!")
            speak("You have no tasks at the moment.")
        else:
            print("Here are your tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. Task: {task['task']} | Time: {task['time']}")
            speak("Here are your tasks.")

# Main Function
def main():
    to_do = ToDoTaskReminder()
    print("Welcome to the To-Do Task Reminder App!")
    speak("Welcome to the To-Do Task Reminder App!")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Start Reminders")
        print("4. Exit")
        print("You can also say 'bye' to exit the app.")
        
        # Get user choice through voice input
        choice = listen_for_input("your choice (1 2 3 4 or say 'bye' to exit)")

        if "1" in choice or "add task" in choice:
            task_name = listen_for_input("the task name")
            if task_name is None:
                continue

            # Get reminder time via voice input
            reminder_time = listen_for_input("the reminder time ")
            if reminder_time is None:
                continue

            # Add the task with the provided information
            to_do.add_task(task_name, reminder_time)

        elif "2" in choice or "show tasks" in choice:
            to_do.show_tasks()
        elif "3" in choice or "start reminders" in choice:
            print("Starting the reminder system...")
            speak("Starting the reminder system. I will notify you when tasks are due.")
            to_do.check_reminders()
        elif "4" in choice or "exit" in choice:
            print("Goodbye!")
            speak("Goodbye! Have a productive day!")
            break
        elif "bye" in choice:
            print("Goodbye!")
            speak("Goodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
            speak("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
