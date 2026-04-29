# Session 02 — NumPy, Pandas Deep Dive & Matplotlib/Seaborn Basics

## 🎯 What I Learned
- Renamed DataFrame columns
- Explored DataFrame structure (`shape`, `columns`, `dtypes`, `memory_usage`)
- Understood data types (float64 vs float32) and memory optimization
- Distinguished between Series and DataFrame outputs
- Counted unique values with `value_counts()`
- Created bar plots, scatter plots, line plots, and histograms
- Used both Matplotlib and Seaborn for visualization
- Learned `pd.cut()` for binning continuous data
- Created box plots for distribution comparison
- Used pair plots to visualize all feature relationships at once
- Identified best features for prediction visually

## 📁 Files
- `session02.ipynb` — Jupyter notebook with all exercises
- `outputs/` — Visualizations and plots from this session

## 🔑 Key Concepts Covered

| Concept | Library | Example |
|---------|---------|---------|
| Rename columns | Pandas | `df.columns = ['SL','SW','PL','PW','Target']` |
| Memory optimization | Pandas | `df.astype({'SL': 'float32'})` |
| Series vs DataFrame | Pandas | `df.loc[4]` vs `df.loc[[4]]` |
| Value counts | Pandas | `df['Target'].value_counts()` |
| Bar plot | Matplotlib | `plt.bar(a.index, a.values)` |
| Bar plot | Seaborn | `sns.barplot(df, x=a.index, y=a.values)` |
| Scatter plot | Seaborn | `sns.scatterplot(data=df, x='PL', y='Target', hue='Target')` |
| Line plot | Matplotlib | `plt.plot(df.index, df['SL'])` |
| Histogram | Matplotlib | `plt.hist(df['PL'])` |
| Binning data | Pandas | `pd.cut(df['age'], bins=4)` |
| Box plot | Pandas | `df.boxplot(['PL', 'SW'])` |
| Pair plot | Seaborn | `sns.pairplot(df, hue='Target')` |

## 📊 Datasets Used
- **Iris** — 150 rows × 4 features (classification)

## 🧠 Key Takeaways
- `float32` uses half the memory of `float64` — important for large datasets
- `df.loc[4]` returns Series, `df.loc[[4]]` returns DataFrame — syntax matters
- `pd.cut()` converts continuous data into categorical bins
- Pair plots reveal which features best separate classes
- Box plots show distribution, median, and outliers in one view
