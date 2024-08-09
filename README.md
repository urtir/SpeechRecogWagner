# Offline Speech Recognition with Python

This repository demonstrates how to build a real-time Speech-to-Text application in Python that works offline using the Vosk library. The application captures audio from a microphone, converts it into text, and stops running when a specific phrase ("please stop all of this") is detected.

## Features

- **Real-Time Speech Recognition**: Converts spoken words into text in real-time.
- **Offline Functionality**: No need for an internet connection, all processing is done locally.
- **Customizable Stop Command**: The application stops when the phrase "selesai bicara" is detected, allowing for easy termination of the speech recognition process.
- **Multi-Language Support**: Supports various languages, including Bahasa Indonesia, with downloadable Vosk models.

## Requirements

- Python 3.6+
- [Vosk](https://pypi.org/project/vosk/) library
- [PyAudio](https://pypi.org/project/PyAudio/) library (for microphone input)
- [SoundDevice](https://pypi.org/project/sounddevice/) library (for capturing audio)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/offline-speech-recognition-python.git
2. Install the required Python libraries:
   ```bash
   pip install vosk pyaudio sounddevice
3. Download the appropriate Vosk language model from the [Vosk Model Repository](https://alphacephei.com/vosk/models) and extract it to the project directory.
