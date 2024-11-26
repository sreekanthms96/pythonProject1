import pyautogui
import random
import time

def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()  # Get screen dimensions
    while True:
        # Generate random coordinates
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        
        # Move the mouse to the random coordinates
        pyautogui.moveTo(x, y, duration=0.5)  # Smooth movement
        print(f"Mouse moved to: ({x}, {y})")
        
        # Wait for 2 minutes
        time.sleep(120)

if __name__ == "__main__":
    move_mouse_randomly()
