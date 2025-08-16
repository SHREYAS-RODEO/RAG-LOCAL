# 📘 Moodle RAG Assistant

An **AI-powered Retrieval-Augmented Generation (RAG) assistant** integrated with **Moodle LMS** that can query both **unstructured data (PDF documents)** and **structured data (databases like students, teachers, grades, and attendance)**.  
Built with **Flask, LangChain, Ollama, and FAISS**, paired with a **modern TailwindCSS frontend**.

---

## ✨ Features
- 📂 **Upload PDFs** → Automatically processed and embedded into a **persistent FAISS vector store**.  
- 🧠 **Unstructured Querying** → Ask natural language questions on uploaded PDFs.  
- 📊 **Structured Querying** → Interact with SQLite databases (students, teachers, grades, attendance).  
- ⚡ **Dual Mode** → Choose between *structured (SQL agent)* or *unstructured (RAG)* queries.  
- 🎨 **Modern UI** → TailwindCSS-powered frontend with:
  - Light/Dark theme toggle  
  - Smooth animations  
  - Chat-style responses  
  - Query history  
  - Copy-to-clipboard feature  
- 🔒 **Local-first** → Runs with [Ollama](https://ollama.ai) for privacy and offline use.  

---

## 🗂️ Project Structure
moodle-rag-assistant/
├── backend/
│ ├── app.py # Flask API entrypoint
│ ├── config.py # Config: database mappings, table schemas
│ ├── create_databases.py # Script to generate SQLite databases
│ ├── document_loader.py # PDF loader and text extraction
│ ├── rag_engine.py # RAG pipeline (Ollama + FAISS retriever)
│ ├── sql_agent.py # SQL Agent for structured queries
│ ├── vector_store.py # Persistent FAISS index handling
│ └── requirements.txt # Python dependencies
└── frontend/
└── index.html # TailwindCSS + JS frontend


---

## ⚙️ Setup Instructions

 1. Clone the repository
```bash
git clone https://github.com/SHREYAS-RODEO/moodle-rag-assistant.git
cd moodle-rag-assistant

2. Backend Setup
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Start Ollama

Install Ollama and pull a model (e.g., mistral):

ollama pull mistral


👉 If Ollama runs on Windows host but backend is inside WSL:
Find your Windows IP:

cat /etc/resolv.conf | grep nameserver


Then export it:

export OLLAMA_BASE_URL=http://<windows-ip>:11434

4. Create Example Databases
python create_databases.py

5. Run the Backend
python app.py


Backend runs at: http://127.0.0.1:5000

🌐 Frontend

Open the frontend:

frontend/index.html


Features:

Upload PDFs

Choose query type (Structured DB / Unstructured PDF)

Chat-style assistant responses

Dark/light theme toggle

Copy answers & view query history

⚡ Example Usage
Upload & Query PDFs

Upload research_paper.pdf

Ask:

Summarize the key contributions of this paper.

Query Databases

Choose Structured Query → Select Grades

Ask:

Show all students with grades above 80.


Response will be generated via SQL agent.

📊 Tech Stack

Backend: Python, Flask, LangChain, FAISS, SQLite

LLM: Ollama (mistral by default, configurable)

Frontend: HTML, TailwindCSS, Vanilla JavaScript

Databases: SQLite (students, teachers, grades, attendance)

🔮 Future Roadmap

 Charts & tables rendering for structured responses

 Support multiple Ollama models (llama3, gemma, etc.)

 Multi-document management (upload + delete PDFs)

 Deployment on cloud VM with Ollama remote endpoint


##👨‍💻 Author

Shreyas S Acharya
Final-year Information Science Student @ NMIT

🌐 Cloud & AI Enthusiast

☁️ Certified in AWS & GCP

🤖 Projects in LLMs, RAG, Flutter, and Cloud DevOps

🏆 Hackathon Finalist (Namma Suraksha Hackathon)
