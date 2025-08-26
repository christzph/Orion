import speech_recognition as sr
import pyttsx3
from config import ASSISTANT_LANGUAGE

def listen_to_user() -> str | None:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Reconhecendo...")
        text = recognizer.recognize_google(audio, language=ASSISTANT_LANGUAGE)
        print(f"Usuário disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return None
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento; {e}")
        return None

def speak(text: str):
    engine = pyttsx3.init()
    engine.say(text)
    print(f"Assistente: {text}")
    engine.runAndWait()