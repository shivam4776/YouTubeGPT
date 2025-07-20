# 🎥 YouTube Video QA System using RAG (Retrieval-Augmented Generation)                            --YouTubeGPT

This is a Retrieval-Augmented Generation (RAG) based system that allows users to interact with YouTube videos in a more intelligent way.
An intelligent, Streamlit-powered app that summarizes YouTube videos using their transcripts with RAG (Retrieval-Augmented Generation).
By simply providing a YouTube link, the system extracts the video transcript, breaks it down into meaningful chunks, and enables users to ask questions or request summaries — powered by embeddings and a large language model (LLM).

---

## 🧠 What the System Does

1. **Takes a YouTube Link** from the user via a **Streamlit UI**
2. **Fetches the Transcript** of the video using the `youtube-transcript-api`
3. **Chunks the Transcript** into overlapping segments for better context capture
4. **Embeds the Chunks** using a sentence embedding model (e.g., OpenAI or SentenceTransformers)
5. **Stores Embeddings** in a vector database (e.g., FAISS or Chroma)
6. **Handles Natural Language Queries** by the user about the video content
7. **Retrieves the Most Relevant Chunks** using vector similarity
8. **Generates an Answer or Summary** using an LLM (like GPT-4), grounded in the retrieved context

---

## ✨ Key Features

* 🎯 Semantic search over video transcripts
* 💬 Context-aware Q\&A based on transcript chunks
* 📄 Summary generation using relevant parts of the video
* 🖥️ Interactive front-end built with **Streamlit**
* 📦 Fully modular design with retriever, chunking, and summarization components

---
## 🖼️ Example YouTube Video

<img width="268" height="84" alt="image" src="https://github.com/user-attachments/assets/41ba9c04-33e3-4400-bbaf-80721e0f6191" />

---

## 🖼️ Result Screenshots

<img width="666" height="546" alt="image" src="https://github.com/user-attachments/assets/6a0e7020-9875-455e-a443-1bc1711d26c8" />

---

<img width="684" height="617" alt="image" src="https://github.com/user-attachments/assets/187b26f0-817a-474d-adc6-4ec11e8ed345" />


---

## 🛠️ Tech Stack

| Component               | Tool/Library                     |
| ----------------------- | -------------------------------- |
| **Frontend**            | Streamlit                        |
| **Transcript Fetching** | `youtube-transcript-api`         |
| **Embedding**           | HuggingFace                      |
| **Vector Search**       | FAISS                            |
| **LLM**                 | OpenAI GPT / Local LLM           |
| **Chunking Logic**      | Custom (Sliding Window or Fixed) |
| **Backend Language**    | Python                           |

---

## 🔍 Example Use Cases

* Summarize long-form YouTube content (lectures, podcasts, documentaries)
* Ask targeted questions like “What did the speaker say about climate change?”
* Use as a research or study tool for digesting video content quickly

---

## 👤 Author

**Shivam Kashyap**
[LinkedIn](https://www.linkedin.com/in/shivam-kashyap-2768691b5) • [GitHub](https://github.com/shivam4776) • [Email](mailto:shivam4776kashyap@gmail.com)

