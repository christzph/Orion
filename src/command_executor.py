from datetime import datetime
import locale

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    print("Localidade 'pt_BR.UTF-8' não encontrada. O nome do mês pode ficar em inglês.")

def execute_local_command(command: str) -> str | None:

    command = command.lower()

    if "que horas são" in command or "me diga as horas" in command:
        now = datetime.now()
        return f"Agora são {now.hour} horas e {now.minute} minutos."

    if "que dia é hoje" in command or "qual a data de hoje" in command:
        now = datetime.now()
        return now.strftime("Hoje é dia %d de %B de %Y.")
        
    return None