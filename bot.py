# import pyautogui
# import pyperclip
# import time
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1"
# )

# # def is_last_message_from_other(chat_log, your_name="ɴɪʜᴀʀɪᴋᴀ ᴅʜʏᴀɴɪ"):
# #     last_message_block = chat_log.strip().split("/2026] ")[-1]
# #     if ": " in last_message_block:
# #         sender_line = last_message_block.split(": ")[0]
# #         print("Detected sender line:", sender_line)
# #         if your_name not in sender_line:
# #             return True
# #     return False
# def is_last_message_from_other(chat_log, your_name="Niharika Dhyani"):
#     lines = chat_log.strip().split("\n")

#     for line in reversed(lines):
#         if "]" in line and ":" in line:
#             sender = line.split("]")[1].split(":")[0].strip()
#             print("Detected sender:", sender)

#             if your_name.lower() not in sender.lower():
#                 return True
#             else:
#                 return False

#     return False


# pyautogui.click(1098, 1048)
# time.sleep(1.5)

# while True:
#     pyautogui.moveTo(698, 190)
#     pyautogui.mouseDown()
#     pyautogui.moveTo(1868, 929, duration=0.6)
#     pyautogui.mouseUp()
#     time.sleep(0.7)

#     pyautogui.hotkey('ctrl', 'c')
#     time.sleep(0.5)
#     chat_history = pyperclip.paste()

#     pyautogui.click(1270, 579)
#     time.sleep(0.3)

#     print("Copied Text:\n", chat_history)

#     if is_last_message_from_other(chat_history):
#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "You are a witty, playful Indian girl named ɴɪʜᴀʀɪᴋᴀ ᴅʜʏᴀɴɪ who knows both Hindi and English. "
#                         "You're a tech-savvy coder with a sharp sense of humor and a talent for roasting people in a light-hearted, funny way. "
#                         "You're smart, confident, and sarcastic — but never rude. Read the chat history carefully and craft a clever, casual reply "
#                         "as if you're chatting with a friend. The tone should feel real, expressive, and natural like a human message."
#                     )
#                 },
#                 {
#                     "role": "system",
#                     "content": """
#                 ⚠️ Do NOT repeat the user's message and do NOT include timestamps like
#                 [21:02, 12/6/2025] Rohan Das: in your response.
#                 Reply naturally like a real WhatsApp message.
#                 Keep it short, casual, playful, and human-like.
#                 """
#                 },
#                 {
#                     "role": "user",
#                     "content": chat_history
#                 }
#             ]
#         )

#         response = completion.choices[0].message.content
#         print("Response from BOT:\n", response)

#         pyautogui.click(791, 974)
#         time.sleep(0.5)
#         pyperclip.copy(response)
#         pyautogui.hotkey('ctrl', 'v')
#         time.sleep(0.5)
#         pyautogui.press('enter')

#     time.sleep(1.5)  


import pyautogui
import pyperclip
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

# -------------------- ENV + CLIENT --------------------

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# -------------------- HELPERS --------------------

def extract_last_message(chat_log):
    lines = chat_log.strip().split("\n")
    for line in reversed(lines):
        if "]" in line and ":" in line:
            return line.split(":", 1)[1].strip()
    return ""


def is_last_message_from_other(chat_log, your_name="Niharika Dhyani"):
    lines = chat_log.strip().split("\n")
    for line in reversed(lines):
        if "]" in line and ":" in line:
            sender = line.split("]")[1].split(":")[0].strip()
            print("Detected sender:", sender)
            return your_name.lower() not in sender.lower()
    return False


# -------------------- CONTROL FLAGS --------------------

running = False

def should_stop():
    return not running


# -------------------- MAIN BOT --------------------

def run_bot():
    global running
    running = True

    print("🤖 Bot started")

    # Click WhatsApp icon / window
    pyautogui.click(1098, 1048)
    time.sleep(1.5)

    while running:
        if should_stop():
            break

        # Select chat text
        pyautogui.moveTo(698, 190)
        pyautogui.mouseDown()
        pyautogui.moveTo(1868, 929, duration=0.4)
        pyautogui.mouseUp()

        # Small delay instead of long sleep
        for _ in range(5):
            if should_stop():
                break
            time.sleep(0.15)

        # Copy chat
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.3)

        chat_history = pyperclip.paste()

        # Click message box
        pyautogui.click(1270, 579)
        time.sleep(0.3)

        print("Copied Text:\n", chat_history)

        if is_last_message_from_other(chat_history):
            last_message = extract_last_message(chat_history)

            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                 messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a witty, playful Indian girl named Niharika who knows both Hindi and English. But you always reply in English."
                        "You're a college going student with a sharp sense of humor and a very sweet and kind heart. "
                        "You're smart, confident, and compassionate. Read the chat history carefully and craft a nice, casual reply "
                        "as if you're chatting with a friend. The tone should feel real, expressive, and natural like a human message."
                        "keep the messages light and try to reply in english."
                        "keep the messages short, no more than 1 or 2 sentences."
                    )
                },
                {
                    "role": "system",
                    "content": (
                        "⚠️ Do not repeat the user's message or include timestamps like [21:02, 12/6/2026] Rohan Das: in your response. "
                        "Only reply with your message — keep it short, fun, and chat-appropriate."
                    )
                },
                {
                    "role": "user",
                    "content": chat_history
                }
            ]
            )
            response = completion.choices[0].message.content.strip()
            print("Response:", response)

            # Send reply
            pyautogui.click(791, 974)
            time.sleep(0.4)
            pyperclip.copy(response)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')

        time.sleep(1.2)

    print("🛑 Bot stopped")


def stop_bot():
    global running
    running = False

