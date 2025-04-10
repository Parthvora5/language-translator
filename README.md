# 🌍 Language Translator

![Title Image](https://github.com/ashin-coder/language-translator/assets/73836674/04a6874c-adf6-4ba1-9030-83253d386e8f)

The **Language Translator** is a powerful Python-based application designed to bridge communication gaps by enabling seamless translation across 100+ languages. With intelligent auto-detect, text-to-speech, and speech-to-text capabilities, this tool makes global interaction intuitive and effortless.

Developed using **Tkinter** for the GUI and powered by APIs like **Google Translate**, the app provides a clean and user-friendly experience suitable for both casual and professional users.

---

## 🛠 Created By

This project was co-developed by:

- 👨‍💻 [Parth Vora](https://github.com/Parthvora5)
- 👨‍💻 [Dhruvin Kheni](https://github.com/Khenidhruvin2001)

👥 Both contributors have equally shared the development work **50/50**.

[![Contributors](https://img.shields.io/github/contributors/Parthvora5/language-translator)](https://github.com/Parthvora5/language-translator/graphs/contributors)
[![Built By](https://img.shields.io/badge/Co--Developed%20By-Parth%20%26%20Dhruvin-blueviolet)](https://github.com/Parthvora5/language-translator)

---

## 🚀 Features

- 🌐 **Translate Text**: Support for over 100 languages using Google Translate API
- 🔊 **Text-to-Speech**: Hear translated text aloud with `gTTS`
- 🎤 **Speech-to-Text**: Speak in English and translate into any language using `speech_recognition`
- 📋 **Copy**: Quickly copy translated text to your clipboard
- 🧹 **Clear**: Instantly clear the input and output text areas
- 🖼️ **Simple GUI**: Built with Tkinter for an intuitive interface

---

## 🛠 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Parthvora5/language-translator.git

# 2. Change directory
cd language-translator

# 3. Create and activate a virtual environment (optional but recommended)
python -m venv env
env\Scripts\activate  # For Windows

# 4. Install the dependencies
pip install -r requirements.txt

# 5. Run the application
python main.py
```

📌 **Note**: This project was developed using **Python 3.10** and tested in **PyCharm**. While it may run in other IDEs, PyCharm is recommended. An **internet connection is required** for real-time translations and speech recognition.

---

## 🧩 Implementation Details

- **Translation Engine**: Utilizes `googletrans` to handle text translation with auto language detection.
- **Text-to-Speech**: Powered by `gTTS`, creates an MP3 file played by the system's default media player.
- **Speech Recognition**: Uses `speech_recognition` to capture English audio input and convert it to text.
- **Clipboard Integration**: Via `pyperclip`, translated text can be copied instantly.
- **Interface**: Built with `tkinter`, the GUI includes dropdowns for source/target languages, input/output text boxes, and control buttons.

---

## 📸 Screenshots

### 🔤 Translate Text
![text_translate](https://github.com/ashin-coder/language-translator/assets/73836674/bd609942-9381-444a-912f-9c3183a33727)

### 📋 Copy
![copy_1](https://github.com/ashin-coder/language-translator/assets/73836674/600ff069-707e-4e98-a9fb-cca3edb5ffa7)
![copy_2](https://github.com/ashin-coder/language-translator/assets/73836674/5722d2b1-7d88-4970-b27e-8c67cf76d616)

### 🔊 Read Aloud
![read_aloud](https://github.com/ashin-coder/language-translator/assets/73836674/ca3ee180-f9bc-4f18-b740-770709da3868)

### 🎙 Voice Input
![voice_input](https://github.com/ashin-coder/language-translator/assets/73836674/a1d9ddfc-477c-4946-a37a-19dfd32d9b76)

### 🧹 Clear
![clear](https://github.com/ashin-coder/language-translator/assets/73836674/28b035b4-c624-4823-a49f-e44f3ec9cbac)

---

## 🎖 Badges

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Made with Tkinter](https://img.shields.io/badge/Made%20with-Tkinter-brightgreen)](https://docs.python.org/3/library/tkinter.html)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/Parthvora5/language-translator)
[![Contributors](https://img.shields.io/github/contributors/Parthvora5/language-translator)](https://github.com/Parthvora5/language-translator/graphs/contributors)
[![Built By](https://img.shields.io/badge/Built%20With-Parth%20%26%20Dhruvin-blue)](https://github.com/Parthvora5/language-translator)

---

## 🙏 Acknowledgments

Huge thanks to:
- The developers of Python and its incredible libraries: `googletrans`, `gTTS`, `speech_recognition`, `pyperclip`, `tkinter`
- [Flaticon](https://www.flaticon.com/) for icon support
- The open-source community for inspiration and support

---

## 🧑‍💻 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Parthvora5">
        <img src="https://github.com/Parthvora5.png" width="80px;" alt="Parth Vora"/><br />
        <sub><b>Parth Vora</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Khenidhruvin2001">
        <img src="https://github.com/Khenidhruvin2001.png" width="80px;" alt="Dhruvin Kheni"/><br />
        <sub><b>Dhruvin Kheni</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## ⚠️ Project Disclaimer

> This project is shared for **educational and demonstration purposes only**. While fully functional, it may contain bugs or require improvements before real-world deployment. Contributions and suggestions are welcome!

Feel free to fork, star ⭐, improve, and use this project in your own apps!

---

**Made with ❤️ by [Parth Vora](https://github.com/Parthvora5) and [Dhruvin Kheni](https://github.com/Khenidhruvin2001)**
