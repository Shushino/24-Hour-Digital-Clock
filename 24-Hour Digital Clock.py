import time
import os

print("=== 24-Hour Live Digital Clock ===")
print("Press Ctrl+C to stop\n")

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        now = time.localtime()
        print(f"{now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02}")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nClock stopped. Goodbye!")
