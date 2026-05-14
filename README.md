# 🚀 InternFlow AI

AI-powered internship and mentor management platform built using Python, FastAPI, LangChain, and Streamlit.

InternFlow AI automates internship workflow management by generating structured project plans, creating internship tasks, and intelligently matching interns with mentors based on skills and expertise from uploaded Excel datasets.

---

# ✨ Features

* 📂 Upload Excel datasets containing interns and mentors
* 🤖 AI-generated internship/project plans
* 📝 Automatic task generation for interns
* 🎯 Smart mentor-intern matching using LLMs
* 🌐 REST API built with FastAPI
* 📊 Interactive Streamlit frontend
* 🔗 Public API access using Ngrok
* 🧠 Powered by Hugging Face LLMs and LangChain

---

# 🛠️ Technologies Used

* Python
* Streamlit
* FastAPI
* LangChain
* Hugging Face Transformers
* Pandas
* Pyngrok
* FAISS
* Sentence Transformers

---

# ⚙️ System Workflow

1. User uploads an Excel dataset
2. System reads interns and mentors data
3. AI generates a complete internship/project plan
4. Tasks are automatically created
5. Interns are matched with suitable mentors
6. Results are returned through the API and displayed in the frontend

---

# 📂 Excel Dataset Structure

The uploaded Excel file should contain:

## Mentors Sheet

* Mentor Name
* Skills
* Experience
* Domain

## Interns Sheet

* Intern Name
* Skills
* Interests
* Level

---

# 🚀 Run the Project

## Install Dependencies

```bash id="s19a1"
pip install -r requirements.txt
```

## Run FastAPI Server

```bash id="c72lq"
uvicorn app:app --reload
```

## Run Streamlit Frontend

```bash id="w9x2n"
streamlit run app.py
```

---

# 🧠 AI Capabilities

InternFlow AI uses Large Language Models (LLMs) to:

* Generate internship roadmaps
* Create beginner-friendly tasks
* Recommend mentor assignments
* Structure project timelines
* Automate internship coordination

---

# 📡 API Endpoint

```python id="s81dp"
POST /process-project
```

Accepts:

* Project title
* Excel dataset file

Returns:

* Generated project plan
* Task assignments
* Mentor matching results

---

# 🎯 Use Cases

* Internship management systems
* Training programs
* University graduation projects
* Team assignment automation
* HR onboarding workflows

---

# 👨‍💻 Author

Developed using AI, FastAPI, LangChain, and Streamlit.
