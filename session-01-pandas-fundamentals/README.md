# Session 01 — Pandas Fundamentals & DataFrames

## 🎯 What I Learned
- Loaded real datasets with `sklearn.datasets` (California Housing, Iris)
- Created DataFrames from raw data with proper column names
- Explored data using `head()`, `tail()`, `info()`
- Added target columns to feature DataFrames
- Sorted DataFrames by column values
- Filtered data with logical conditions (`>`, `<`, `&`)
- Accessed specific cells with `.loc[row, column]`
- Inserted NaN values and handled missing data
- Detected nulls with `isnull()` and `sum()`
- Filled missing values with mean imputation
- Introduced to the Iris dataset for classification

## 📁 Files
- `Session 0-1-Pandas1.ipynb` — Jupyter notebook with all exercises
- `outputs/` — Visualizations and plots from this session

## 🔑 Key Pandas Operations Covered

| Operation | Code |
|-----------|------|
| Create DataFrame | `pd.DataFrame(data.data, columns=data.feature_names)` |
| View first rows | `df.head()` |
| View last rows | `df.tail()` |
| Sort values | `df.sort_values(by="column", ascending=False)` |
| Filter rows | `df[df["Target"] > 4.5]` |
| Multiple conditions | `df[(df["Target"]>3) & (df["Target"]<4)]` |
| Access cell | `df.loc[0, "HouseAge"]` |
| Set value | `df.loc[0, "HouseAge"] = np.nan` |
| Check nulls | `df.isnull().sum()` |
| Fill nulls | `df["col"].fillna(df["col"].mean())` |

## 📊 Datasets Used
- **California Housing** — 20,640 rows × 8 features (regression)
- **Iris** — 150 rows × 4 features (classification)

## 🧠 Key Takeaways
- `.loc` accesses by label (row index, column name)
- Use `&` (not `and`) for combining Pandas conditions
- Always check for missing values before analysis
- Mean imputation is a simple first approach for NaN
- `sklearn.datasets` provides clean, ready-to-use data
