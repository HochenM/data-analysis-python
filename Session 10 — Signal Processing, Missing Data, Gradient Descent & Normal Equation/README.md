# Session 10 — Signal Processing, Missing Data, Gradient Descent & Normal Equation

## 🎯 What I Learned
- Found peaks and valleys in data using manual loops and `scipy.signal.find_peaks`
- Applied smoothing filters (moving average, weighted average) to financial data
- Calculated Simple Moving Average (SMA) with `rolling()` and manual loops
- Explored Exponential Moving Average (EMA)
- Handled missing data with `SimpleImputer`, `KNNImputer`, `ffill()`, `bfill()`, and `fillna()`
- Implemented Linear Regression with Gradient Descent manually
- Solved Linear Regression using the Normal Equation (exact mathematical solution)
- Compared Gradient Descent vs Normal Equation approaches
- Visualized how the regression line improves over gradient descent iterations
- Generated synthetic data for hands-on ML experimentation

## 📁 Files
- `main.py` — Signal processing, imputation, GD and Normal Equation implementation
- `outputs/` — Plots of smoothing, regression lines, and gradient descent convergence

## 🔑 Key Concepts Covered

| Concept | Method/Tool | Description |
|---------|------------|-------------|
| Peak/Valley Detection | Manual loop, `scipy.signal.find_peaks` | Find local maxima and minima |
| Moving Average Smoothing | Manual weighted average, `rolling().mean()` | Reduce noise in time series |
| Exponential Moving Average | `df['Close'].ewm()` | Gives more weight to recent data |
| Simple Imputer | `SimpleImputer(strategy='median')` | Fill missing values with mean/median |
| KNN Imputer | `KNNImputer()` | Fill missing using nearest neighbors |
| Forward/Backward Fill | `ffill()`, `bfill()` | Propagate last/next valid value |
| Normal Equation | `np.linalg.inv(XᵀX) Xᵀy` | Exact solution — no iterations needed |
| Gradient Descent | Manual GD loop with `lr` and `iterations` | Iterative optimization |
| Learning Rate | `lr = 0.1` | Controls step size for GD convergence |
| Bias Column | `np.c_[np.ones(n,1), X]` | Adds intercept term to features |

## 🧠 Key Takeaways
Peaks and valleys are local extrema — find_peaks automates pattern detection

Moving averages smooth noisy data — larger window = smoother but more lag

EMA reacts faster to recent changes than SMA

ffill() carries last valid value forward — good for time series

bfill() uses next valid value — useful when future data is available

KNNImputer fills missing values based on similarity to other rows

Normal Equation gives exact solution in one step — works best for small datasets

Gradient Descent iteratively approaches the solution — works for large datasets

Learning rate 0.1 with 1000 iterations converged well for synthetic data

Visualizing GD lines shows how the model progressively fits the data

text
