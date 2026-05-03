# Session 05 — Data Cleaning, APIs & Multiprocessing

## 🎯 What I Learned
- Downloaded financial data with `yfinance` (Bitcoin prices)
- Extracted date components (`.dt.month`) from datetime index
- Loaded and inspected real weather API data (CSV)
- Handled mixed data types with `pd.to_numeric()` and `errors='coerce'`
- Understood the difference between single processing vs multiprocessing
- Ran parallel functions using `multiprocessing.Process`

## 📁 Files
- `finance.py` — Bitcoin data download and date extraction with yfinance
- `weather.py` — Weather data cleaning (handling invalid values)
- `weather.csv` — Real weather dataset (temperature, rain, snowfall, wind speed)
- `Multiprocessing.py` — Single vs parallel processing demo
- `outputs/` — Visualizations and plots from this session

## 🔑 Key Concepts Covered

| Concept | Library/Method | Example |
|---------|---------------|---------|
| Financial data download | `yfinance` | `yf.download('BTC-USD')` |
| Date extraction | Pandas `.dt` | `df['Date'].dt.month` |
| Convert to numeric | `pd.to_numeric()` | `errors='coerce'` |
| Handle bad data | `errors='coerce'` | Invalid → NaN |
| Parallel processing | `multiprocessing` | `Process(target=func)` |

## 📊 Datasets Used
- **BTC-USD** — Bitcoin daily prices (via yfinance)
- **Weather data** — Temperature, rain, snowfall, wind speed (CSV)

## 🔍 Data Cleaning Details

| Error Type | `pd.to_numeric()` Behavior |
|------------|---------------------------|
| `errors='raise'` | Throws error on invalid data |
| `errors='ignore'` | Keeps original (no conversion) |
| `errors='coerce'` | Invalid → **NaN** (safest!) |

## 🧠 Key Takeaways
- `yfinance` provides clean financial data with minimal code
- `pd.to_numeric(errors='coerce')` is the safest way to clean mixed columns
- Weather data often has missing values — always inspect with `.info()` first
- Multiprocessing runs functions in parallel, not sequentially
- `if __name__ == "__main__"` is required for multiprocessing on Windows
