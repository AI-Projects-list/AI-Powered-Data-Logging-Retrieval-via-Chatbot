import React, { useState } from "react";

function Chatbot() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const sendQuery = async () => {
    const res = await fetch("http://localhost:5000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: input, engine: "ollama" }),
    });
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div>
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={sendQuery}>Ask</button>
      <p>{response}</p>
    </div>
  );
}

export default Chatbot;
