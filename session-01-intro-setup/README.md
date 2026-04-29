# Session 01 — Introduction to AI, Setup & First Scripts

## 🎯 What I Learned
- Set up the Python environment and IDEs for data analysis
- Read multiple file formats (CSV, JSON, XML) with Pandas
- Converted and exported data between formats (XML → Excel)
- Explored NumPy basics (diagonal, identity, triangular matrices)
- Tested yfinance for financial data downloading
- Built a simple interactive dashboard with Streamlit
- Understood the difference between Series and DataFrame in Pandas

## 📁 Files
- `script.py` — Main practice script (Pandas, NumPy, yfinance)
- `dashboard.py` — First Streamlit interactive dashboard
- `stu.csv` — Sample student data in CSV
- `stu.json` — Sample student data in JSON
- `stu.xml` — Sample student data in XML
- `stu3.xlsx` — Converted output (XML → Excel)

## 🔑 Key Concepts Covered

| Concept | Library/Tool | Example |
|---------|-------------|---------|
| Read CSV | Pandas | `pd.read_csv()` |
| Read JSON | Pandas | `pd.read_json()` |
| Read XML | Pandas | `pd.read_xml()` |
| Export to Excel | Pandas | `df.to_excel()` |
| Matrix operations | NumPy | `np.diag()`, `np.eye()`, `np.tril()` |
| Financial data | yfinance | `yf.download()` |
| Dashboard | Streamlit | `st.title()`, `st.button()` |
| Data structures | Pandas | Series vs DataFrame |

## 🧠 Key Takeaways
- Pandas handles multiple formats with the same interface (`read_csv`, `read_json`, `read_xml`)
- NumPy provides efficient matrix operations for linear algebra
- yfinance makes financial data accessible in one line
- Streamlit turns Python scripts into web dashboards instantly
- Series = 1D, DataFrame = 2D — understanding this is fundamental
