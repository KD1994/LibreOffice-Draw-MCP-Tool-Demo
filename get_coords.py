import pyautogui
import time


if __name__ == "__main__":
    print("Move your mouse to the rectangle tool... (Ctrl+C to stop)")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"X: {x} Y: {y}"
            print(position_str, end="\r", flush=True)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nDone.")
