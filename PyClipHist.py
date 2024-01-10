# JDD 12/2023
# Clipboard History

import sys, time, pyperclip

class ClipboardHistory:
    # class of functions for clipboard history
    def __init__(self, max_length=10):
        # function to default to max of 10
        self.history = []
        self.max_length = max_length
        self.current_clipboard = ""

    def update_history(self):
        # function to update histories
        clipboard_content = pyperclip.paste()
        if clipboard_content != self.current_clipboard:
            self.current_clipboard = clipboard_content
            self.history.append(clipboard_content)
            if len(self.history) > self.max_length:
                self.history.pop(0)

    def get_history(self, count=None):
        # function to extract
        count = count or self.max_length
        return self.history[-count:]

def format_time(seconds):
    # function to formate time
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

def main():
    print("\nWelcome to the PyClipboard History!")

    history = ClipboardHistory()
    print('\x1b[11;30;42m' + "Monitoring clipboard... Press Ctrl+C to stop and show history." + '\x1b[0m')

    start_time = time.time()
    # keep track of time of program
    try:
        while True:
            history.update_history()
            elapsed_time = time.time() - start_time
            print(f"Running for {format_time(elapsed_time)}", end="\r")
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    if len(sys.argv) > 1:
        # store command line arugment that is provided
        count = int(sys.argv[1])
    else:
        # prompt the user to input a history amount
        count = int(input("\nHow many recent clipboard items do you want to retrieve? \n"))

    items = history.get_history(count)
    for idx, item in enumerate(items, 1):
        print(f"{idx}: {item}")

# main

if __name__ == "__main__":
    main()

# end
