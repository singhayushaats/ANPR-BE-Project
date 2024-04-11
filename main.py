# import tkinter
# import os
# import sys
# import subprocess
# from tkinter import filedialog
# from PIL import Image, ImageTk

# def open_image():
#     global img
#     global img_name
#     global submit

#     img_name = filedialog.askopenfilename(initialdir=".", title="Select Image", filetypes=(("images", "*.jpg"), ("images", "*.bmp"), ("image", "*.*")))
#     print(img_name)
#     input.insert(0, img_name)

#     label_original = tkinter.Label(root, text="Original Image:")
#     label_original.grid(column=0, row=2)

#     img = ImageTk.PhotoImage(Image.open(img_name).resize((250, 250)))
#     label_image = tkinter.Label(root, image=img)
#     label_image.grid(column=0, row=3)

#     submit = tkinter.Button(root, text="Submit", command=call_haze)
#     submit.grid(column=0, row=4)

# def call_haze():
#     global dehazed
#     submit.destroy()
#     subprocess.call(f"python haze_removal.py \"{img_name}\"", shell=True)
#     msg = tkinter.Label(root, text="Dehazing complete! Image stored in dehazed folder.")
#     msg.grid(column=0, row=4, columnspan=2)

#     label_dehazed = tkinter.Label(root, text="Dehazed Image:")
#     label_dehazed.grid(column=1, row=2)

#     dehazed = ImageTk.PhotoImage(Image.open("img/dst.jpg").resize((250, 250)))
#     label_dehazed_image = tkinter.Label(root, image=dehazed)
#     label_dehazed_image.grid(column=1, row=3, padx=10)

#     retry = tkinter.Button(root, text="Retry", command=restart_program)
#     retry.grid(column=0, row=5)

#     quit_button = tkinter.Button(root, text="Quit", command=quit_program)
#     quit_button.grid(column=1, row=5)

# def restart_program():
#     os.execl(sys.executable, sys.executable, *sys.argv)

# def quit_program():
#     sys.exit()
# # Create the main Tkinter window
# root = tkinter.Tk()
# root.title("Dehaze")
# root.update_idletasks()

# # Create and place the label
# label = tkinter.Label(root, text="Select image or enter image path:")
# label.grid(column=0, row=0, pady=10)

# # Create and place the entry widget
# input = tkinter.Entry(root, width=50)
# input.grid(column=0, row=1, padx=10, pady=10)

# # Create and place the "Browse" button
# browse = tkinter.Button(root, text="Browse", command=open_image)
# browse.grid(column=1, row=1)

# # Start the Tkinter event loop
# root.mainloop()

import tkinter
import os
import sys
import subprocess
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    global img
    global img_name
    global submit

    img_name = filedialog.askopenfilename(initialdir=".", title="Select Image", filetypes=(("images", "*.jpg"), ("images", "*.bmp"), ("image", "*.*")))
    print(img_name)
    input_entry.delete(0, tkinter.END)
    input_entry.insert(0, img_name)

    label_original = tkinter.Label(root, text="Original Image:")
    label_original.grid(column=0, row=2)

    img = ImageTk.PhotoImage(Image.open(img_name).resize((250, 250)))
    label_image = tkinter.Label(root, image=img)
    label_image.grid(column=0, row=3)

    submit = tkinter.Button(root, text="Submit", command=call_haze)
    submit.grid(column=0, row=4)

def call_haze():
    global dehazed
    submit.destroy()
    subprocess.call(f"python haze_removal.py \"{img_name}\"", shell=True)
    msg = tkinter.Label(root, text="Dehazing complete! Image stored in dehazed folder.")
    msg.grid(column=0, row=4, columnspan=2)

    label_dehazed = tkinter.Label(root, text="Dehazed Image:")
    label_dehazed.grid(column=1, row=2)

    dehazed = ImageTk.PhotoImage(Image.open("img/dst.jpg").resize((250, 250)))
    label_dehazed_image = tkinter.Label(root, image=dehazed)
    label_dehazed_image.grid(column=1, row=3, padx=10)

    retry = tkinter.Button(root, text="Retry", command=restart_program)
    retry.grid(column=0, row=5)

    quit_button = tkinter.Button(root, text="Quit", command=quit_program)
    quit_button.grid(column=1, row=5)

def restart_program():
    os.execl(sys.executable, sys.executable, *sys.argv)

def quit_program():
    sys.exit()

# Create the main Tkinter window
root = tkinter.Tk()
root.title("Dehaze")
root.update_idletasks()

# Create and place the label
label = tkinter.Label(root, text="Select image or enter image path:")
label.grid(column=0, row=0, pady=10)

# Create and place the entry widget
input_entry = tkinter.Entry(root, width=50)
input_entry.grid(column=0, row=1, padx=10, pady=10)

# Create and place the "Browse" button
browse_button = tkinter.Button(root, text="Browse", command=open_image)
browse_button.grid(column=1, row=1)

# Start the Tkinter event loop
root.mainloop()
