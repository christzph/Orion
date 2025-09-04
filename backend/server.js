const express = require('express');
const cors = require('cors');
const { GoogleGenerativeAI } = require('@google/generative-ai');
require('dotenv').config();


const { executeLocalCommand } = require('./src/commandExecutor');


const app = express();
const port = 3000;


app.use(cors());
app.use(express.json());


const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    throw new Error("A chave da API Gemini não foi configurada. Por favor, adicione sua chave no arquivo '.env'.");
}
const genAI = new GoogleGenerativeAI(apiKey);
const model = genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });

/**
 * @param {string} prompt O texto enviado pelo usuário
 * @returns {Promise<string>} A resposta do assistente
 */
async function generateResponse(prompt) {
    const localResponse = executeLocalCommand(prompt);
    if (localResponse) {
        return localResponse;
    }

    try {
        const result = await model.generateContent(prompt);
        const response = await result.response;
        return response.text();
    } catch (error) {
        console.error("Erro ao contatar a API Gemini:", error);
        return "Desculpe, não consegui me conectar aos meus servidores de inteligência.";
    }
}

app.post('/api/ask', async (req, res) => {

    const { question } = req.body;

    if (!question) {
        return res.status(400).json({ error: 'Nenhuma pergunta foi feita.' });
    }

    console.log(`Recebida a pergunta: "${question}"`);
    const responseText = await generateResponse(question);
    console.log(`Enviando a resposta: "${responseText}"`);


    res.json({ response: responseText });
});


app.listen(port, () => {
    console.log(`🤖 Servidor do Orion rodando em http://localhost:${port}`);
});