import sys
import time
import pyperclip

class ClipboardHistory:
    def __init__(self, max_length=10):
        self.history = []
        self.max_length = max_length
        self.current_clipboard = ""

    def update_history(self):
        clipboard_content = pyperclip.paste()
        if clipboard_content != self.current_clipboard:
            self.current_clipboard = clipboard_content
            self.history.append(clipboard_content)
            if len(self.history) > self.max_length:
                self.history.pop(0)

    def get_history(self, count=None):
        count = count or self.max_length
        return self.history[-count:]

def main():
    history = ClipboardHistory()
    print("Monitoring clipboard... Press Ctrl+C to stop and show history.")

    try:
        while True:
            history.update_history()
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass

    if len(sys.argv) > 1:
        count = int(sys.argv[1])
    else:
        count = int(input("How many recent clipboard items do you want to retrieve? "))

    items = history.get_history(count)
    for idx, item in enumerate(items, 1):
        print(f"{idx}: {item}")

if __name__ == "__main__":
    main()
