"""
Simple RAG Engine using sentence-transformers and FAISS for vector similarity search.
This implementation answers questions based ONLY on provided sustainability documents.
"""

import os
from typing import List, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

class RAGEngine:
    def __init__(self, documents_path="documents"):
        """Initialize the RAG engine with document path."""
        self.documents_path = documents_path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight model
        self.documents = []
        self.document_names = []
        self.embeddings = None
        self.index = None
        
    def load_documents(self):
        """Load all documents from the documents folder."""
        if not os.path.exists(self.documents_path):
            os.makedirs(self.documents_path)
            print(f"📁 Created documents folder at: {self.documents_path}")
            print("⚠️ Please add sustainability policy documents (.txt files) to this folder!")
            return
        
        # Load all .txt files from documents folder
        txt_files = [f for f in os.listdir(self.documents_path) if f.endswith('.txt')]
        
        if not txt_files:
            print("⚠️ No documents found! Please add .txt files to the documents folder.")
            return
        
        print(f"📚 Loading {len(txt_files)} document(s)...")
        
        for filename in txt_files:
            filepath = os.path.join(self.documents_path, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Split into chunks (simple chunking by paragraphs)
                    chunks = self._chunk_text(content)
                    for chunk in chunks:
                        self.documents.append(chunk)
                        self.document_names.append(filename)
                print(f"✅ Loaded: {filename} ({len(chunks)} chunks)")
            except Exception as e:
                print(f"❌ Error loading {filename}: {e}")
        
        if self.documents:
            self._create_index()
            print(f"✅ RAG Engine initialized with {len(self.documents)} text chunks")
        else:
            print("⚠️ No content loaded!")
    
    def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        """Split text into smaller chunks for better retrieval."""
        # Simple chunking by character count with overlap
        chunks = []
        words = text.split()
        current_chunk = []
        current_length = 0
        
        for word in words:
            current_chunk.append(word)
            current_length += len(word) + 1
            
            if current_length >= chunk_size:
                chunks.append(' '.join(current_chunk))
                # Overlap: keep last 50 words
                current_chunk = current_chunk[-50:] if len(current_chunk) > 50 else current_chunk
                current_length = sum(len(w) + 1 for w in current_chunk)
        
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def _create_index(self):
        """Create FAISS index from document embeddings."""
        print("🔄 Creating embeddings...")
        self.embeddings = self.model.encode(self.documents, show_progress_bar=True)
        
        # Create FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings.astype('float32'))
        print("✅ FAISS index created!")
    
    def get_answer(self, question: str, top_k: int = 3) -> Tuple[str, List[str]]:
        """
        Get answer to a question based on document retrieval.
        Returns: (answer, list of source documents)
        """
        if not self.documents:
            return "I don't have any documents loaded to answer your question. Please add sustainability policy documents to the documents folder.", []
        
        # Encode the question
        question_embedding = self.model.encode([question])
        
        # Search for most similar documents
        distances, indices = self.index.search(question_embedding.astype('float32'), top_k)
        
        # Get relevant document chunks
        relevant_chunks = []
        sources = set()
        
        for idx in indices[0]:
            if idx < len(self.documents):
                relevant_chunks.append(self.documents[idx])
                sources.add(self.document_names[idx])
        
        # Create answer from retrieved chunks
        if not relevant_chunks:
            return "I couldn't find relevant information in the available documents.", []
        
        # Simple answer generation: return the most relevant chunk
        # In a full implementation, you would use an LLM to synthesize an answer
        answer = self._generate_simple_answer(question, relevant_chunks)
        
        return answer, list(sources)
    
    def _generate_simple_answer(self, question: str, chunks: List[str]) -> str:
        """
        Generate a simple answer from retrieved chunks.
        Note: This is a basic implementation. For production, use an LLM (OpenAI, etc.)
        """
        # For this simple version, return the most relevant chunk with context
        answer = (
            "Based on the available policy documents:\n\n"
            f"{chunks[0][:600]}..."
            if len(chunks[0]) > 600 else chunks[0]
        )
        
        if len(chunks) > 1:
            answer += f"\n\nAdditional relevant information was found in {len(chunks)-1} more section(s)."
        
        return answer
    
    def get_document_list(self) -> List[str]:
        """Return list of unique document names."""
        return list(set(self.document_names))

