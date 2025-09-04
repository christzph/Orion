const chatContainer = document.getElementById('chat-container');
const inputForm = document.getElementById('input-form');
const userInput = document.getElementById('userInput');
const micBtn = document.getElementById('micBtn');
const loadingIndicator = document.getElementById('loading-indicator');

const API_URL = 'http://localhost:3000/api/ask';

function addMessage(sender, text) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender === 'user' ? 'user-message' : 'orion-message');
    messageElement.textContent = text;
    chatContainer.appendChild(messageElement);

    chatContainer.scrollTop = chatContainer.scrollHeight;
}


async function sendMessageToBackend(text) {
    loadingIndicator.classList.remove('hidden');
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: text }),
        });

        if (!response.ok) {
            throw new Error('A resposta da rede não foi OK.');
        }

        const data = await response.json();
        const orionResponse = data.response;
        
        addMessage('orion', orionResponse);
        speak(orionResponse); 

    } catch (error) {
        console.error('Erro ao enviar mensagem:', error);
        addMessage('orion', 'Desculpe, tive um problema de comunicação com meu servidor. Tente novamente.');
    } finally {
        loadingIndicator.classList.add('hidden');
    }
}

inputForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const userText = userInput.value.trim();

    if (userText) {
        addMessage('user', userText);
        sendMessageToBackend(userText);
        userInput.value = '';
    }
});


function speak(text) {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'pt-BR';
        window.speechSynthesis.speak(utterance);
    } else {
        console.log("Seu navegador não suporta a síntese de voz.");
    }
}

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.lang = 'pt-BR';
    recognition.continuous = false;

    micBtn.addEventListener('click', () => {
        micBtn.classList.add('recording');
        recognition.start();
    });

    recognition.onresult = (event) => {
        const spokenText = event.results[0][0].transcript;
        userInput.value = spokenText;

        inputForm.dispatchEvent(new Event('submit'));
    };

    recognition.onerror = (event) => {
        console.error("Erro no reconhecimento de voz:", event.error);
        alert(`Erro no reconhecimento: ${event.error}`);
    };

    recognition.onend = () => {
        micBtn.classList.remove('recording');
    };

} else {
    console.log("Seu navegador não suporta o reconhecimento de voz.");
    micBtn.style.display = 'none';
}


window.onload = () => {
    const welcomeMessage = "Olá! Sou o Orion. Como posso te ajudar hoje?";
    addMessage('orion', welcomeMessage);
    speak(welcomeMessage);
};