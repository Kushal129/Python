import psutil
import pyttsx3
import time

def speak(message):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(message)
    engine.runAndWait()

def monitor_resources(cpu_threshold=80, memory_threshold=80, disk_threshold=90, continuous=True, check_count=5):

    check = 0  
    warnings = 0
    last_stats = {}

    while continuous or check < check_count:
        # Get resource usage stats
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent

        # Display system stats
        print(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}% | Disk Usage: {disk_usage}%")

        # Store the last stats for speaking later
        last_stats = {  
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "disk_usage": disk_usage,
        }

        # Check for threshold breaches
        if cpu_usage > cpu_threshold:
            alert_message = f"Warning! CPU usage is at {cpu_usage}%!"
            print(alert_message)
            speak(alert_message)
            warnings += 1

        if memory_usage > memory_threshold:
            alert_message = f"Warning! Memory usage is at {memory_usage}%!"
            print(alert_message)
            speak(alert_message)
            warnings += 1

        if disk_usage > disk_threshold:
            alert_message = f"Warning! Disk usage is at {disk_usage}%!"
            print(alert_message)
            speak(alert_message)
            warnings += 1

        # Increment the check counter if not in continuous mode
        if not continuous:
            check += 1

        # Wait for 5 seconds before the next check
        time.sleep(5)

    # Speak and display the final stats
    final_message = (
        f"Final Check: CPU Usage is {last_stats['cpu_usage']}%, "
        f"Memory Usage is {last_stats['memory_usage']}%, "
        f"and Disk Usage is {last_stats['disk_usage']}%."
    )
    print("Monitoring complete!")
    print(final_message)
    speak(final_message)

    # Evaluate system performance based on warnings
    if warnings == 0:
        performance_message = "System performance is good. No issues detected."
    elif warnings < 3:
        performance_message = "System performance is acceptable, but some warnings were detected."
    else:
        performance_message = "System performance is critical. Please check your resources."

    print(performance_message)
    speak(performance_message)

def main():

    print("Welcome to System Resource Monitor!")
    speak("Welcome to System Resource Monitor!")

    # Ask the user if they want continuous or limited checks
    choice = input("Do you want to continuously monitor resources? (yes/no): ").strip().lower()

    if choice == "yes":
        continuous = True
        check_count = 0  # Not needed for continuous mode
    else:
        continuous = False
        check_count = int(input("Enter the number of checks to perform (e.g., 5): ").strip())

    print("\nStarting monitoring...\n")
    speak("Starting monitoring now!")

    # Start monitoring
    monitor_resources(
        cpu_threshold=80,  # Fixed thresholds
        memory_threshold=80,
        disk_threshold=90,
        continuous=continuous,
        check_count=check_count
    )

if __name__ == "__main__":
    main()
