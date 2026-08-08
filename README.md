<div align="center">

# ⚖️ LegalBot

### Police, FIR, Arrest & Bail Assistant

**AI-powered legal information assistant focused on Police, FIR, Arrest & Bail matters in India.**

<img src="https://github.com/Clestialcosmos/LegalBot/blob/main/picture1" alt="LegalBot Prototype" width="900">

</div>

---

## 📖 Table of Contents

- [Project Focus](#-project-focus)
- [Why This Segment?](#-why-this-segment)
- [Selected Legal Scope](#️-selected-legal-scope)
- [Features](#-planned--target-features)
- [RAG Architecture](#-rag-architecture)
- [Query Flow](#-query-flow)
- [Technology Stack](#️-technology-stack)
- [Prototype](#️-prototype)
- [Example Questions](#-example-questions)
- [API](#-api)
- [Local Setup](#-local-setup)
- [Docker](#-docker)
- [Deployment Architecture](#-deployment-architecture)
- [Project Structure](#-project-structure)
- [Legal & Safety Boundaries](#-legal--safety-boundaries)
- [Knowledge Base Direction](#-knowledge-base-direction)
- [Project Outcome](#-project-outcome)
- [Future Scope](#-future-scope)
- [Disclaimer](#️-disclaimer)
- [Project Identity](#-project-identity)

---

## 🎯 Project Focus

LegalBot is specifically focused on the **Police, FIR, Arrest & Bail** segment. The project is designed to help people understand their basic rights and the correct procedural next steps when dealing with:

- Police stations
- FIR registration
- Police refusal to register an FIR
- Arrest and search
- Bail
- Default bail
- Old IPC/CrPC references versus the current BNS/BNSS framework
- Access to free legal assistance through DLSA

The project specification identifies this area as a major source of confusion because people may be afraid of police stations, families of arrested persons can be exploited by touts, and online information can contain outdated IPC/CrPC section numbers after the 2023 criminal-law transition.

---

## 💡 Why This Segment?

Police, FIR, arrest and bail procedures can be intimidating for ordinary citizens. A user may not know:

- Whether an FIR should be registered
- What to do if the police refuse to register an FIR
- What basic rights apply at a police station
- What safeguards apply during arrest or search
- What bail means and what types of bail may apply
- How older IPC/CrPC references correspond to BNS/BNSS
- Where to find free legal assistance

LegalBot is intended to turn this confusion into a simple, structured explanation and guide the user toward appropriate official or human legal support.

---

## 🧑‍⚖️ Selected Legal Scope

**Selected legal domain:** Police, FIR, Arrest & Bail

**Core legal framework:**

| Current Framework | Successor To |
|---|---|
| Bharatiya Nyaya Sanhita (BNS), 2023 | Indian Penal Code (IPC) |
| Bharatiya Nagarik Suraksha Sanhita (BNSS), 2023 | Code of Criminal Procedure (CrPC) |
| Bharatiya Sakshya Adhiniyam (BSA), 2023 | Indian Evidence Act |

**Additional safeguards referenced:**
- D.K. Basu safeguards
- Arnesh Kumar safeguards

---

## 🚀 Planned / Target Features

### 1. Know Your Rights
Simple cards explaining rights and safeguards related to:
- Police stations
- Arrest
- Search
- FIR-related procedures

### 2. FIR Assistance
Helps users understand:
- What an FIR is
- When FIR registration may be relevant
- What information is generally needed
- What steps can be taken when registration is refused

### 3. FIR Refusal Escalation
If a user reports that police have refused to register an FIR, LegalBot can guide them toward the documented escalation pathway, including:
- Superintendent of Police (SP)
- Magistrate

The system may also assist with preparing a draft refusal-escalation letter.

### 4. IPC ↔ BNS Converter
A major feature for this project is helping users understand the transition between:

```
IPC 2023-era references
        ↓
BNS 2023 framework
```

This is important because older legal information on the internet may still use IPC terminology.

### 5. CrPC ↔ BNSS Converter

```
CrPC references
        ↓
BNSS 2023 framework
```

This helps reduce confusion when users encounter older articles, documents, or legal explanations.

### 6. Arrest & Search Rights
Explains relevant safeguards in simple language rather than presenting raw legal text without context.

### 7. Bail Explainer
Includes explanations around bail, helping users understand relevant bail concepts and procedures.

### 8. DLSA Routing
Where appropriate, LegalBot points users toward District Legal Services Authorities (DLSA) for access to human legal assistance.

---

## 🤖 RAG Architecture

LegalBot is designed as a **Retrieval-Augmented Generation (RAG)** system.

A general-purpose LLM can hallucinate statutes, section numbers, or procedures — particularly risky for a legal application. The intended architecture therefore retrieves relevant legal material first, then generates a plain-language response grounded in that retrieved information.

```
                    USER
                      │
                      ▼
              ┌──────────────┐
              │ React Frontend│
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │ FastAPI API  │
              └──────┬───────┘
                     │
                     ▼
             ┌─────────────────┐
             │ Query Processing│
             └────────┬────────┘
                      │
                      ▼
            ┌────────────────────┐
            │ Hybrid Retrieval   │
            │ Semantic + Keyword │
            └─────────┬──────────┘
                      │
                      ▼
                ┌──────────┐
                │ Reranker │
                └────┬─────┘
                     │
                     ▼
             ┌────────────────┐
             │ Legal Context  │
             └───────┬────────┘
                     │
                     ▼
              ┌──────────────┐
              │ LLM / Groq   │
              └──────┬───────┘
                     │
                     ▼
             Grounded Response
             + Disclaimer
             + Sources
```

---

## 🔄 Query Flow

```
User Question
     │
     ▼
Intent / Domain Understanding
     │
     ▼
Safety Check
     │
     ▼
Hybrid Retrieval
     │
     ├── Semantic Search
     │
     └── Keyword Search
     │
     ▼
Reranking
     │
     ▼
Relevant Legal Information
     │
     ▼
LLM Generation
     │
     ▼
Plain-language Answer
     │
     ▼
Sources + Disclaimer
```

---

## 🛠️ Technology Stack

<table>
<tr>
<td valign="top" width="25%">

**Frontend**
- React 19
- Vite
- Tailwind CSS
- Axios
- React Icons

</td>
<td valign="top" width="25%">

**Backend**
- Python
- FastAPI
- Uvicorn
- Pydantic Settings

</td>
<td valign="top" width="25%">

**AI / RAG**
- Retrieval-Augmented Generation
- Semantic retrieval
- Keyword retrieval
- Hybrid retrieval
- Reranking
- LLM-based response generation
- Legal knowledge base

</td>
<td valign="top" width="25%">

**Infrastructure**
- Docker
- Railway
- GitHub
- Web deployment

</td>
</tr>
</table>

---

## 🖥️ Prototype

The prototype provides a conversational LegalBot interface with:

- LegalBot branding
- AI-powered legal assistant introduction
- Suggested legal questions
- Chat-based interaction
- Responsive web interface
- Purple/white visual design

<p align="center">
  <img src="https://github.com/Clestialcosmos/LegalBot/blob/main/picture2" alt="LegalBot Prototype" width="900">
</p>

---

## 💬 Example Questions

The interface can be designed around questions directly relevant to this selected segment:

1. What is an FIR?
2. What should I do if police refuse to register my FIR?
3. What are my rights during a police arrest?
4. What are my rights during a police search?
5. What is the difference between FIR and complaint?
6. What is bail?
7. What is default bail?
8. What is the difference between IPC and BNS?
9. What is the difference between CrPC and BNSS?
10. How can I get legal help through DLSA?

---

## 🔌 API

The frontend communicates with the FastAPI backend through HTTP/JSON.

**Example chat request**

```http
POST /api/v1/chat
Content-Type: application/json

{
  "message": "What are my rights during police arrest?"
}
```

The backend processes the query through the application's RAG/LLM pipeline and returns the response consumed by the frontend.

**Root Endpoint**

```http
GET /
```

Example response:

```json
{
  "success": true,
  "message": "Welcome to LegalBot API",
  "data": null
}
```

---

## 🚀 Local Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

**Frontend environment variable**

Create `frontend/.env` and configure:

```env
VITE_API_URL=http://127.0.0.1:8000
```

For production, point this variable to the deployed backend URL.

---

## 🐳 Docker

The backend can be containerized with Docker.

```bash
# Build
docker build -t legalbot-backend .

# Run
docker run -p 8000:8000 legalbot-backend
```

The production container runs FastAPI through Uvicorn on port 8000.

---

## 🌐 Deployment Architecture

```
┌───────────────────────┐
│     User Browser      │
│   Desktop / Mobile    │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    React Frontend     │
│     Web Deployment    │
└───────────┬───────────┘
            │ HTTPS
            ▼
┌───────────────────────┐
│   Railway Backend     │
│ FastAPI + Uvicorn     │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│      RAG Pipeline     │
│ Retrieval + Reranking │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│      LLM / Groq       │
└───────────────────────┘
```

---

## 📁 Project Structure

```
LegalBot/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   ├── config/
│   │   ├── schemas/
│   │   └── main.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.*
│
├── data/
│   └── legal knowledge base
│
├── assets/
│   └── prototype.png
│
└── README.md
```

---

## 🔐 Legal & Safety Boundaries

LegalBot is an information and guidance system, **not a replacement for a qualified advocate**. The project should:

- Explain legal concepts in plain language
- Ground answers in retrieved legal information
- Avoid inventing section numbers
- Clearly distinguish general information from professional legal advice
- Route high-stakes matters toward appropriate human legal support
- Treat generated FIR/complaint/bail-related documents as drafts requiring review
- Avoid assisting illegal activity or evasion of law enforcement

For the criminal-law domain, the system should be particularly careful about the IPC → BNS and CrPC → BNSS transition.

---

## 📚 Knowledge Base Direction

The project's broader architecture describes a knowledge base built from verified legal material such as:

- Statutes
- Rules
- Government guidance
- Legal-service resources
- Curated FAQs

For this selected segment, the knowledge base should prioritize authoritative material relevant to:

- BNS
- BNSS
- BSA
- FIR procedures
- Arrest safeguards
- Search safeguards
- Bail
- D.K. Basu safeguards
- Arnesh Kumar safeguards
- DLSA / legal-aid routing

---

## 🎯 Project Outcome

The goal is not simply to create another chatbot. The goal is to build a specialized LegalTech assistant for Police, FIR, Arrest & Bail issues that can:

> **Understand the user's situation → retrieve relevant law → explain it simply → guide the next step → connect the user to appropriate human/legal support.**

---

## 🔮 Future Scope

- IPC ↔ BNS automated mapping
- CrPC ↔ BNSS automated mapping
- Section-level legal retrieval
- FIR drafting assistance
- FIR refusal escalation letter generation
- Bail procedure explainers
- Arrest/search rights cards
- DLSA location-based routing
- Hindi and other Indian-language support
- Voice-based interaction
- Better citation verification
- Legal-document upload and retrieval
- Evaluation datasets for legal RAG accuracy

---

## ⚠️ Disclaimer

LegalBot provides general legal information and procedural guidance. **It does not constitute legal advice** and does not replace a qualified advocate or competent legal authority. For urgent or high-stakes matters, users should seek appropriate professional or official assistance.

---

## ⭐ Project Identity

| | |
|---|---|
| **Project** | LegalBot |
| **Domain** | LegalTech / Generative AI / RAG |
| **Selected Segment** | Police, FIR, Arrest & Bail |
| **Frontend** | React + Vite + Tailwind CSS |
| **Backend** | FastAPI + Python |
| **Deployment** | Railway + Web Frontend |
| **AI Approach** | Retrieval-Augmented Generation |

<div align="center">

*Making Indian legal procedures easier to understand — especially when dealing with the police, FIRs, arrest and bail.*

</div>
