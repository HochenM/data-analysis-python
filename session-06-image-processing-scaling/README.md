# Session 06 — Image Processing, Scaling, Encoding & Visualization

## 🎯 What I Learned
- Loaded Digits and MNIST datasets for image classification
- Reshaped and displayed image data with Matplotlib and OpenCV
- Applied data scaling: `StandardScaler` and `MinMaxScaler`
- Compared BTC and ETH prices before and after normalization
- Used inverse_transform to recover original values
- Encoded categorical data with `LabelEncoder` and `OneHotEncoder`
- Loaded, split, merged, and displayed color channels with OpenCV
- Visualized individual R, G, B channels with zero-padding technique
- Captured webcam frames and real-time video with OpenCV
- Detected faces using Haar Cascade Classifier
- Applied Canny edge detection on live video
- Explored ResNet50 architecture from Keras Applications
- Reduced image dimensions with `np.ravel()` and `reshape()`
- Loaded Olivetti Faces dataset
- Created statistical plots: boxplot, violin plot, and pie chart

## 📁 Files
- `main.py` — All session exercises combined
- `session 4.py` — MNIST image display
- `boxplot1.png` — BTC boxplot visualization
- `boxandviolen1.png` — Box and violin plot stats
- `outputs/` — Additional visualizations from this session

## 🔑 Key Concepts Covered

| Concept | Library/Tool | Example |
|---------|-------------|---------|
| Load digits/MNIST | `sklearn.datasets` | `load_digits()`, `fetch_openml()` |
| Image display | Matplotlib/OpenCV | `plt.imshow()`, `cv.imshow()` |
| Standard scaling | `StandardScaler` | Zero mean, unit variance |
| Min-Max scaling | `MinMaxScaler` | Scale to [0, 1] or custom range |
| Inverse transform | `scaler.inverse_transform()` | Recover original values |
| Label encoding | `LabelEncoder` | `male` → 0, `female` → 1 |
| One-hot encoding | `OneHotEncoder` | `male` → [1,0], `female` → [0,1] |
| BGR/RGB split | OpenCV | `cv.split(img)` |
| Channel visualization | OpenCV | `cv.merge((b, z, z))` |
| Webcam capture | OpenCV | `cv.VideoCapture(0)` |
| Face detection | Haar Cascade | `detectMultiScale()` |
| Edge detection | Canny | `cv.Canny(frame, 100, 200)` |
| ResNet50 | Keras Applications | `ResNet50(weights='imagenet')` |
| Flatten/Reshape | NumPy | `np.ravel()`, `.reshape()` |
| Box plot | Matplotlib | `plt.boxplot()` |
| Violin plot | Matplotlib | `plt.violinplot()` |
| Pie chart | Matplotlib | `plt.pie()` |

## 📊 Datasets Used
- **Digits** — 8×8 handwritten digits
- **MNIST** — 28×28 handwritten digits (via OpenML)
- **BTC-USD & ETH-USD** — Cryptocurrency prices (yfinance)
- **Olivetti Faces** — 64×64 face images
- **ImageNet (ResNet50)** — Pre-trained weights

## 🧠 Key Takeaways
- `MinMaxScaler` preserves shape better than `StandardScaler` for visualization
- OpenCV loads images in BGR, Matplotlib expects RGB — use `cv.cvtColor()`
- Zero-padding channels with `np.zeros_like()` isolates individual color channels
- Haar Cascade is a fast, pre-trained face detector
- Canny edge detection works on live video at 30+ FPS
- ResNet50 has 1000 classes pre-trained on ImageNet
- `np.ravel()` flattens any N-D array to 1D efficiently
