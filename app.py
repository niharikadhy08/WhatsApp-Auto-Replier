import streamlit as st
import threading
import bot

st.set_page_config(page_title="WhatsApp Auto Replier", layout="centered")

st.title("🤖 WhatsApp Auto Replier")

st.write("Control your WhatsApp bot using buttons below.")

if "bot_running" not in st.session_state:
    st.session_state.bot_running = False


def start_bot():
    if not st.session_state.bot_running:
        st.session_state.bot_running = True
        threading.Thread(target=bot.run_bot, daemon=True).start()


def stop_bot():
    st.session_state.bot_running = False
    bot.stop_bot()


col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Start Bot"):
        start_bot()

with col2:
    if st.button("⏹ Stop Bot"):
        stop_bot()

st.markdown("---")

if st.session_state.bot_running:
    st.success("Bot is running 🟢")
else:
    st.warning("Bot is stopped 🔴")

st.info("⚠️ Keep WhatsApp Web open and visible while the bot is running.")
