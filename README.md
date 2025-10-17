# AI Research Assistant Chatbot 🤖

> A full-stack web application featuring an intelligent, tool-using LLM agent, built with Django and LangChain, and deployed on AWS EC2.

## 🎯 Project Goal

The objective of this project was to develop and deploy a complete AI-powered chatbot from scratch. Unlike simple chatbots, this application uses an **LLM agent architecture**, enabling it to perform complex, multi-step reasoning by autonomously selecting and using external tools to answer questions that require real-time information or logical calculations.

---

## ✨ Features

* **Natural Language Understanding:** Interprets user queries to determine intent and required actions.
* **Tool-Using Agent:** The core of the application is a LangChain agent that can use two primary tools:
    * **🌐 Web Search:** Utilizes the DuckDuckGo API to find up-to-date information on the internet.
    * **🧮 Calculator:** A custom tool to perform mathematical calculations.
* **Multi-Step Reasoning:** The agent can chain its thoughts and tools together to solve complex problems (e.g., "Find the population of Tokyo and divide it by the area of Japan").
* **API Backend:** A robust API built with **Django Rest Framework** handles all communication between the frontend and the AI agent.

---

## 🛠️ Tech Stack & Architecture

The application is built with a modern, production-ready architecture.

**Tech Stack:**
* **Backend:** Python, Django, Django Rest Framework (DRF)
* **AI Framework:** LangChain, Google Gemini API
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** AWS EC2 (Ubuntu), Nginx, Gunicorn

**Architecture:**

The user interacts with a simple web interface. When a message is sent, a JavaScript `fetch` call sends a `POST` request to the backend API. **Nginx**, acting as a reverse proxy, receives this request on port 80 and forwards it to the **Gunicorn** application server on port 8000. Gunicorn runs the **Django** application, which processes the request, sends the query to the **LangChain agent**, and returns the agent's response as JSON.

---

## 🚀 Local Setup

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rohan00112233/Django_Chatbot_project.git](https://github.com/rohan00112233/Django_Chatbot_project.git)
    cd Django_Chatbot_project
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file** in the root directory and add your Google API key:
    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

---

## ☁️ Deployment Status

* **Live URL:** `http://18.234.46.163`
* **Status:** The application is fully deployed on an AWS EC2 instance with Nginx and Gunicorn. The frontend loads correctly, and the backend infrastructure is running.
* **Known Issue:** A final runtime configuration issue exists in the live environment, causing the bot to not return a response. The application is **fully functional** in the local development environment, indicating the core logic is sound.

---

## 💡 Key Learnings & Challenges Solved

This project provided deep, hands-on experience in full-stack development and cloud deployment. Key challenges that were successfully diagnosed and resolved include:

* **Production Security:** Correctly configured Django's `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` for a live server environment.
* **Server Process Management:** Fixed server-side port conflicts (`Address already in use`) by identifying and managing stray Gunicorn processes.
* **WSGI Server Configuration:** Resolved Gunicorn worker timeouts by tuning the `--timeout` setting to handle slow initial AI API calls.
* **Linux Environment & Permissions:** Diagnosed and fixed `sudo` environment path and variable issues when running the application server as a service.
* **Dependency Management:** Resolved numerous `ModuleNotFoundError` issues on both local and server environments by managing `requirements.txt` and virtual environments.
