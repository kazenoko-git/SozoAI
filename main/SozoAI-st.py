import instances as ins
import chat
try: import streamlit as st
except: ins.install("streamlit")
finally: import streamlit as st
st.set_page_config(page_title="Sozomi LLM", page_icon=":tada:", layout="wide") # https://www.webfx.com/tools/emoji-cheat-sheet/
with st.container():
    global AI, TTS
    st.header("sozomi LLM")
    st.text_input("your username: ", key="username")
    name = str(st.session_state.username)
    AI = chat.completions(username=name, model="sozomi-discord", test=True)

with st.container():
    if "username" not in st.session_state:
        st.write("please enter your username first.")
        print("WARN: No username detected.")
    else:
        st.write("---")
        st.subheader("chat with Sozomi!")
        st.text_input("chat with Sozomi!", key="prompt", label_visibility="hidden")
        if "prompt" not in st.session_state:
            print("WARN: No prompt detected.")
        else: st.write(AI.create(str(st.session_state.prompt)))