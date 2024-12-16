import psutil
import pygame
import time
import os
import sys

play_count = 0


def play_sound(sound_file):
    global play_count
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    play_count += 1
    if play_count >= 3:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        sys.exit()


def check_battery():
    battery = psutil.sensors_battery()

    if "prev_charging_status" not in globals():
        globals()["prev_charging_status"] = battery.power_plugged

    if battery.power_plugged != globals()["prev_charging_status"]:
        if battery.power_plugged:
            print("Laptop is plugged into the charger.")
            automation_on_plug_in()
        else:
            print("Laptop is not plugged into the charger.")

        globals()["prev_charging_status"] = battery.power_plugged

    if battery.power_plugged and battery.percent == 100:
        print("Battery is fully charged!")
        sound_file = "C:\\Windows\\Media\\battery_charged_sound.mp3"

        if os.path.exists(sound_file):
            play_sound(sound_file)
            time.sleep(2)
            play_count = 0
        else:
            print(f"Sound file not found: {sound_file}")


def automation_on_plug_in():
    print("Charger plugged in. Running automation...")


while True:
    check_battery()
    time.sleep(2)
