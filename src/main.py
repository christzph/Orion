# src/main.py
import voice_handler
import gemini_client  # <--- MUDANÇA AQUI
# import command_executor # Futura implementação

def main():
    """
    Loop principal do assistente de voz Orion.
    """
    voice_handler.speak("Olá! Sou o Orion. Como posso te ajudar?")
    
    while True:
        user_input = voice_handler.listen_to_user()
        
        if user_input:
            # Comando para encerrar o assistente
            if "desligar" in user_input.lower() or "parar" in user_input.lower():
                voice_handler.speak("Até mais!")
                break
            
            # Futuramente, aqui podemos checar por comandos locais antes de enviar para a Gemini
            
            # Envia a pergunta do usuário para a Gemini API
            response = gemini_client.get_gemini_response(user_input)
            
            # Reproduz a resposta para o usuário
            voice_handler.speak(response)

if __name__ == "__main__":
    main()