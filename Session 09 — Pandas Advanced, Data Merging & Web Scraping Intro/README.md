# Session 09 — Pandas Advanced, Data Merging & Web Scraping Intro

## 🎯 What I Learned
- Created DataFrames from lists of dictionaries and dictionary of lists
- Concatenated DataFrames vertically with `pd.concat()`
- Merged DataFrames using SQL-style joins with `pd.merge()`
- Understood different join types (inner, left, right, outer)
- Handled missing values (`NaN`) during merge operations
- Used `shift()` to create time-series target variables (e.g., next day's price)
- Dropped rows with missing values using `dropna()`
- Introduced to web scraping/crawling concepts (Part 3 placeholder)

## 📁 Files
- `main.py` — DataFrame creation, merging, shifting, and scraping intro
- `outputs/` — Any resulting tables or screenshots

## 🔑 Key Concepts Covered

| Concept | Method | Description |
|---------|--------|-------------|
| DataFrame from dict list | `pd.DataFrame([{...}, {...}])` | Each dict = one row |
| DataFrame from dict of lists | `pd.DataFrame({'col': [...]})` | Each key = one column |
| Concatenation | `pd.concat([df1, df2], axis=0)` | Stack DataFrames vertically |
| Merge (Join) | `pd.merge(left, right, how='inner', on='id')` | SQL-style join on common column |
| Shift | `df['price'].shift(-1)` | Move values down/up for time-series targets |
| Drop NaN | `df.dropna()` | Remove rows with missing values |

## 🧠 Key Takeaways
- `pd.DataFrame()` accepts both list-of-dicts and dict-of-lists formats
- `pd.concat(axis=0)` stacks DataFrames vertically (more rows)
- `pd.merge()` is SQL-style — needs `on=` to specify the key column
- Inner merge keeps only matching rows; NaN in key column prevents matching
- `shift(-1)` creates "next value" column — essential for time-series prediction
- `shift(1)` creates "previous value" column — useful for lag features
- `dropna()` removes rows with any NaN — clean data before modeling
- Web scraping/crawling extracts data from websites (next step)
