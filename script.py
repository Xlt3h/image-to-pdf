#create a gui with two inputs
import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image 

def img_pdf(filename,output):
    images = []
    for file in filename:
        im  = Image.open(file)
        im = im.convert('RGB')
        images.append(im)
    images[0].save(output,save_all=True,append_images=images[1:])
    #tkinter message box
    tk.messagebox.showinfo("Success","Your PDF has been created")
tk_ = tk.Tk()
tk_.title("image to pdf")
tk_.geometry("400x400")
#create a button that opens file dialog
def open_file():
    filename = fd.askopenfilenames()
    return filename
def save_file():
    output = fd.asksaveasfilename(defaultextension=".pdf")
    return output
def main():
    filename = open_file()
    output = save_file()
    img_pdf(filename,output)
button = tk.Button(tk_,text="Select Images",command=main)
button.pack()
tk_.mainloop()

