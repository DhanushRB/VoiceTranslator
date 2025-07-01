
# Whisper Language Detector and English Translator

This project records audio from a microphone, transcribes it using OpenAI's Whisper large-v3 model, detects the spoken language, and translates the text into English.

## Features

- Microphone audio recording
- Whisper-based speech recognition using the large-v3 model
- Language detection with full language name
- Translation to English
- Option to run the process in a loop

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/whisper-language-translator.git
cd whisper-language-translator
```

### 2. Create and Activate Virtual Environment (Optional but Recommended)

On macOS/Linux:

```
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Required Python Packages

```
pip install -r requirements.txt
```

If `pyaudio` fails, this project uses `sounddevice` as an alternative, so you can ignore `pyaudio`.

## Required Dependencies

This project requires the following Python packages:

- openai-whisper
- googletrans==4.0.0-rc1
- langdetect
- sounddevice
- numpy
- scipy

You can install them manually:

```
pip install openai-whisper googletrans==4.0.0-rc1 langdetect sounddevice numpy scipy
```

## FFmpeg Requirement

The Whisper model depends on FFmpeg to process audio. Make sure it is installed on your system and available in your system PATH.

### Windows

1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract it and move it to a folder like `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to your system PATH environment variable
4. Restart the terminal and verify using:

```
ffmpeg -version
```

### macOS (Homebrew)

```
brew install ffmpeg
```

### Ubuntu / Debian

```
sudo apt update
sudo apt install ffmpeg
```

## Running the Application

To run the application:

```
python app.py
```

You will be prompted to speak. The program will:

1. Record a short audio sample (default is 5 seconds)
2. Transcribe the speech using Whisper
3. Detect the language
4. Translate the recognized text to English
5. Ask if you want to run again

## Project Structure

```
whisper-language-translator/
│
├── app.py              # Main script
├── recorded.wav        # Temporary recorded audio file
├── requirements.txt    # List of required Python packages
└── README.md           # This file
```

## Common Issues

- If `ffmpeg` is not found, check if it is correctly installed and added to the PATH.
- If microphone access fails, make sure your microphone is connected and the program has permission.
- If Whisper is slow, consider using a GPU or a smaller model like `base`, `small`, or `medium`.

## License

This project is open-source and licensed under the MIT License. You are free to use, modify, and distribute it.
