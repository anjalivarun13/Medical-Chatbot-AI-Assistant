# 🩺 Medical Chatbot AI Assistant

An AI-powered healthcare assistant built using **Retrieval-Augmented Generation (RAG)** that delivers context-aware responses to medical queries by combining semantic search with Large Language Models (LLMs).

The system utilizes **Google Gemini**, **LangChain**, **Pinecone Vector Database**, and **Hugging Face Embeddings** to retrieve relevant medical knowledge from a trusted reference source before generating responses.

---

## 📌 Project Objective

Traditional LLMs may generate inaccurate or hallucinated responses when answering domain-specific questions. This project addresses that challenge by implementing a **Retrieval-Augmented Generation (RAG)** pipeline that grounds responses in verified medical literature.

The chatbot retrieves relevant information from **The Gale Encyclopedia of Medicine (Second Edition)** and uses the retrieved context to generate informative and reliable answers.

---

## 🚀 Key Features

- Retrieval-Augmented Generation (RAG) Architecture
- Medical Knowledge Base Search
- Context-Aware Question Answering
- Semantic Similarity Search using Vector Embeddings
- Google Gemini Powered Response Generation
- Interactive Streamlit User Interface
- Real-Time Medical Query Processing
- Secure API Key Management
- Cloud Deployment Ready

---

## 🏗️ System Architecture

```text
Medical PDF Documents
          │
          ▼
Document Processing
          │
          ▼
Text Chunking
          │
          ▼
Sentence Transformer Embeddings
          │
          ▼
Pinecone Vector Database
          │
          ▼
Relevant Context Retrieval
          │
          ▼
Google Gemini LLM
          │
          ▼
Medical Response Generation
          │
          ▼
Streamlit User Interface
```

---

## 📸 Application Screenshots

### Home Page
![Home Page](https://github.com/anjalivarun13/Medical-Chatbot-AI-Assistant/blob/main/Screenshot/SS1.jpeg)

### Chat Interface
![Chat Interface](https://github.com/anjalivarun13/Medical-Chatbot-AI-Assistant/blob/main/Screenshot/SS2.jpeg)

### Medical Query Example
![Medical Query Example](https://github.com/anjalivarun13/Medical-Chatbot-AI-Assistant/blob/main/Screenshot/SS3.jpeg)

---

## 🔄 RAG Workflow

1. Load medical reference PDFs.
2. Extract textual content.
3. Split documents into manageable chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in Pinecone Vector Database.
6. User submits a medical question.
7. Similar medical content is retrieved from Pinecone.
8. Retrieved context is passed to Gemini.
9. Gemini generates a context-grounded response.
10. Response is displayed through the Streamlit interface.

---

## 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini |
| Framework | LangChain |
| Embeddings | Hugging Face Sentence Transformers |
| Vector Database | Pinecone |
| Deployment | Streamlit Cloud |

---

## 🎥 Live Demo

### Web Application
![Web Application](https://ai-medical-chatbot-assistant.streamlit.app/)

### Video Demonstration
![Video Demo](https://drive.google.com/file/d/1tgH4nZ-ftKlZ4v1DDq0BGFI0OdVETUAr/view?usp=sharing)

---

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/anjalivarun13/Medical-Chatbot-AI-Assistant.git
cd Medical-Chatbot-AI-Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

```env
PINECONE_API_KEY=YOUR_PINECONE_API_KEY
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📈 Skills Demonstrated

- Generative AI Applications
- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Databases
- Semantic Search
- Prompt Engineering
- Embedding Models
- LangChain Framework
- End-to-End AI Application Development
- Cloud Deployment

---

## 🔮 Future Enhancements

- Multi-Model Support (Gemini, GPT, Claude)
- Voice-Based Medical Queries
- Conversation History Export
- Multi-Language Support
- Advanced Citation-Based Responses
- Medical Source Attribution

---

## ⚠️ Disclaimer

This application is intended solely for educational and informational purposes. It is not designed to provide medical diagnosis, treatment recommendations, or professional healthcare advice. Users should consult qualified healthcare professionals regarding medical concerns.

---

## 🙏 Acknowledgements

- The Gale Encyclopedia of Medicine (Second Edition)
- LangChain
- Pinecone
- Google Gemini
- Hugging Face
- Streamlit

---

## 👩‍💻 Author

**Anjali Varun**

**GitHub**: https://github.com/anjalivarun13

**LinkedIn:**: https://www.linkedin.com/in/anjali-varun/

If you found this project useful, consider giving the repository a ⭐.
