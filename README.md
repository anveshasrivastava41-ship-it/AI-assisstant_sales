# 🤖 AI Sales Assistant (ServiceHive Internship Assignment)

## 📌 Overview

This project was developed as part of the ServiceHive Machine Learning Internship assignment.

It simulates a real-world AI-driven SaaS sales agent that can:

* Understand user intent
* Answer product queries using a knowledge base (RAG)
* Identify high-intent users
* Capture leads via a structured workflow

---

## 🚀 Features

### 🧠 Intent Detection

Classifies user inputs into:

* Greeting
* Product inquiry (pricing, features, policies)
* High-intent (demo / purchase)

---

### 📚 RAG (Retrieval-Augmented Generation)

Product information is stored in a local JSON file (`knowledge.json`) and dynamically used to generate responses.

Includes:

* Pricing plans
* Features
* Company policies

---

### 🤖 Conversational Agent Flow

The assistant:

* Responds to queries
* Guides users toward conversion
* Suggests next steps (e.g., demo CTA)

---

### 🧾 Lead Capture Workflow

For high-intent users:

1. Collect Name
2. Collect Email
3. Collect Platform

Then triggers:

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

---

### 💬 Modern Chat UI

* ChatGPT-style interface (Streamlit)
* Persistent chat history
* Interactive conversation flow

---

## 🧱 Tech Stack

* Python
* Streamlit
* JSON (knowledge base)
* Session State (memory)

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd servicehive-assignment
pip install streamlit
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧪 Example Flow

1. User: "Hi"

2. Bot: Greeting

3. User: "What is pricing?"

4. Bot: Returns pricing + asks for demo

5. User: "Yes"

6. Bot: Initiates lead capture

7. User provides details →

8. Tool executes (mock_lead_capture)

---

## 🧠 System Architecture

Pipeline:

1. User Input
2. Intent Detection (rule-based)
3. Knowledge Retrieval (JSON-based RAG)
4. Response Generation
5. Action Trigger (Lead Capture Tool)

---

## 💡 Key Design Decisions

* Used rule-based intent detection for deterministic control
* Implemented JSON-based RAG instead of vector DB for simplicity
* Designed system to be LLM-agnostic (plug-and-play APIs)
* Focused on reliability and structured workflow

---

## 🔧 LLM Integration Note

Due to API quota constraints, the system currently uses a rule-based response engine.

However, the architecture is fully compatible with LLM integration (OpenAI, Gemini, Claude) and can be extended easily.

---

## 📈 Future Improvements

* Add LLM-based response generation
* Integrate FAISS or vector DB for advanced RAG
* Improve intent classification using ML models
* Add analytics dashboard for leads
* Deploy on cloud / WhatsApp integration

---

## 📲 WhatsApp Integration (Design)

This system can be integrated with WhatsApp using:

1. Webhook to receive messages
2. Backend server (Flask/FastAPI)
3. Process input → run agent
4. Send response back via WhatsApp API

---

## 🎯 Conclusion

This project demonstrates a real-world AI agent capable of:

* Understanding user intent
* Answering context-based queries
* Driving conversions
* Capturing leads

It reflects how modern AI systems are used in SaaS sales automation.

---
