from . import voice_handler
from . import gemini_client
from . import command_executor

def main():
    print("--------------------------------------------------------------------------")
    voice_handler.speak("Olá! Sou o Orion. Como posso te ajudar?")
    
    while True:
        print("  1: Falar | 2: Digitar | 3: Sair")

        choice = input("\nSua escolha: ")
        print("\n")
        user_input = None 

        if choice == '1':
            user_input = voice_handler.listen_to_user()
        elif choice == '2':
            user_input = input("Você: ")
        elif choice == '3':
            voice_handler.speak("Até mais!")
            break
        else:
            print("Opção inválida, tente novamente.")
            continue
        
        if user_input:
            if "desligar" in user_input.lower() or "parar" in user_input.lower():
                voice_handler.speak("Até mais!")
                break
            
            response = gemini_client.generate_response(user_input)
            print("\n")
            voice_handler.speak(response)

def line():
    print("---" * 100)

if __name__ == "__main__":
    main()