# Jarvis-AI

A Python-based voice-controlled AI assistant that can listen to commands, open websites, tell time, and interact using OpenAI GPT.

## Features

- 🎤 Voice recognition (speech-to-text)
- 🔊 Text-to-speech responses
- 🌐 Open websites (YouTube, Google, Wikipedia)
- 🧠 AI chat using OpenAI API
- ⏰ Tell current time
- 💬 Continuous conversation mode (chat memory)

##  Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- OpenAI API
- Webbrowser module

##  Working Flow
Microphone listens to user voice 🎤
Speech converted to text
Command is analyzed
If command = website → opens browser 🌐
If command = time → returns system time ⏰
If command = general chat → sent to OpenAI 🤖
AI response is spoken using TTS 🔊
Loop continues until exit command


