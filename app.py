from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os

app = FastAPI(title="Green Policy Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG Engine with error handling
rag_engine = None

try:
    from rag_engine_simple import RAGEngine
    rag_engine = RAGEngine()
    rag_engine.load_documents()
    print("✅ RAG Engine initialized successfully!")
except Exception as e:
    print(f"⚠️ RAG Engine initialization failed: {e}")
    print("Creating fallback response system...")
    class FallbackRAGEngine:
        def get_answer(self, question):
            return (
                "I'm currently operating in limited mode due to technical issues with the document analysis system. "
                "However, I can provide general information about sustainability and green policies.\n\n"
                f"Regarding your question: '{question}'\n\n"
                "For specific policy details, please ensure the backend system is properly configured with the required AI/ML dependencies. "
                "In the meantime, I recommend checking official government websites for the most current sustainability policies and regulations.",
                []
            )
        def get_document_list(self):
            return ["System temporarily unavailable"]

    rag_engine = FallbackRAGEngine()
    print("✅ Fallback system ready!")

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: List[str]

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Green Policy Chatbot API is running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not rag_engine:
        return ChatResponse(
            answer="I'm sorry, but the document analysis system is currently unavailable. Please try again later or contact support.",
            sources=[]
        )

    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        answer, sources = rag_engine.get_answer(request.question)
        return ChatResponse(answer=answer, sources=sources)
    except Exception as e:
        print(f"Error processing question: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")

@app.get("/documents")
async def list_documents():
    if not rag_engine:
        return {
            "documents": [],
            "count": 0,
            "message": "Document analysis system is currently unavailable"
        }

    docs = rag_engine.get_document_list()
    return {"documents": docs, "count": len(docs)}

# Serve static frontend files
@app.get("/")
async def serve_index():
    return FileResponse("index.html")

@app.get("/style.css")
async def serve_css():
    return FileResponse("style.css")

@app.get("/script.js")
async def serve_js():
    return FileResponse("script.js")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
