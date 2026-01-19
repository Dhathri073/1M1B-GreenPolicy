// API Configuration
const API_URL = 'http://localhost:8000';

// DOM Elements
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const chatMessages = document.getElementById('chatMessages');
const sendButton = document.getElementById('sendButton');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    userInput.focus();
    checkBackendStatus();
});

// Check if backend is running
async function checkBackendStatus() {
    try {
        const response = await fetch(`${API_URL}/health`, {
            method: 'GET',
        });
        if (response.ok) {
            console.log('✅ Backend is connected');
        }
    } catch (error) {
        console.warn('⚠️ Backend not connected. Start the backend server to enable chatbot functionality.');
        addMessage('bot', 'Note: Backend server is not running. Please start the server to use the chatbot.', true);
    }
}

// Handle form submission
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const question = userInput.value.trim();
    if (!question) return;
    
    // Add user message
    addMessage('user', question);
    
    // Clear input
    userInput.value = '';
    
    // Disable input while processing
    setInputState(false);
    
    // Add loading message
    const loadingId = addLoadingMessage();
    
    try {
        // Send request to backend
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        });
        
        if (!response.ok) {
            throw new Error('Failed to get response from server');
        }
        
        const data = await response.json();
        
        // Remove loading message
        removeLoadingMessage(loadingId);
        
        // Add bot response
        addMessage('bot', data.answer, false, data.sources);
        
    } catch (error) {
        console.error('Error:', error);
        removeLoadingMessage(loadingId);
        addMessage('bot', 'Sorry, I encountered an error. Please make sure the backend server is running and try again.', true);
    } finally {
        setInputState(true);
        userInput.focus();
    }
});

// Add message to chat
function addMessage(sender, text, isError = false, sources = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    
    const avatar = document.createElement('div');
    avatar.className = `message-avatar ${sender}-avatar`;
    avatar.textContent = sender === 'user' ? '👤' : '🤖';
    
    const content = document.createElement('div');
    content.className = 'message-content';
    
    const textP = document.createElement('p');
    textP.textContent = text;
    if (isError) {
        textP.style.color = '#e53e3e';
    }
    content.appendChild(textP);
    
    // Add sources if available
    if (sources && sources.length > 0) {
        const sourcesDiv = document.createElement('div');
        sourcesDiv.className = 'sources';
        
        const sourcesTitle = document.createElement('div');
        sourcesTitle.className = 'sources-title';
        sourcesTitle.textContent = '📄 Sources:';
        sourcesDiv.appendChild(sourcesTitle);
        
        sources.forEach((source, index) => {
            const sourceItem = document.createElement('div');
            sourceItem.className = 'source-item';
            sourceItem.textContent = `${index + 1}. ${source}`;
            sourcesDiv.appendChild(sourceItem);
        });
        
        content.appendChild(sourcesDiv);
    }
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Add loading message
function addLoadingMessage() {
    const loadingId = `loading-${Date.now()}`;
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message loading-message';
    messageDiv.id = loadingId;
    
    const avatar = document.createElement('div');
    avatar.className = 'message-avatar bot-avatar';
    avatar.textContent = '🤖';
    
    const content = document.createElement('div');
    content.className = 'message-content';
    content.innerHTML = `
        <div class="loading-dot"></div>
        <div class="loading-dot"></div>
        <div class="loading-dot"></div>
    `;
    
    messageDiv.appendChild(avatar);
    messageDiv.appendChild(content);
    
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
    
    return loadingId;
}

// Remove loading message
function removeLoadingMessage(loadingId) {
    const loadingMessage = document.getElementById(loadingId);
    if (loadingMessage) {
        loadingMessage.remove();
    }
}

// Enable/disable input
function setInputState(enabled) {
    userInput.disabled = !enabled;
    sendButton.disabled = !enabled;
}

// Scroll to bottom of chat
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Handle Enter key
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        chatForm.dispatchEvent(new Event('submit'));
    }
});

