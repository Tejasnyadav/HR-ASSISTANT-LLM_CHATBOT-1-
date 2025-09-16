from flask import Flask, request, jsonify, send_from_directory
from sentence_transformers import SentenceTransformer
import faiss, os, pickle, subprocess

app = Flask(__name__, static_folder="static")

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Paths
POLICY_DIR = "policies"
INDEX_FILE = "vector_store.pkl"

# Load or build vector index
if os.path.exists(INDEX_FILE):
    with open(INDEX_FILE, "rb") as f:
        index, texts = pickle.load(f)
else:
    texts = []
    for fname in os.listdir(POLICY_DIR):
        if fname.endswith(".txt"):
            with open(os.path.join(POLICY_DIR, fname), "r", encoding="utf-8") as f:
                texts.append(f.read())
    embeddings = embedder.encode(texts, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    with open(INDEX_FILE, "wb") as f:
        pickle.dump((index, texts), f)

# Function to call Ollama
def ask_ollama(prompt: str) -> str:
    cmd = ["ollama", "run", "llama3", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()

@app.route("/ask", methods=["POST"])
def ask():
    q = request.json.get("q", "")
    if not q:
        return jsonify({"answer": "Please ask a question."})

    # Find best policy chunk
    q_embed = embedder.encode([q], convert_to_numpy=True)
    D, I = index.search(q_embed, 1)  # top 1 match
    best = texts[I[0][0]]

    # Prompt for LLM
    prompt = f"""
You are an HR Assistant. Use the following HR policies to answer clearly and politely:

{best}

Question: {q}
Answer:
"""
    answer = ask_ollama(prompt)

    return jsonify({"answer": answer})

# Route to serve frontend
@app.route("/")
def serve_index():
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
