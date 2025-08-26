# src/gemini_client.py
import google.generativeai as genai
from config import GEMINI_API_KEY

# Mensagem de erro para o caso da chave não ter sido configurada
if not GEMINI_API_KEY or GEMINI_API_KEY == "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent":
    raise ValueError("A chave da API Gemini não foi configurada. Por favor, adicione sua chave no arquivo 'config.py'.")

# Configura a API Key
genai.configure(api_key=GEMINI_API_KEY)

# Inicializa o modelo
model = genai.GenerativeModel('gemini-pro')

def get_gemini_response(prompt: str) -> str:
    """
    Envia o prompt do usuário para a Gemini API e retorna a resposta em texto.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Erro ao contatar a API Gemini: {e}")
        return "Desculpe, não consegui me conectar aos meus servidores de inteligência."