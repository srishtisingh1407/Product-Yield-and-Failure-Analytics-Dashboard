# 📊 Product Yield and Failure Analytics Dashboard

A Python dashboard that analyzes factory test data for NAND flash memory production. It tracks unit-level results, calculates overall yield, and visualizes failure patterns and time-to-repair (TTR) metrics.

---

## ✅ Features
- 📈 **Compute yield** across production cycles
- ❌ **Analyze failure types** (e.g., ECC errors, Voltage drops)
- ⏱️ **Visualize TTR distribution** for failed units
- 📊 **Charts built using matplotlib**
- 🐍 Clean and modular Python code

---

## 🗂️ Folder Structure
```bash
Product-Yield-Analytics/
├── analytics_dashboard.py     # Main Python script
├── factory_data.csv           # Sample NAND factory data
├── README.md                  # This file
```
## 🐍 Requirements
Make sure Python 3.x is installed along with:

bash
Copy
Edit
pip install pandas matplotlib
🚀 How to Run
bash
Copy
Edit
python analytics_dashboard.py
This will:

✅ Print overall product yield in terminal

📊 Show a bar chart of failure types

⏱️ Display a histogram of TTR (repair time) for failed units

## 🧠 Sample Output
Terminal:

vbnet
Copy
Edit
✅ Overall Yield: 85.00% (425/500)
Charts:

Failure Type Distribution (bar chart)

TTR Distribution (histogram of failed units)

