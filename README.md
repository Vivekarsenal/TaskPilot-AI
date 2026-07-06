# 🚀 TaskPilotAI – AI Todo List Generator

An AI-powered Multi-Agent Todo List Generator built using **FastAPI**, **LLMs**, and **python-docx**.

The system converts a natural language goal into a structured roadmap and exports it as a professional Microsoft Word document.

---

# ✨ Features

- Multi-Agent Architecture
- FastAPI REST API
- LLM-powered Parsing
- LLM-powered Planning
- Human-in-the-Loop Validation
- Request Validation & Guardrails
- Automatic Word (.docx) Generation
- Modular & Scalable Design

---

# 🏗 Architecture

<p align="center">
<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/46d1a9bd-127a-453f-be56-afea8b590937" />

</p>

The system follows a modular multi-agent workflow.

```
User
   │
   ▼
FastAPI
   │
   ▼
TodoService
   │
   ├──────────────► Parser Agent
   │                    │
   │                    ▼
   │           Parsed Instruction
   │                    │
   ▼                    ▼
Request Validation (Human-in-the-loop)

       Missing Information?
            │
      ┌─────┴─────┐
      │           │
     Yes          No
      │           │
      ▼           ▼
Return Questions  Planner Agent
                      │
                      ▼
              Task Roadmap
                      │
                      ▼
            Document Generator
                      │
                      ▼
               Word Document
```

---

# 📁 Project Structure

```
LumiAI
│
├── API
│   └── routes.py
│
├── Agents
│   ├── parser_agent.py
│   └── planner_agent.py
│
├── Prompts
│   ├── parser_prompt.py
│   └── planner_prompt.py
│
├── Services
│   ├── llm.py
│   ├── todo_service.py
│   └── document_service.py
│
├── Models
│   ├── request.py
│   ├── parsed_instruction.py
│   └── planner.py
│
├── output
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ Technologies Used

- Python 3.12
- FastAPI
- Groq API
- Llama 3
- Pydantic
- python-docx
- Uvicorn
- dotenv

---

# 🤖 Agent Workflow

## 1. Parser Agent

Responsible for understanding the user's instruction.

Extracts

- Goal
- Timeline
- Constraints
- Missing Information

Example

Input

```
I want to become a Java Backend Developer in 6 months.
```

Output

```json
{
    "goal":"Become Java Backend Developer",
    "timeline":"6 months",
    "constraints":[
    ],
    "missing_information":[]
}
```

---

## 2. Request Validation & Guardrails

Before moving to planning, the system validates whether enough information is available.

If important information is missing, the workflow stops immediately and asks the user for clarification.

Example

Input

```
Help
```

Output

```json
{
    "status":"needs_clarification",
    "questions":[
        "What is your goal?",
        "What timeline do you have?",
        "Do you have any constraints?"
    ]
}
```

This prevents the planner from making incorrect assumptions.

---

## 3. Planner Agent

Uses the parsed instruction to generate

- milestones
- roadmap
- priority
- task order

---

## 4. Document Generator

Automatically generates a professional Word document using

python-docx

The generated document contains

- Goal
- Timeline
- Tasks
- Priority
- Description

---

# 📦 API

## POST

```
/generate-todo
```

Body

```json
{
    "instruction":"Become Java Backend Developer in 6 months"
}
```

---

# Sample Successful Response

```json
{
  "parsed_instruction": {...},
  "planner_response": {...},
  "document":"output/todo_xxxxx.docx"
}
```

---

# Human-in-the-Loop Example

Request

```json
{
    "instruction":"Help"
}
```

Response

```json
{
    "status":"needs_clarification",
    "questions":[
        "What goal would you like to achieve?",
        "What timeline do you have?",
        "Any constraints?"
    ]
}
```

---

# Running the Project

Clone

```bash
git clone https://github.com/yourusername/TaskPilot.git
```

Install

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# Future Improvements

- Conversation Memory
- Reviewer Agent
- Retry Logic
- Tool Calling
- Web Search
- Calendar Integration
- RAG
- Authentication

---

# Author

**Vivek**

Built with ❤️ using FastAPI, Groq Llama, and Multi-Agent Architecture.
