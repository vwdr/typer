from pynput.keyboard import Key, Controller
from playsound import playsound
import pyautogui
import time
import tkinter as tk
import threading

quitVariable = False  # Changed to a boolean value

def quit_program():
    global quitVariable
    quitVariable = True  # Set the global variable to True
    root.destroy()

def write_text():
    charCount = 0
    keyboard = Controller()

    with open("text.txt", "r") as f:
        data = f.read()

    print("Starting in 5 seconds...")
    time.sleep(5)

    for char in data:
        if quitVariable:  # Check the global variable
            break  # Exit the loop if the quit variable is True
        keyboard.press(char)
        keyboard.release(char) 
        time.sleep(0.12)
        charCount += 1
        if charCount % 500 == 0:
            pyautogui.moveTo(30, 139)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(325, 583)
            pyautogui.click()
            time.sleep(1)
            playsound('ping.mp3')
            time.sleep(10)



def check_input():
    # Check for new keyboard input or perform other tasks here
    root.after(100, check_input)  # Check every 100 milliseconds

root = tk.Tk()
root.title("Main Program")

quit_button = tk.Button(root, text="Quit", command=quit_program)
quit_button.pack()

# Start the writing script in a separate thread
writing_thread = threading.Thread(target=write_text)
writing_thread.start()

# Start checking for input in the Tkinter main loop
root.mainloop()