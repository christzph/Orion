import google.generativeai as genai
from config import GEMINI_API_KEY
import command_executor

if not GEMINI_API_KEY or GEMINI_API_KEY == "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent":
    raise ValueError("A chave da API Gemini não foi configurada. Por favor, adicione sua chave no arquivo 'config.py'.")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')


def generate_response(prompt: str) -> str:

    local_response = command_executor.execute_local_command(prompt)
    if local_response:
        return local_response

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao contatar a API Gemini: {e}")
        return "Desculpe, não consegui me conectar aos meus servidores de inteligência."