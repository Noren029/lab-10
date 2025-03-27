import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import ctypes
import os
from poke_api import get_pokemon_list, download_pokemon_image

# Load Windows DLL function
dll = ctypes.windll.user32
dll.MessageBoxW(0, "Welcome to the Pokémon Viewer!", "Info", 1)

def on_pokemon_selected(event):
    pokemon_name = combo.get()
    image_path = download_pokemon_image(pokemon_name)
    if image_path:
        photo = PhotoImage(file=image_path)
        img_label.config(image=photo)
        img_label.photo = photo
    else:
        messagebox.showerror("Error", "Image not found!")

def exit_app():
    root.quit()

# Initialize Tkinter window
root = tk.Tk()
root.title("Pokémon Viewer")
root.geometry("400x500")
root.resizable(True, True)
root.iconbitmap("pokeball.ico")

# UI Elements
frame = tk.Frame(root)
frame.pack(pady=20)

combo = ttk.Combobox(frame, state="readonly", width=30)
combo['values'] = get_pokemon_list()
combo.pack()
combo.bind("<<ComboboxSelected>>", on_pokemon_selected)

img_label = tk.Label(root)
img_label.pack()

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=10)

root.mainloop()

