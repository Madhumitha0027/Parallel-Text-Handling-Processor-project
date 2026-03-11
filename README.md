# Python-Parallel-Text-Handling-Processor-project

## 📌 Project Overview
Python Parallel Text Handling Processor is a scalable text processing system developed using Python.  
The application processes large volumes of textual data using parallel execution techniques and stores results in an SQLite database.  
The project includes performance benchmarking and scalability testing to evaluate execution efficiency.

---

## 🚀 Implemented Features
- Text and CSV file processing
- Text chunking for large dataset handling
- Parallel execution (Single Execution, ThreadPoolExecutor, Multiprocessing)
- Performance benchmarking and scalability testing
- SQLite database integration
- Database indexing for optimized queries
- Bulk data insertion

---

## 🔄 System Flow

The system follows a structured pipeline to process large-scale text data efficiently.

1️⃣ Input File Processing  
Users provide text or CSV files. The system reads and prepares the input data for processing.

2️⃣ Text Chunking  
Large text content is divided into smaller chunks to make processing faster and more scalable.

3️⃣ Parallel Processing  
Chunks are processed using different execution strategies:
- Single Execution  
- ThreadPoolExecutor  
- Multiprocessing  

4️⃣ Database Storage  
Processed results are stored in an SQLite database. Indexing is used to improve query speed and data retrieval.

---

## ⚙️ Technologies Used
- Python
- SQLite
- concurrent.futures
- Pandas

---

## 📂 Project Structure

```
Parallel-Text-Handling-Processor-project/
│
├── modules/
│   ├── text_loader.py        # Text chunking & parallel loader
│   └── rule_engine.py        # Weighted sentiment scoring
│
├── database/
│   └── db_manager.py         # SQLite database operations
│
├── benchmark_test.py         # Performance & scalability testing
├── main.py                   # Core processing script
├── texts.db                  # SQLite database file
├── README.md
```

---

## ▶️ How to Run

Run Main Processing:
python main.py

Run Benchmark Tests:
python benchmark_test.py

---
