# Import required modules
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
from googletrans import Translator  # googletrans==3.1.0a0
import pyperclip as pc
from gtts import gTTS
import os
import speech_recognition as spr

# Initialize main window
root = tk.Tk()
root.title('Language Translator')
root.geometry('1060x660')
root.resizable(False, False)

# Load title bar icon safely
try:
    title_bar_icon = PhotoImage(file="resources/icons/translation.png")
    root.iconphoto(False, title_bar_icon)
except Exception as e:
    print("Warning: Title bar icon not loaded.", e)

cl = ''
output = ''

# Translation function
def translate():
    global cl, output
    text_input = t1.get("1.0", "end-1c")
    cl = choose_langauge.get()
    if not text_input.strip():
        messagebox.showerror('Language Translator', 'Please fill the Text Box for Translation')
        return
    try:
        t2.delete(1.0, 'end')
        translator = Translator()
        result = translator.translate(text_input, dest=cl)
        output = result.text
        t2.insert('end', output)
    except Exception as e:
        messagebox.showerror('Translation Error', f"Error: {e}")

# Clear text boxes
def clear():
    t1.delete(1.0, 'end')
    t2.delete(1.0, 'end')

# Copy translated text
def copy():
    pc.copy(str(output))

# Convert text to speech
def texttospeech():
    global cl
    cl = choose_langauge.get()
    if os.path.exists("text_to_speech.mp3"):
        os.remove("text_to_speech.mp3")
    mytext = output
    lang_map = {
        'English': 'en', 'Afrikaans': 'af', 'Albanian': 'sq', 'Arabic': 'ar', 'Hindi': 'hi',
        'French': 'fr', 'German': 'de', 'Gujarati': 'gu', 'Tamil': 'ta', 'Telugu': 'te',
        'Spanish': 'es', 'Russian': 'ru', 'Chinese': 'zh', 'Urdu': 'ur'
    }
    language = lang_map.get(cl, 'en')
    try:
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("text_to_speech.mp3")
        os.system("start text_to_speech.mp3")
    except Exception as e:
        messagebox.showerror('Text to Speech Error', f"{cl} is not supported for TTS.\n\nError: {e}")

# Convert speech to text and translate
def speechtotext():
    global cl, output
    cl = choose_langauge.get()
    from_lang = 'en'
    to_lang = cl
    recog = spr.Recognizer()
    mic = spr.Microphone()
    with mic as source:
        try:
            recog.adjust_for_ambient_noise(source)
            audio = recog.listen(source)
            sentence = recog.recognize_google(audio)
            t1.insert("end", sentence + "\n")
            translator = Translator()
            result = translator.translate(sentence, src=from_lang, dest=to_lang)
            translated_text = result.text
            output = translated_text
            t2.insert("end", translated_text + "\n")
        except spr.UnknownValueError:
            messagebox.showwarning("Speech Error", "Unable to understand the input.")
        except spr.RequestError as e:
            messagebox.showerror("Speech Error", f"Service error: {e}")

# Load background image
try:
    img = ImageTk.PhotoImage(Image.open('translator.png'))
    label = Label(image=img)
    label.place(x=0, y=0)
except Exception as e:
    print("Background image not found.", e)

# Language options
languages = ['Afrikaans', 'Albanian', 'Arabic', 'Armenian', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali',
             'Bosnian', 'Bulgarian', 'Catalan', 'Cebuano', 'Chichewa', 'Chinese', 'Corsican', 'Croatian', 'Czech',
             'Danish', 'Dutch', 'English', 'Esperanto', 'Estonian', 'Filipino', 'Finnish', 'French', 'Frisian',
             'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole', 'Hausa', 'Hawaiian', 'Hebrew',
             'Hindi', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
             'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin',
             'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese',
             'Maori', 'Marathi', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian', 'Odia', 'Pashto', 'Persian',
             'Polish', 'Portuguese', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian',
             'Sesotho', 'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish', 'Sundanese',
             'Swahili', 'Swedish', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian',
             'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']

a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=a, state='readonly', font=('Corbel', 20, 'bold'))
auto_detect['values'] = ['Auto Detect'] + languages
auto_detect.place(x=50, y=140)
auto_detect.current(0)

l = tk.StringVar()
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_langauge['values'] = languages
choose_langauge.place(x=600, y=140)
choose_langauge.current(0)

# Load icons
translate_text_icon = ImageTk.PhotoImage(Image.open("resources/icons/documents.png").resize((32, 32)))
clear_text_icon = ImageTk.PhotoImage(Image.open("resources/icons/eraser.png").resize((32, 32)))
copy_text_icon = ImageTk.PhotoImage(Image.open("resources/icons/copy.png").resize((32, 32)))
read_aloud_icon = ImageTk.PhotoImage(Image.open("resources/icons/text_to_speech.png").resize((32, 32)))
voice_input_icon = ImageTk.PhotoImage(Image.open("resources/icons/voice_recognition.png").resize((32, 32)))

# Text areas
t1 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE, font=('Calibri', 16))
t1.place(x=20, y=200)
t2 = Text(root, width=45, height=13, borderwidth=0, relief=RIDGE, font=('Calibri', 16))
t2.place(x=550, y=200)

# Buttons
Button(root, text=" Translate Text ", image=translate_text_icon, compound="right", relief=RIDGE, borderwidth=0,
       font=('Corbel', 20, 'bold'), cursor="hand2", command=translate, bg="#ffffff").place(x=40, y=565)

Button(root, text=" Clear ", image=clear_text_icon, compound="right", relief=RIDGE, borderwidth=0,
       font=('Corbel', 20, 'bold'), cursor="hand2", command=clear, bg="#ffffff").place(x=270, y=565)

Button(root, text=" Copy ", image=copy_text_icon, compound="right", relief=RIDGE, borderwidth=0,
       font=('Corbel', 20, 'bold'), cursor="hand2", command=copy, bg="#ffffff").place(x=485, y=565)

Button(root, text=" Read Aloud ", image=read_aloud_icon, compound="right", relief=RIDGE, borderwidth=0,
       font=('Corbel', 20, 'bold'), cursor="hand2", command=texttospeech, bg="#ffffff").place(x=650, y=565)

Button(root, text=" Voice Input ", image=voice_input_icon, compound="right", relief=RIDGE, borderwidth=0,
       font=('Corbel', 20, 'bold'), cursor="hand2", command=speechtotext, bg="#ffffff").place(x=850, y=565)

# Run the application
root.mainloop()
