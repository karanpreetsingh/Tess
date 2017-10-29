from init.base import start_keyphrase_recognition, tokenize
import init.settings as st

st.init()

if __name__ == "__main__":    
    start_keyphrase_recognition(tokenize, st.globalName)
