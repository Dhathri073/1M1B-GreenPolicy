# 🚀 Quick Start Guide

## Get Your Green Policy Chatbot Running in 3 Steps!

### Step 1: Install Dependencies ⚙️

Open a terminal and navigate to the backend folder:

```bash
cd backend
pip install -r requirements.txt
```

This installs:
- FastAPI (web framework)
- sentence-transformers (AI embeddings)
- FAISS (vector search)
- uvicorn (web server)

### Step 2: Start the Backend Server 🖥️

```bash
python app.py
```

You should see:
```
🚀 Initializing RAG Engine...
📚 Loading 2 document(s)...
✅ Loaded: sustainability_policy_sample.txt (X chunks)
✅ Loaded: climate_action_plan.txt (X chunks)
✅ RAG Engine initialized with X text chunks
✅ RAG Engine ready!
```

The server will run at `http://localhost:8000`

### Step 3: Open the Chatbot 🌐

**Option A: Direct File Open**
- Navigate to the `frontend` folder
- Double-click `index.html`
- It will open in your default browser

**Option B: Using a Local Server** (recommended)

Open a new terminal:
```bash
cd frontend
python -m http.server 3000
```

Then visit: `http://localhost:3000`

---

## 💬 Try These Sample Questions:

- "What are the solar panel subsidies?"
- "Tell me about electric vehicle incentives"
- "What is the carbon tax policy?"
- "What are the renewable energy targets?"
- "How does the emissions trading scheme work?"
- "What is the plastic ban regulation?"
- "Tell me about the reforestation initiative"

---

## 📚 Adding Your Own Documents

1. Create `.txt` files with your policy documents
2. Place them in the `documents/` folder
3. Restart the backend server (`Ctrl+C` then `python app.py` again)
4. The new documents will be automatically indexed!

---

## ❓ Troubleshooting

### "Backend not connected" message in the chatbot:
- Make sure the backend server is running (`python app.py`)
- Check that it's running on port 8000
- Verify no errors in the terminal

### No answer or poor answers:
- Make sure there are `.txt` files in the `documents/` folder
- Check that the documents contain relevant information
- Try rephrasing your question

### Installation errors:
- Make sure you have Python 3.8 or higher: `python --version`
- Try upgrading pip: `pip install --upgrade pip`
- On some systems, use `pip3` instead of `pip`

---

## 🎉 That's It!

Your RAG-powered sustainability chatbot is now ready to answer questions based on your policy documents!

The chatbot will ONLY answer based on the documents you provide - ensuring accurate, document-grounded responses.

---

**Need Help?** Check the full README.md for more details and advanced configuration options.

