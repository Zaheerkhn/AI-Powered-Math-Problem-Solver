# 📘 AI-Powered Math Problem Solver

## 🚀 Overview
The **AI-Powered Math Problem Solver** is a Streamlit-based web application that leverages AI to solve complex math problems, provide step-by-step explanations, and retrieve relevant information from Wikipedia. It integrates **LangChain** with Groq's **Gemma2-9b-It** model and supports various tools like a calculator, logical reasoning solver, and Wikipedia search.

## 🎯 Features
- **Step-by-Step Math Problem Solving** 
- **Wikipedia Search for Additional Information** 
- **Numerical Calculation Using AI** 
- **Interactive Chat-Based Interface** 
- **Beautiful and Responsive UI** 

## 🏗️ Tech Stack
- **Python** 
- **Streamlit** 
- **LangChain** 
- **Groq (Google: Gemma2-9b-It)** 
- **Wikipedia API** 

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Zaheerkhn/AI-Powered-Math-Problem-Solver
cd math-problem-solver
```

### 2️⃣ Install Dependencies
Make sure you have **Python 3.8+** installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your API keys:
```env
LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

## 🏆 How It Works
1. **User Inputs Math Problem**: Enter a mathematical query in the chat input.
2. **AI Processes the Query**: The application uses LangChain's **LLMMathChain** for calculations and **LLMChain** for logical reasoning.
3. **Wikipedia Lookup (If Needed)**: If the query involves general knowledge, Wikipedia API provides additional context.
4. **AI Responds with Solution**: The AI gives a step-by-step solution or direct answer based on the query type.
5. **Interactive Chat Experience**: Users can continuously ask follow-up questions or input new problems.

## 📌 Features Breakdown
- **Math Calculation**: Uses AI for arithmetic and algebraic problem-solving.
- **Reasoning-Based Solutions**: Breaks down complex logical problems into structured steps.
- **Wikipedia Search**: Fetches real-world facts and definitions when required.
- **Custom UI Styling**: Enhances readability and interaction experience.

## 🤝 Contribution
Contributions are welcome! Feel free to fork the repo and submit a pull request.

## 📜 License
This project is licensed under the **Apache License 2.0**.

---
💡 **Developed with AI and Math Enthusiasm!** 🧠


