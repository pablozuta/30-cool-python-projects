'''
This Python project uses the langdetect module (see pip install instructions) to help us identify the language that has been entered. This can be really useful if you’re unsure which language you’re dealing with. 
'''

from langdetect import detect
import tkinter as tk
import customtkinter


 



def detect_lang():
    
    
    window = customtkinter.CTk()
    window.geometry("600x400")
    window.title("Language Detector")

    def check_language():
        new_text = text.get()
        lang = detect(str(new_text))
        tk.Label(window, text=lang).place(x=260, y=200)

    text = tk.StringVar()    
    tk.Entry(window, textvariable=text).place(
        x=200, y=80, height=30, width=280)
    customtkinter.CTkButton(window, text="Check Language",
             command=check_language) .place(x=285, y=150)    
    window.mainloop()



if __name__ == '__main__':
    detect_lang()