# 🦜🔗 LangSmith Learning Journey

> A structured, hands-on progression through the LangChain ecosystem — from a single LLM call all the way to stateful multi-agent workflows with LangGraph.

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green?logo=chainlink)](https://www.langchain.com/)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.6.4-orange)](https://langchain-ai.github.io/langgraph/)
[![LangSmith](https://img.shields.io/badge/LangSmith-0.4.13-purple)](https://smith.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-lightgrey?logo=openai)](https://openai.com/)

---

## 📚 What This Repo Is

This repository documents my learning path through **LangChain**, **LangGraph**, and **LangSmith** — building progressively more complex AI systems step by step. Each numbered file is a self-contained lesson that builds on the previous one.

The progression follows this arc:

```
Simple LLM Call → Sequential Chains → RAG (v1→v4) → Agents → LangGraph
```

---

## 🗂️ File Structure

```
langsmith/
├── 1_simple_llm_call.py      # Lesson 1: Basic LLM chain with PromptTemplate
├── 2_sequential_chain.py     # Lesson 2: Multi-step sequential chains (LCEL)
├── 3_rag_v1.py               # Lesson 3a: RAG - naive retrieval baseline
├── 3_rag_v2.py               # Lesson 3b: RAG - improved chunking & embeddings
├── 3_rag_v3.py               # Lesson 3c: RAG - FAISS vector store + retriever
├── 3_rag_v4.py               # Lesson 3d: RAG - conversational memory + history
├── 4_agent.py                # Lesson 4: ReAct agent with DuckDuckGo + tools
├── 5_langgraph.py            # Lesson 5: Stateful graph-based agent (LangGraph)
├── islr.pdf                  # Knowledge base: Introduction to Statistical Learning
├── requirements.txt          # All dependencies (pinned)
└── .gitignore
```

---

## 🧭 Lesson Breakdown

### 1️⃣ `1_simple_llm_call.py` — Simple LLM Call
The foundation. Builds a minimal chain using LangChain Expression Language (LCEL):

```
PromptTemplate → ChatOpenAI → StrOutputParser
```

**Concepts:** `PromptTemplate`, `ChatOpenAI`, `StrOutputParser`, pipe operator (`|`), `.invoke()`

---

### 2️⃣ `2_sequential_chain.py` — Sequential Chains
Chains multiple LLM steps together so the output of one becomes the input of the next.

**Concepts:** Multi-step LCEL chains, prompt composition, chaining transforms

---

### 3️⃣ `3_rag_v1.py` → `3_rag_v4.py` — Retrieval-Augmented Generation (RAG)

A four-version deep dive into RAG using **`islr.pdf`** (Introduction to Statistical Learning) as the knowledge source.

| Version | What's new |
|---------|-----------|
| `v1` | Naive RAG — load PDF, split, embed, query |
| `v2` | Better chunking strategy, improved retrieval quality |
| `v3` | FAISS vector store, persistent index, similarity search |
| `v4` | Conversational RAG with chat history & memory |

**Concepts:** `PyPDFLoader`, `RecursiveCharacterTextSplitter`, `OpenAIEmbeddings`, `FAISS`, `RetrievalQA`, `ConversationalRetrievalChain`

---

### 4️⃣ `4_agent.py` — ReAct Agent with Tools
An autonomous agent that decides which tools to call based on the query — including live web search.

**Tools used:**
- 🔍 `DuckDuckGoSearchRun` — real-time web search
- 📺 `YouTubeTranscriptTool` — fetch and query YouTube transcripts

**Concepts:** `create_react_agent`, tool binding, agent executor, tool schemas

---

### 5️⃣ `5_langgraph.py` — Stateful Agent with LangGraph
The most advanced lesson. Builds a graph-based agent with **persistent state**, **conditional edges**, and **SQLite checkpointing** using LangGraph.

```
[User Input] → [Agent Node] → (tool needed?) → [Tool Node] → [Agent Node] → [Output]
                                     ↓ no
                                  [END]
```

**Concepts:** `StateGraph`, `ToolNode`, `MessagesState`, conditional edges, `SqliteSaver` checkpointer, streaming

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/codeantik/langsmith.git
cd langsmith
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root:
```env
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langsmith-learning
```

> Get your LangSmith API key at [smith.langchain.com](https://smith.langchain.com)

---

## ▶️ Running the Scripts

```bash
# Run any lesson individually
python 1_simple_llm_call.py
python 2_sequential_chain.py
python 3_rag_v1.py
python 4_agent.py
python 5_langgraph.py
```

---

## 🔑 Key Dependencies

| Package | Purpose |
|---------|---------|
| `langchain` | Core chains, prompts, output parsers |
| `langchain-openai` | OpenAI model integration |
| `langchain-community` | Community tools (DuckDuckGo, YouTube, etc.) |
| `langgraph` | Stateful agent graphs |
| `langsmith` | Tracing, evaluation, observability |
| `faiss-cpu` | Vector similarity search |
| `pypdf` | PDF loading for RAG |
| `openai` | Direct OpenAI API client |
| `python-dotenv` | Environment variable management |
| `streamlit` | (Optional) interactive UI |

---

## 🔭 Observability with LangSmith

All chains and agents are automatically traced in **LangSmith** when `LANGCHAIN_TRACING_V2=true` is set. This gives you:

- Full run traces (inputs, outputs, latency)
- Token usage per step
- Error debugging
- Prompt evaluation and comparison

View your traces at → [smith.langchain.com](https://smith.langchain.com)

---

## 🗺️ Learning Roadmap

- [x] Simple LLM calls with LCEL
- [x] Sequential chains
- [x] RAG pipeline (v1 → v4)
- [x] ReAct agents with tools
- [x] Stateful graphs with LangGraph
- [ ] Multi-agent systems
- [ ] Human-in-the-loop workflows
- [ ] LangGraph Studio integration
- [ ] Custom evaluators in LangSmith

---

## 👨‍💻 Author

**Ankit Singh** — Full Stack Developer & Agentic AI Specialist

[![GitHub](https://img.shields.io/badge/GitHub-codeantik-black?logo=github)](https://github.com/codeantik)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ankit_Singh-blue?logo=linkedin)](https://linkedin.com/in/codeantik)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
