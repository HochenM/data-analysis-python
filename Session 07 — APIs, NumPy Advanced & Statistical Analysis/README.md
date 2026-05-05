# Session 07 — APIs, NumPy Advanced & Statistical Analysis

## 🎯 What I Learned
- Fetched live data from a REST API (Wallex crypto exchange)
- Explored API JSON response structure with `.keys()` and `.items()`
- Converted API responses to Pandas DataFrames
- Built a simple API server with **Flask** (GET endpoints, query parameters)
- Used `render_template` to serve HTML pages
- Implemented API key authentication logic
- Connected to Flask API from Python client using `requests`
- Stacked arrays horizontally/vertically with `hstack` and `vstack`
- Used `np.where()` for conditional indexing and masking
- Applied `np.clip()` to limit values to a valid range
- Explored `np.tile()`, `np.repeat()`, and `np.diff()` for array manipulation
- Padded arrays with different modes (`constant`, `reflect`, `edge`, `linear_ramp`)
- Generated random permutations and selections from arrays
- Loaded the **Diabetes dataset** and analyzed feature correlation
- Created **heatmaps** with Seaborn for correlation visualization
- Computed **covariance** and **correlation** matrices manually and with NumPy/Pandas
- Understood positive, negative, and zero correlation with examples

## 📁 Files
- `main.py` — All session exercises
- `outputs/` — Heatmap visualizations from this session

## 🔑 Key Concepts Covered

| Concept | Library/Tool | Example |
|---------|-------------|---------|
| REST API call | `requests` | `requests.get(url).json()` |
| JSON exploration | Python dict | `.keys()`, `.items()`, `for k,v in ...` |
| Create API server | Flask | `@app.route('/student')` |
| Query parameters | Flask | `request.args.get('key')` |
| HTML templates | Flask | `render_template('index.html')` |
| API key auth | Flask | Check key → return data or error |
| Client-server API | `requests` | `requests.get("http://127.0.0.1:5000/...")` |
| Stack arrays | NumPy | `np.hstack()`, `np.vstack()` |
| Conditional indexing | NumPy | `np.where((X>5) & (X<10))` |
| Value clipping | NumPy | `np.clip(result, 0, 255)` |
| Tile/Repeat | NumPy | `np.tile()`, `np.repeat()` |
| Difference | NumPy | `np.diff(A, n=1)` |
| Padding | NumPy | `np.pad(A, pad_width=(2,2), mode='edge')` |
| Random operations | NumPy | `np.random.permutation()`, `np.random.choice()` |
| Correlation heatmap | Seaborn | `sns.heatmap(df.corr(), annot=True)` |
| Covariance matrix | NumPy | `np.cov(X, y)` |
| Correlation matrix | Pandas | `df.corr()` |

## 📊 Datasets Used
- **Wallex API** — Crypto market data (live JSON)
- **Diabetes** — 442 samples × 10 features (sklearn)
- **Custom arrays** — Manual correlation examples

## 🧠 Key Takeaways
- APIs return JSON → Python dictionaries → easy to loop and convert
- `pd.DataFrame(api_data)` works but may need `.T` for nested structures
- Flask makes API creation simple — just define routes and return JSON
- `np.where()` returns indices; `np.clip()` modifies values in-place
- Padding is essential for CNNs and signal processing
- `df.corr()` gives Pearson correlation; 1 = perfect positive, -1 = perfect negative
- Heatmaps are the best way to visualize correlation at a glance
