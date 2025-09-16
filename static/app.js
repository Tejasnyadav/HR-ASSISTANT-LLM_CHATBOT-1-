const chat = document.getElementById("chat");
const input = document.getElementById("q");
const btn = document.getElementById("askBtn");

function addMessage(sender, text) {
  const p = document.createElement("p");
  p.className = sender;
  p.textContent = (sender === "user" ? "You: " : "HR Assistant: ") + text;
  chat.appendChild(p);
  chat.scrollTop = chat.scrollHeight;
}

btn.onclick = async () => {
  const q = input.value.trim();
  if (!q) return;
  addMessage("user", q);
  input.value = "";

  const r = await fetch("/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ q })
  });

  const data = await r.json();
  addMessage("bot", data.answer);
};
