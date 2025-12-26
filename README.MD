Sairam AI – Advanced Personal Assistant

Sairam AI is a full-stack, responsive chatbot application featuring a modern glassmorphic user interface and a robust Python Flask backend powered by the Gemini 2.0 model. It delivers a smooth, professional AI chat experience similar to ChatGPT or Gemini.

1. Project Overview

The application supports multiple conversations, persistent chat history, and light/dark theme switching. AI responses are displayed in a clean, readable format without distracting markdown symbols, ensuring a professional user experience.

2. Frontend Architecture (HTML, CSS, JavaScript)
A. User Interface (UI)

Sidebar System: Manages conversation history with toggle support.

Theme Engine: Uses CSS variables (:root) for Dark and Light modes.

Adaptive Input Box: Automatically expands for multi-line input.

Glassmorphism Design: Implemented using backdrop-filter: blur() and semi-transparent borders.

B. Logic & State Management

Local Storage: Saves chat history and theme preferences.

Response Formatting: JavaScript with Regex is used to:

Remove symbols like ** or ***

Convert line breaks into paragraphs

Detect bullet points and render them using <ul> and <li>

3. Backend Architecture (Python Flask)
Workflow

Frontend sends a POST request to /chat

Flask processes the message and connects to Gemini

AI response is returned as JSON: { "reply": "..." }

4. Running the Project
Backend Setup
pip install flask
python app.py

Frontend Setup

Place index.html inside the templates folder.

Access Application

Open: http://127.0.0.1:8080/


Author : NAKKA LEELA LAKSHMI SAI RAM
EMAIL  : nleelasairamanakka@gmail.com
GITHUB : https://github.com/sairam-900
