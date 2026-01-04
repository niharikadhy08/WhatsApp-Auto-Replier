# 🤖 WhatsApp Auto Replier (AI-Powered)

A Python-based WhatsApp Auto Reply Bot that reads incoming messages from **WhatsApp Web** and automatically replies using an **AI language model**.  
The bot is controlled through a **Streamlit UI** with Start/Stop buttons.

This project uses **screen automation** instead of official WhatsApp APIs and works by detecting chat text directly from the screen.

---

## 🚀 Features

- ✅ Auto-replies to incoming WhatsApp messages
- 🧠 AI-generated replies using **LLaMA (Groq API)**
- 🎛 Control bot using a **Streamlit dashboard**
- 🧍 Detects whether the last message was sent by you or the other person
- 💬 Human-like, casual, friendly replies
- 🛑 Start / Stop bot anytime

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – UI control panel
- **PyAutoGUI** – Screen & mouse automation
- **Pyperclip** – Clipboard access
- **Groq API (LLaMA models)** – AI responses
- **dotenv** – Environment variable handling

---

## 📂 Project Structure
├── app.py # Streamlit UI to control the bot
├── bot.py # Core WhatsApp automation + AI logic
├── auto_reply.py # AI test file (optional / experimental)
├── get_cursor.py # Utility to get screen coordinates
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ How It Works 

1. You open **WhatsApp Web** in your browser  
2. The bot:
   - Selects the chat
   - Copies chat text from the screen
   - Checks if the last message is from the other person
3. If yes:
   - Sends the chat history to the AI model
   - Generates a reply
   - Pastes and sends it automatically
4. You control everything using **Start / Stop buttons** in Streamlit

---
▶️Run the App - streamlit run app.py
Click Start Bot - to begin auto replying
Click Stop Bot - anytime to stop