# 📱 Budget-Based Mobile Advisor

A modular Python SaaS application built with **Streamlit** that helps users discover the best mobile phones tailored to their monthly income, expenses, and savings goals.

## 🚀 Features
- **Smart Savings Calculator:** Calculates target budget based on user income, expenses, and savings duration.
- **Dynamic Mobile Recommendations:** Filters and ranks mobile devices within the calculated budget.
- **Modular Architecture:** Strictly follows the **Separation of Concerns (SoC)** principle across independent modules.
- **Interactive Web UI:** Clean and responsive user interface powered by Streamlit.

## 🏗️ Architecture & Project Structure
```text
Project/
├── data.json         # Local mobile dataset
├── scraper.py        # Data loading and ingestion module
├── calculator.py     # Core business logic and calculations
├── main.py           # Streamlit Web UI application
└── README.md         # Project documentation