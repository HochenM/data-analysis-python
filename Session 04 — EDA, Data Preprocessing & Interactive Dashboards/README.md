# Session 04 — Data Preprocessing, EDA & Interactive Visualization

## 🎯 What I Learned
- Loaded and cleaned tabular data (column dropping, label encoding, type narrowing)
- Used `LabelEncoder` to convert categorical variables to numeric
- Performed Exploratory Data Analysis (EDA) with correlation heatmaps and pair plots
- Filtered data subsets for targeted correlation analysis (`df[df['Age']<20]`)
- Downloaded financial data with `yfinance` (BTC-USD)
- Built a **candlestick chart** using `plotly.graph_objects`
- Converted Gregorian dates to Jalali (Persian) calendar using `persiantools`
- Created an **interactive dashboard** with `streamlit`
- Added dropdown selectors (`st.selectbox`) for crypto selection
- Combined data visualization and analysis in a single Streamlit app

## 📁 Files
- `main.py` — Data preprocessing, EDA, candlestick chart, and Streamlit crypto dashboard
- `outputs/` — Heatmaps, pair plots, and interactive chart screenshots

## 🔑 Key Concepts Covered

| Concept | Library/Tool | Example |
|---------|-------------|---------|
| Label Encoding | `sklearn.preprocessing.LabelEncoder` | Gender → 0/1 |
| Data Type Narrowing | NumPy | `astype(np.uint8)` to save memory |
| Correlation Matrix | Pandas | `df.corr()` |
| Correlation Heatmap | Seaborn | `sns.heatmap(df.corr(), annot=True)` |
| Pair Plot | Seaborn | `sns.pairplot(df, hue='Gender')` |
| Financial Data | `yfinance` | `yf.download('BTC-USD')` |
| Candlestick Chart | `plotly.graph_objects` | `go.Candlestick()` |
| Jalali Date Conversion | `persiantools.jdatetime` | `JalaliDateTime(x).date()` |
| Interactive Dashboard | `streamlit` | `st.selectbox()`, `st.plotly_chart()` |
| Lambda Functions | Python | `apply(lambda x: 'green' if x > 0 else 'red')` |

## 📊 Datasets Used
- **Tabular data** — CSV with demographics (age, gender, etc.)
- **BTC-USD** — Bitcoin daily price data via yfinance

## 🧠 Key Takeaways
- `LabelEncoder` converts categorical labels to integers for ML models
- `astype(np.uint8)` reduces memory usage for small integer columns
- Correlation heatmaps reveal relationships between features at a glance
- Pair plots with `hue` show how categories separate across features
- `plotly` creates interactive charts that users can zoom and hover
- `persiantools` seamlessly converts dates to Jalali calendar
- `streamlit` turns Python scripts into web dashboards with minimal code
- `st.selectbox` allows dynamic user input for interactive analysis
- Candlestick charts are the standard visualization for financial OHLC data
- Lambda functions provide concise one-line transformations
