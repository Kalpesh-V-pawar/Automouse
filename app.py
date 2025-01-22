import pyautogui
import time
import os
import subprocess
import keyboard
import time


# Add a safety feature - move mouse to top-left corner to stop script
pyautogui.FAILSAFE = True

# This will store both mouse coordinates and keyboard actions
AUTOMATION_SEQUENCE = [
    # Example sequence (you'll replace this with your recorded sequence):


    {'type': 'click', 'name': 'search', 'x': 71, 'y': 108},
    {'type': 'click', 'name': 'search', 'x': 1840, 'y': 109},
    {'type': 'click', 'name': 'search', 'x': 1840, 'y': 109},    
    {'type': 'click', 'name': 'search', 'x': 380, 'y': 146},    
    {'type': 'click', 'name': 'search', 'x': 1249, 'y': 223},
    {'type': 'click', 'name': 'search', 'x': 621, 'y': 356},
    {'type': 'click', 'name': 'search', 'x': 1150, 'y': 485},
    {'type': 'click', 'name': 'search', 'x': 1767, 'y': 187},
    {'type': 'click', 'name': 'search', 'x': 961, 'y': 276},
    {'type': 'click', 'name': 'search', 'x': 1505, 'y': 399},
    {'type': 'click', 'name': 'search', 'x': 1634, 'y': 458},
    {'type': 'click', 'name': 'search', 'x': 1531, 'y': 470},
    {'type': 'click', 'name': 'search', 'x': 434, 'y': 162},
    {'type': 'click', 'name': 'search', 'x': 794, 'y': 499},
    {'type': 'click', 'name': 'search', 'x': 1493, 'y': 992},
    {'type': 'click', 'name': 'search', 'x': 24, 'y': 105},


]

def click_at_position(x, y, delay=1):
    """Move to specified coordinates and click"""
    print(f"Clicking at position x={x}, y={y}")
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(delay)
    pyautogui.click()

def get_current_position():
    """Get current mouse position"""
    x, y = pyautogui.position()
    return x, y

def record_sequence():
    """Record a sequence of mouse clicks and keyboard actions"""
    print("\nRECORD AUTOMATION SEQUENCE")
    print("=========================")
    
    sequence = []
    while True:
        print("\nWhat would you like to record?")
        print("1. Mouse Click")
        print("2. Type Text")
        print("3. Press Special Key (enter, tab, etc.)")
        print("4. Add Delay")
        print("5. Press Hotkey Combination")  # New option
        print("6. Finish Recording")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            # Record mouse click
            name = input("Enter a name for this position (e.g., 'search_button'): ")
            print(f"\nMove your mouse to the {name} position...")
            print("You have 5 seconds...")
            time.sleep(5)
            x, y = get_current_position()
            sequence.append({
                'type': 'click',
                'name': name,
                'x': x,
                'y': y
            })
            print(f"Recorded click at {name}: x={x}, y={y}")

        elif choice == '2':
            # Record text input
            text = input("Enter the text you want to type: ")
            sequence.append({
                'type': 'type',
                'text': text
            })
            print(f"Recorded: Type '{text}'")

        elif choice == '3':
            # Record special key press
            print("\nCommon special keys: enter, tab, space, backspace, delete, up, down, left, right")
            key = input("Enter the key name: ")
            sequence.append({
                'type': 'key',
                'key': key
            })
            print(f"Recorded: Press '{key}' key")

        elif choice == '4':
            # Record delay
            seconds = float(input("Enter delay in seconds: "))
            sequence.append({
                'type': 'delay',
                'seconds': seconds
            })
            print(f"Recorded: Wait {seconds} seconds")

        elif choice == '5':
            # Record hotkey combination
            print("\nEnter keys separated by commas (e.g., ctrl,t or ctrl,shift,n)")
            keys = input("Enter key combination: ").split(',')
            sequence.append({
                'type': 'hotkey',
                'keys': keys
            })
            print(f"Recorded: Hotkey combination {'+'.join(keys)}")   

        elif choice == '6':
            break

    print("\nHere's your recorded sequence (copy this to the AUTOMATION_SEQUENCE at the top of the script):")
    print("\nAUTOMATION_SEQUENCE = [")
    for action in sequence:
        if action['type'] == 'click':
            print(f"    {{'type': 'click', 'name': '{action['name']}', 'x': {action['x']}, 'y': {action['y']}}},")
        elif action['type'] == 'type':
            print(f"    {{'type': 'type', 'text': '{action['text']}'}},")
        elif action['type'] == 'key':
            print(f"    {{'type': 'key', 'key': '{action['key']}'}},")
        elif action['type'] == 'delay':
            print(f"    {{'type': 'delay', 'seconds': {action['seconds']}}},")
           
    print("]")

def run_automation():
    """Run the recorded automation sequence"""
    print("Starting automation in 5 seconds...")
    print("Switch to your target window now!")
    time.sleep(5)
    
    for action in AUTOMATION_SEQUENCE:
        if action['type'] == 'click':
            click_at_position(action['x'], action['y'])
        elif action['type'] == 'type':
            pyautogui.write(action['text'])
            time.sleep(0.5)
        elif action['type'] == 'key':
            pyautogui.press(action['key'])
            time.sleep(0.5)
        elif action['type'] == 'delay':
            time.sleep(action['seconds'])
        elif action['type'] == 'hotkey':
            pyautogui.hotkey(*action['keys'])
            time.sleep(0.5)

def kill_python_processes():
    """Kill all python.exe and pythonw.exe processes"""
    print("Terminating all Python processes...")
    os.system("taskkill /F /IM python.exe")  # Kill all python.exe processes
    os.system("taskkill /F /IM pythonw.exe")  # Kill all pythonw.exe processes
    print("All Python processes have been terminated.")

def listen_for_termination():
    """Listen for Ctrl+Tab key press to terminate the script"""
    while True:
        if keyboard.is_pressed('ctrl+tab'):
            kill_python_processes()
            sys.exit(0)  # Exit the script
        time.sleep(0.1)  # Small delay to prevent high CPU usage

if __name__ == "__main__":
    # Start listening for the Ctrl+Tab key press in a separate thread
    import threading
    termination_thread = threading.Thread(target=listen_for_termination)
    termination_thread.daemon = True
    termination_thread.start()

    while True:
            run_automation()

