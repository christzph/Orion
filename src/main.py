import voice_handler
import gemini_client

def main():
    voice_handler.speak("Olá! Sou o Orion. Como posso te ajudar?")
    
    while True:
        user_input = voice_handler.listen_to_user()
        
        if user_input:
            if "desligar" in user_input.lower() or "parar" in user_input.lower():
                voice_handler.speak("Até mais!")
                break
            
            response = gemini_client.generate_response(user_input)
            voice_handler.speak(response)

if __name__ == "__main__":
    main()