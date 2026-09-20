import tkinter as tk

from core import autoclicker


autoclicker_instance = autoclicker()
root = tk.Tk()
root.geometry("800x600")
root.title("Auto Clicker")

def toggle_clicking():
    if button["text"] == "Start Clicking":
        button["text"] = "Stop Clicking"
        autoclicker_instance.start()


    else:
        button["text"] = "Start Clicking"
        autoclicker_instance.stop()

label = tk.Label(root, text="Auto Clicker", font=("Arial", 24))
label.pack(pady=20)



button = tk.Button(root, text="Start Clicking", font=("Arial", 16), command=toggle_clicking)
button.pack(pady=20)



scalar = tk.Scale(root, from_=0.1, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, label="Click Interval (seconds)", font=("Arial", 10), length=300) 
scalar.pack(pady=20)


root.mainloop()
