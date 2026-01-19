import time  # For accessing system time and pausing
import os  # For clearing the console screen


def get_current_time():  # Retrieves the current local system time
    return time.localtime()  # Returns a struct with hour, minute, second


def clear_screen():  # Clears the terminal/console screen
    os.system("cls" if os.name == "nt" else "clear")


def display_time(current_time):  # Formats and prints the current time as HH:MM:SS
    print(
        f"{current_time.tm_hour:02}:{current_time.tm_min:02}:{current_time.tm_sec:02}"
    )


# Main program
print("=== 24-Hour Live Digital Clock ===")
print("Press Ctrl+C to stop\n")

try:
    while True:
        clear_screen()  # Clear previous clock display
        now = get_current_time()  # Get current system time
        display_time(now)  # Display formatted time
        time.sleep(1)  # Wait for 1 second before updating

except KeyboardInterrupt:
    print("\nClock stopped. Goodbye!")
