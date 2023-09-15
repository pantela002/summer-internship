import tkinter as tk
from tkinter import filedialog
import subprocess
from tkinter import PhotoImage
from PIL import Image, ImageTk
app = tk.Tk()
app.title("GUI App")
pil_image = Image.open("/home/oopsie/Documents/Lukowa/cv_parser/blueberi1.jpg")
background_image = ImageTk.PhotoImage(pil_image)
# Set the size of the app to match the default terminal size
app.geometry("960x480")

title_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 14)
button_font = ("Helvetica", 14, "bold")


def submit_action():
    selected_option = option_var.get()
    word = word_entry.get()
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()

    # Now you can use the values: selected_option, word, input_folder, output_folder
    print("Selected Option:", selected_option)
    print("Word:", word)
    print("Input Folder:", input_folder)
    print("Output Folder:", output_folder)


    



def browse_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder)

def browse_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, output_folder)


def submit_action():
    selected_option = option_var.get()
    word = word_entry.get()
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    print("Selected Option:", selected_option)
    print("Word:", word)
    print("Input Folder:", input_folder)
    print("Output Folder:", output_folder)

    if selected_option == "Remove":
        bash_script_path = "/home/oopsie/Documents/Lukowa/cv_parser/fajl1.sh"  # Update this with the actual path
        arguments = [input_folder, selected_option]
    else:
        bash_script_path = "/home/oopsie/Documents/Lukowa/cv_parser/fajl2.sh"  # Update this with the actual path
        arguments = [input_folder, selected_option, word, output_folder]
    result = subprocess.run([bash_script_path] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("-------------------------------------------")
    # Get the output and error messages
    stdout = result.stdout.strip()
    stderr = result.stderr.strip()

    # Perform actions based on selected_option, word, input_folder, and output_folder
    # Add your code here


background_label = tk.Label(app, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Input and Output Folder Browsing
input_folder_label = tk.Label(app, text="Input Folder:", font=("Arial", 20,'bold'))
input_folder_label.pack(pady=2)

input_folder_entry = tk.Entry(app, font=("Arial", 14,'bold'))
input_folder_entry.pack(pady=2)

input_browse_button = tk.Button(app, text="Browse", command=browse_input_folder, font=("Arial", 14,'bold'))
input_browse_button.pack(pady=10)

output_folder_label = tk.Label(app, text="Output Folder:", font=("Arial", 14,'bold'))
output_folder_label.pack(pady=10)

output_folder_entry = tk.Entry(app, font=("Arial", 14,'bold'))
output_folder_entry.pack(pady=2)

output_browse_button = tk.Button(app, text="Browse", command=browse_output_folder, font=("Arial", 14,'bold'))
output_browse_button.pack(pady=2)

# Text Entry
word_label = tk.Label(app, text="Enter a word:", font=("Arial", 14,'bold'))
word_label.pack(pady=10)

word_entry = tk.Entry(app, font=("Arial", 14,'bold'))
word_entry.pack(pady=10)

# Options
options = ["Highlight", "Remove"]
option_var = tk.StringVar()
option_var.set(options[0])

option_label = tk.Label(app, text="Select an option:")
option_label.pack(pady=10)

option_menu = tk.OptionMenu(app, option_var, *options)
option_menu.pack(pady=10)

# Submit Button
submit_button = tk.Button(app, text="Submit", command=submit_action)
submit_button.pack(pady=10)

app.mainloop()
