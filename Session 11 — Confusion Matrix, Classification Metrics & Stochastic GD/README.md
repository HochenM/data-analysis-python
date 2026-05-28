# Session 09 — Confusion Matrix, Classification Metrics & Stochastic GD

## 🎯 What I Learned
- Built a **confusion matrix manually** using nested loops and label matching
- Calculated **TP, FP, FN** from scratch for multi-class classification
- Used sklearn's `confusion_matrix`, `precision_score`, `recall_score`, `f1_score`
- Understood **macro average** for multi-class metrics
- Used `classification_report` for all metrics in one line
- Implemented **Stochastic Gradient Descent (SGD)** with random sampling
- Used a **learning schedule** (`t0/(t + t1)`) to decrease learning rate over time
- Visualized SGD convergence by plotting prediction lines per iteration
- Understood why `[i:i+1]` keeps 2D shape vs `[i]` which flattens

## 📁 Files
- `main.py` — Manual confusion matrix, sklearn metrics, SGD with learning schedule
- `outputs/` — Confusion matrix tables and SGD convergence plots

## 🔑 Key Concepts Covered

| Concept | Method/Tool | Description |
|---------|------------|-------------|
| Confusion Matrix (Manual) | Nested loops over unique labels | Count TP, FP, FN per class |
| Confusion Matrix (Sklearn) | `confusion_matrix(y_true, y_pred)` | Automated confusion matrix |
| Precision | `precision_score(..., average='macro')` | TP / (TP + FP) |
| Recall | `recall_score(..., average='macro')` | TP / (TP + FN) |
| F1 Score | `f1_score(..., average='macro')` | Harmonic mean of P and R |
| Classification Report | `classification_report(y_true, y_pred)` | All metrics + support per class |
| Macro Average | `average='macro'` | Equal weight to all classes |
| SGD | Random sample per step | Faster, noisier convergence |
| Learning Schedule | `lr = t0 / (t + t1)` | Decreases lr over time |


## 🧠 Key Takeaways
[i:i+1] keeps shape (1, 2) for matrix multiplication — [i] gives (2,) and can break

Macro average treats all classes equally — best for imbalanced datasets

classification_report gives precision, recall, f1 per class in one table

SGD picks ONE random sample per step — much faster than batch GD

Learning schedule reduces lr over time — helps convergence near minimum

Manual confusion matrix helps understand what sklearn does internally

FP = predicted positive but actually negative; FN = predicted negative but actually positive


## 🔧 Key Methods Used

```python
# Manual confusion matrix
labels = np.unique(y_true)
cm = np.zeros((len(labels), len(labels)))
for i, true_label in enumerate(labels):
    for j, pred_label in enumerate(labels):
        cm[i, j] = np.sum((y_true == true_label) & (y_pred == pred_label))

# sklearn metrics
cm = confusion_matrix(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average='macro')
f1 = f1_score(y_true, y_pred, average='macro')

# SGD with learning schedule
lr = t0 / (t + t1)
random_idx = np.random.randint(m)
xi = X_b[random_idx:random_idx+1]  # Keep 2D
gradient = 2 * xi.T @ (xi @ thetas - yi)
thetas = thetas - lr * gradient
