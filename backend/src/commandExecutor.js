
function executeLocalCommand(command) {
    const lowerCaseCommand = command.toLowerCase();

    if (lowerCaseCommand.includes("que horas são") || lowerCaseCommand.includes("me diga as horas")) {
        const now = new Date();

        const timeString = now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
        return `Agora são ${timeString}.`;
    }

    if (lowerCaseCommand.includes("que dia é hoje") || lowerCaseCommand.includes("qual a data de hoje")) {
        const now = new Date();

        const dateString = now.toLocaleDateString('pt-BR', { day: 'numeric', month: 'long', year: 'numeric' });
        return `Hoje é ${dateString}.`;
    }


    return null;
}


module.exports = { executeLocalCommand };