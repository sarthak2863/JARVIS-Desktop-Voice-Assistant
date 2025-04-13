# JARVIS-Desktop-Voice-Assistant
Python-based voice-controlled assistant that allows users to perform tasks such as opening websites, playing music, checking the time, and launching applications through voice commands. It uses speech recognition and text-to-speech technologies to provide a hands-free experience for interacting with your desktop.

Project Overview

JARVIS is a voice-controlled personal assistant program built using Python. It allows you to control various tasks like opening websites, playing music, checking the time, launching applications, and more, simply by speaking commands. The assistant uses speech recognition to understand the user's commands and responds with text-to-speech (TTS) technology.

This project is implemented using several popular Python libraries:
- `speech_recognition` for speech-to-text conversion.
- `pyttsx3` for text-to-speech output.
- `webbrowser` to open URLs in the browser.
- `os` to interact with the operating system (e.g., opening files or applications).
- `datetime` for fetching current time.
- `musicLibrary` (custom module) to access a music library and play songs.
  
### Key Features:
- **Voice Command Recognition**: Listen for the wake word "Jarvis" and process voice commands.
- **Web Browsing**: Open popular websites like Google, YouTube, Gmail, LinkedIn, and Hotstar using simple voice commands.
- **Music Control**: Play songs from a custom music library or open local music files.
- **System Control**: Launch common applications like Calculator, Camera, and Music Player.
- **Time Announcement**: Get the current time by asking "What is the time?".
  
## Requirements

To run the JARVIS assistant, you will need to install the following libraries:

1. **speech_recognition** - for converting speech into text.
2. **pyttsx3** - for text-to-speech functionality.
3. **webbrowser** - to open websites in a browser.
4. **os** - to execute operating system commands (e.g., opening apps).
5. **datetime** - to fetch the current date and time.
6. **musicLibrary** (Custom Module) - This module should contain a dictionary with song names as keys and their corresponding URLs as values.
   
### Install Libraries:
You can install the required libraries using `pip`:
```bash
pip install SpeechRecognition pyttsx3
```

Additionally, `musicLibrary` is a custom module that you need to create with your own music links. Here’s an example:
```python
# musicLibrary.py

music = {
    'song_name': 'https://link_to_song.com',
    'another_song': 'https://another_song_link.com',
}
```

## Project Structure

Here’s the basic structure of the project:

```
JARVIS/
│
├── jarvis.py                 # Main file for running the assistant
├── musicLibrary.py           # Custom music library module
├── requirements.txt          # List of Python dependencies
├── README.md                 # This file
└── assets/                   # Folder for any other necessary resources (e.g., music files, images)
```

### Files Breakdown:
- **jarvis.py**: Main Python script to run the assistant. This file handles speech recognition, text-to-speech, and processing the voice commands.
- **musicLibrary.py**: This is a custom Python module where you can add the songs and their respective URLs or file paths.
- **requirements.txt**: A file listing all Python dependencies to set up the environment.

## How to Use

1. **Set Up Your Environment**:
   - Make sure you have Python 3.x installed on your system.
   - Install the necessary libraries (`speech_recognition`, `pyttsx3`).
   - Create and configure the `musicLibrary.py` with your own music links or local files.

2. **Running the Program**:
   - Once all dependencies are installed, simply run the `jarvis.py` script:
   ```bash
   python jarvis.py
   ```

3. **Using the Assistant**:
   - After running the script, the assistant will be in a listening mode, waiting for the wake word "Jarvis."
   - Once "Jarvis" is detected, you can say commands like:
     - "Open Google"
     - "Play [Song Name]"
     - "What is the time?"
     - "Open Camera"
     - "Open Gmail"
   - The assistant will respond with text-to-speech and execute the corresponding actions (e.g., open websites, play music, etc.).

## Commands List

- **Wake Word**: "Jarvis" (The assistant starts listening after hearing this).
- **Website Commands**:
  - "Open Google"
  - "Open YouTube"
  - "Open Facebook"
  - "Open Gmail"
  - "Open LinkedIn"
  - "Open Hotstar"
- **Music Commands**:
  - "Play [Song Name]" (Fetches from your music library or plays a local file).
  - "Open Music" (Opens a specific local music file).
- **System Commands**:
  - "Open Camera"
  - "Open Calculator"
- **Time Command**:
  - "What is the time?"

## Troubleshooting

- **Microphone Issues**: Ensure that your microphone is properly connected and working.
- **Library Issues**: If the libraries are not found, you may need to install them using `pip install SpeechRecognition pyttsx3`.
- **Music Library**: If the assistant cannot find a song, check that the song exists in the `musicLibrary.py` with the correct name and URL.

## Contributing

If you would like to contribute to the development of JARVIS, feel free to:
1. Fork the repository.
2. Create a new branch for your features or fixes.
3. Make the changes and commit them.
4. Submit a pull request.

We appreciate your contributions and ideas!

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

---

Feel free to expand the features or customize the assistant based on your preferences.
