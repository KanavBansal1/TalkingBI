🎙️ Talking BI — AI Conversational Business Intelligence System
🚀 Overview

Talking BI is an AI-powered conversational Business Intelligence system that allows users to interact with their database using natural language or voice commands. The system automatically generates SQL queries, fetches relevant data, creates interactive dashboards, and provides AI-generated business insights.

This project eliminates the need for manual dashboard creation and SQL knowledge, making data analytics accessible to non-technical users.

🎯 Key Features
🧠 AI-Powered Analytics
Natural language query to SQL generation
Groq LLM-powered insights
Conversational BI interface
📊 Dynamic Dashboard Generation
Automatic dashboard creation
Multiple chart types:
Bar Chart
Line Chart
Pie Chart
Scatter Plot
🎤 Voice Enabled Analytics
Voice input support
Voice output for insights
Conversational chatbot
🔐 Authentication
Login / Signup system
Session management
Secure access
🎨 Multiple Themes
Light Theme
Dark Theme
Blue Theme
Corporate Theme
📥 Download Support
Download dashboards
Export CSV data
🔌 Universal Database Support

Connect to:

SQLite
MySQL
PostgreSQL
SQL Server
Cloud Databases
🧠 How It Works
Workflow
User Voice/Text Query
        ↓
Groq LLM
        ↓
SQL Query Generation
        ↓
Database Connection
        ↓
Fetch Data
        ↓
Generate Dashboards
        ↓
Generate Insights
        ↓
Voice + Text Output
🏗️ Project Architecture
Talking BI
│
├── app.py
├── chatbot.py
├── database.py
├── sql_generator.py
├── schema_extractor.py
├── dynamic_dashboard.py
├── dashboard_cards.py
├── insights.py
├── auth.py
├── themes.py
├── download.py
├── voice.py
└── data/
🛠️ Tech Stack
Frontend
Streamlit
Backend
Python
AI / LLM
Groq LLM
LangChain
Database
SQLAlchemy
SQLite / MySQL / PostgreSQL
Visualization
Plotly
Voice Processing
SpeechRecognition
gTTS
Authentication
SQLite
🚀 Installation
Clone Repository
git clone https://github.com/KanavBansal1/TalkingBI.git
cd TalkingBI
Create Virtual Environment
python -m venv venv

Activate:

Windows:

venv\Scripts\activate
Install Requirements
pip install -r requirements.txt

If no requirements file:

pip install streamlit pandas plotly sqlalchemy langchain groq speechrecognition gtts kaleido
🔑 Setup Environment Variables

Create .env

GROQ_API_KEY=your_api_key
▶️ Run Application
streamlit run app.py
💡 Example Queries

Try:

Show top 5 states by sales
Which category has highest profit
Suggest business improvements

Voice Example:

Which region needs marketing investment
📊 Screenshots
Dashboard Generation
AI generated dashboards
Conversational BI
Voice enabled assistant
AI Insights
Business insights generation
🔐 Security Features
Read-only database access
No destructive queries allowed
Authentication system
🚀 Future Improvements
Real-time analytics
Multi-user dashboards
Cloud deployment
Role-based access
🎯 Use Cases
Business Analytics
Sales Insights
Marketing Analysis
Financial Reporting
Data Exploration
🧠 What Makes This Project Unique

This project combines:

Conversational AI
Business Intelligence
Voice Assistant
SQL Automation

Talking BI works like:

ChatGPT + Power BI Combined

👨‍💻 Author

Kanav Bansal

GitHub:
https://github.com/KanavBansal1

⭐ If You Like This Project

Give it a star ⭐ on GitHub

🎉 Final

Talking BI simplifies data analytics by enabling users to talk to their data and automatically generate dashboards and insights.

DeployedLink - https://talkingbi-mhw7zywwke4fbabnk6ajxq.streamlit.app/
