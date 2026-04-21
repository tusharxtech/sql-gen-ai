# 🧠 Text-to-SQL Query Generator using LLM

This project is a **Streamlit-based web application** that converts natural language queries into **SQLite SQL queries** using an LLM powered by **Ollama (LLaMA 3.2)**.

---

## 🚀 Features

* 🔤 Convert plain English queries into SQL
* 🧠 Powered by LLM (LLaMA 3.2 via Ollama)
* 🗄️ Executes queries on a SQLite database
* 📊 Displays results instantly in UI
* ⚡ Simple and lightweight interface using Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Ollama (LLaMA 3.2 model)**
* **SQLite**
* **dotenv**

---

## 📂 Database Schema

The application uses a sample table:

```
products (
    product_id,
    product_name,
    category,
    price,
    stock_quantity
)
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/text-to-sql-llm.git
cd text-to-sql-llm
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Setup environment variables

Create a `.env` file and add:

```
LANGCHAIN_API_KEY=your_key
OLLAMA_API_KEY=your_key
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 💡 Example Usage

### Input:

```
Show all products with price greater than 500
```

### Output (Generated SQL):

```
SELECT * FROM products WHERE price > 500;
```

---

## 🧩 How It Works

1. User enters a natural language query
2. The query is sent to the LLM via LangChain
3. LLM converts it into a valid SQLite query
4. Query is executed on local database
5. Results are displayed in Streamlit UI

---

## ⚠️ Important Notes

* The LLM is instructed to return **only SQL queries**
* No explanation or extra text is allowed
* Ensure your database (`sqldb.db`) exists before running
* Designed specifically for **SQLite syntax**

---

## 🔮 Future Improvements

* Support multiple tables
* Add query validation & error handling
* Improve prompt engineering for accuracy
* Add chat history
* Deploy on cloud

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/tusharxtech
