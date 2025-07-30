import tkinter as tk
import pyautogui
from ahk import AHK

class App:
    def __init__(self, root):
        self.root = root
        root.title("KHM-Controle")

        # Language buttons
        lang_frame = tk.Frame(root)
        lang_frame.pack(pady=10)

        self.lang_buttons = []
        languages = ["DE", "EN", "FR", "ES"]
        for lang in languages:
            button = tk.Button(lang_frame, text=lang, command=lambda l=lang: self.select_language(l))
            button.pack(side=tk.LEFT, padx=5)
            self.lang_buttons.append(button)

        # Text area
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Accept button
        accept_button = tk.Button(root, text="Accept", command=self.accept_text)
        accept_button.pack(pady=5)

        # Camera trigger button
        camera_button = tk.Button(root, text="Trigger Camera", command=self.trigger_camera)
        camera_button.pack(pady=5)

    def select_language(self, lang):
        print(f"Language selected: {lang}")
        # Define keyboard shortcuts for language selection
        if lang == "DE":
            pyautogui.hotkey('num1')
        elif lang == "EN":
            pyautogui.hotkey('num2')
        elif lang == "FR":
            pyautogui.hotkey('num3')
        elif lang == "ES":
            pyautogui.hotkey('num4')

    def accept_text(self):
        text = self.text_area.get("1.0", tk.END).strip()
        print(f"Accepted text: {text}")
        # Define keyboard shortcut for accepting text
        pyautogui.hotkey('ctrl', 's')

    def trigger_camera(self):
        print("Triggering camera")
        # Define keyboard shortcut for triggering camera
        pyautogui.hotkey('enter')



if __name__ == "__main__":


    ahk = AHK()

    all_windows = ahk.list_windows() 
    print(all_windows)


    root = tk.Tk()
    app = App(root)
    root.mainloop()
