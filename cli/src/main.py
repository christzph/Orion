from . import voice_handler
from . import gemini_client
from . import command_executor
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print("==========================================================")
    print(" OOOOO      RRRRRR     IIIIII     OOOOO     NN   NN")
    print("OO   OO     RR   RR      II      OO   OO    NNN  NN")
    print("OO   OO     RRRRRR       II      OO   OO    NN N NN")
    print("OO   OO     RR  RR       II      OO   OO    NN  NNN")
    print(" OOOOO      RR   RR    IIIIII     OOOOO     NN   NN")
    print("==========================================================")
    print("           Assistente Virtual - v1.0")
    print("----------------------------------------------------------")

def main():
    clear_screen()
    display_header()
    voice_handler.speak("Olá! Sou o Orion. Como posso te ajudar?")
    
    while True:
        print("\n[ 1: Falar ]  [ 2: Digitar ]  [ 3: Sair ]")
        choice = input(">> Sua escolha: ")
        
        user_input = None

        if choice == '1':
            user_input = voice_handler.listen_to_user()
        elif choice == '2':
            user_input = input(">> Você: ")
        elif choice == '3':
            voice_handler.speak("Até mais!")
            break
        else:
            print("\n[AVISO] Opção inválida, tente novamente.")
            time.sleep(2)
            clear_screen()
            display_header()
            continue
        
        if user_input:
            if "desligar" in user_input.lower() or "parar" in user_input.lower():
                voice_handler.speak("Até mais!")
                break
            
            print("\n>> Orion está pensando...")
            response = gemini_client.generate_response(user_input)

            clear_screen()
            display_header()
            
            print(f"🎤 Você disse: {user_input}")
            print("-" * 58)
            print("🤖 Orion responde:")
            voice_handler.speak(response)
            
            input("\n(Pressione Enter para continuar...)")
            clear_screen()
            display_header()

if __name__ == "__main__":
    main()