# HR Assistant (Local LLM Chatbot)

## 📌 Overview  
This is a **local HR Assistant chatbot** designed to help employees quickly find answers to HR-related questions such as leave policies, benefits, and company information.  

It uses a **Python Flask backend**, an **HTML + JavaScript frontend**, and a **local LLM** (e.g., Ollama’s Llama3 or Gemma models) for natural language understanding.  

Employees can ask questions like:  
- *“How many sick leaves do I get?”*  
- *“What are the paid leave policies?”*  
- *“How can I apply for a benefit?”*  

---

## 🚀 Key Features  
- **Local AI Assistant** – No external API calls (optional OpenAI API integration available).  
- **HR Policy Storage** – Policies stored in `policies/` folder as text files.  
- **Vector Search** – Uses SentenceTransformers (`all-MiniLM-L6-v2`) + FAISS for efficient policy lookup.  
- **Chat-Style Frontend** – Clean and user-friendly interface.  
- **Supported Queries** – Handles casual leave, paid leave, sick leave, and benefits.  
- **Optional LLM Integration** – Enhances responses using local LLMs (Llama3, Gemma).  

---

## ⚠️ Limitations  
- Requires sufficient **RAM** to run local LLM models.  
- Answers limited to data inside the `policies/` folder.  
- `vector_store.pkl` (FAISS index) auto-generates on first run if missing.  

---

## 🛠 Tools & Libraries  
- Python 3.x  
- Flask  
- SentenceTransformers (`all-MiniLM-L6-v2`)  
- FAISS  
- Ollama (for local LLM)  
- HTML, CSS, JavaScript (frontend)  

---

## 📂 Project Structure  

HR-Assistant-Local-LLM/
│
├── app.py # Flask backend
├── .gitignore # Ignore large files
├── vector_store.pkl # FAISS index (generated locally)
├── policies/ # HR policy text files
│ ├── leave_policy.txt
│ └── benefits.txt
└── static/
├── index.html # Frontend HTML
└── app.js # JavaScript for chat functionality

yaml
Copy code

---

## ⚙️ Setup Instructions  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/HR-Assistant-Local-LLM.git
cd HR-Assistant-Local-LLM
2. Create Virtual Environment
bash
Copy code
python -m venv hrv
source hrv/bin/activate   # Mac/Linux
hrv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install flask sentence-transformers faiss-cpu
4. Install Ollama & Pull LLM Model
Install Ollama → Ollama Docs

Pull a model (example with Llama3):

bash
Copy code
ollama pull llama3
# or
ollama pull gemma:2b
5. Run the Application
bash
Copy code
python app.py
6. Open in Browser
Navigate to → http://127.0.0.1:5000

💻 Usage
Type HR-related questions in the chatbox.

Chatbot fetches policies from the policies/ folder using vector search.

Local LLM improves natural language answers.

📸 Example Screenshots


🤝 Contributing
Contributions are welcome! Please fork this repo and submit a pull request.
