# 🌱 Green Policy Chatbot - AI Sustainability Assistant

A simple AI chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer questions about sustainability policies and green schemes based on official government documents.

## ✨ Features

- 💬 Interactive chat interface
- 🔍 RAG-based document retrieval
- 📚 Answers ONLY from provided policy documents
- 🎨 Modern, responsive UI
- ⚡ Fast semantic search using FAISS
- 🔗 Source attribution for transparency

## 🏗️ Architecture

### Frontend
- Pure HTML/CSS/JavaScript
- Modern gradient design
- Real-time chat interface
- Responsive for mobile and desktop

### Backend
- **FastAPI** - Python web framework
- **sentence-transformers** - For text embeddings
- **FAISS** - Vector similarity search
- **RAG Engine** - Custom retrieval system

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip
- Modern web browser

### Setup Instructions

1. **Clone or navigate to the project directory**

2. **Install Python dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Add your policy documents**
Place your sustainability policy documents (`.txt` files) in the `documents/` folder. Sample documents are already included:
- `sustainability_policy_sample.txt`
- `climate_action_plan.txt`

4. **Start the backend server**
```bash
python app.py
```
The server will start at `http://localhost:8000`

5. **Open the frontend**
Simply open `frontend/index.html` in your web browser, or use a local server:
```bash
cd frontend
python -m http.server 3000
```
Then visit `http://localhost:3000`

## 🚀 Usage

1. Open the chatbot interface in your browser
2. Type questions about sustainability policies, green schemes, or environmental regulations
3. The chatbot will search through the policy documents and provide relevant answers
4. Sources are cited at the bottom of each response

### Example Questions:
- "What are the solar panel subsidies available?"
- "Tell me about electric vehicle incentives"
- "What is the carbon tax policy?"
- "What are the renewable energy targets for 2030?"
- "How does the emissions trading scheme work?"

## 📁 Project Structure

```
project/
├── frontend/
│   ├── index.html          # Main HTML file
│   ├── style.css           # Styling
│   └── script.js           # Frontend logic
├── backend/
│   ├── app.py              # FastAPI application
│   ├── rag_engine.py       # RAG implementation
│   └── requirements.txt    # Python dependencies
├── documents/
│   ├── sustainability_policy_sample.txt
│   └── climate_action_plan.txt
└── README.md
```

## 🔧 Configuration

### Adding More Documents
1. Create `.txt` files with your policy documents
2. Place them in the `documents/` folder
3. Restart the backend server
4. The RAG engine will automatically index the new documents

### Customizing the RAG Engine
Edit `backend/rag_engine.py` to:
- Change chunk size for document splitting
- Adjust number of retrieved documents (`top_k`)
- Modify the embedding model
- Customize answer generation

### API Endpoints
- `GET /health` - Check if server is running
- `POST /chat` - Send a question and get an answer
- `GET /documents` - List all loaded documents

## 🎯 How RAG Works

1. **Document Loading**: Policy documents are loaded and split into chunks
2. **Embedding**: Each chunk is converted to a vector using sentence-transformers
3. **Indexing**: Vectors are stored in a FAISS index for fast similarity search
4. **Query Processing**: User questions are embedded and matched against document chunks
5. **Retrieval**: Most relevant chunks are retrieved
6. **Answer Generation**: An answer is composed from the retrieved information

## ⚡ Performance Notes

- Uses lightweight `all-MiniLM-L6-v2` model for fast embeddings
- FAISS provides millisecond-level similarity search
- Can handle documents of any size
- No external API calls required (runs locally)

## 🔐 Security & Privacy

- All processing happens locally
- No data sent to external services
- No API keys required
- Documents remain on your server

## 🛠️ Troubleshooting

**Backend not connecting:**
- Check if Python server is running on port 8000
- Verify no firewall blocking localhost connections

**No documents loaded:**
- Ensure `.txt` files are in the `documents/` folder
- Check file encoding is UTF-8
- Restart the backend after adding documents

**Slow responses:**
- Consider reducing document size or number of chunks
- Adjust `top_k` parameter for fewer retrievals

## 📈 Future Enhancements

- Integration with LLMs (OpenAI, Anthropic) for better answer synthesis
- Support for PDF and Word documents
- Multi-language support
- Chat history and conversation context
- Advanced document preprocessing
- User authentication
- Document upload interface

## 📄 License

This is an educational project for demonstration purposes.

## 🤝 Contributing

Feel free to enhance this chatbot by:
- Adding more sophisticated answer generation
- Implementing conversation memory
- Supporting additional document formats
- Improving the UI/UX
- Adding analytics and logging

---

Built with ❤️ for sustainable policy awareness

