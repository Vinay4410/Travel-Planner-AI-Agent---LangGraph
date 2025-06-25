# ✈️ Travel-Planner-AI-Agent---LangGraph


Create your dream itinerary using LLM + Tools + LangGraph + Streamlit.

---

## 🚀 Features

- ✅ Day-by-day itinerary generation
- 📍 Real-time hotel, flight & weather info
- 🧠 RAG-based destination memory
- 💸 Budget calculator & currency converter
- 🎯 Works in Streamlit with beautiful UI

---

## 🛠️ Tech Stack

- OpenAI + LangGraph
- Streamlit (UI)
- FAISS (for RAG)
- Tavily / Serper / OpenWeather APIs

---

## 🧩 Folder Structure

📁 src/
├── app.py
├── agent_setup.py
├── travel_agent.py
├── utils.py


---

.env.example

## ⚙️ Environment Variables (`.env.example`)

```env
OPENAI_API_KEY=your-key
LANGCHAIN_API_KEY=your-key
SERPER_API_KEY=your-key
TAVILY_API_KEY=your-key
OPENWEATHER_API_KEY=your-key
LANGCHAIN_PROJECT=Project-name
LANGCHAIN_TRACING_V2=true



---

▶️ Run Locally
pip install -r requirements.txt
streamlit run app.py

---

📦 Exported Plan Format
Markdown itinerary with:

🗓️ Daily sections
🍽️ Food
✈️ Flights
🏨 Hotels
🌦️ Weather


