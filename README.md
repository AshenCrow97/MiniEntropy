# MiniEntropy
This project creates minimalistic art through a multi-step process involving K-Means color quantization, entropy-based slicing, and cell-wise color simplification.

## How It Works
1. Resize image - since the final artwork is very minimalistic, we can reduce the number of pixels to optimize computation
![Alt text](./starry_night_example/00_orig.bmp?raw=true "Starry Night")

2. Make color palette - we use KMeans model clustering to find the most prominent colors
![Alt text](./starry_night_example/01_k_colors.bmp?raw=true "Starry Night")

3. Slice image horizontally and vertically - we use DecisionTreeClassifier to slice the image into segments with lowest Entropy
![Alt text](./starry_night_example/02_slices.bmp?raw=true "Starry Night")

4. Color cells - we color the cells bounded by the slices with the most common color from the palette
![Alt text](./starry_night_example/03_cells.bmp?raw=true "Starry Night")


## Instalation and Usage
```
git clone https://github.com/AshenCrow97/MiniEntropy.git
cd MiniEntropy
pip3 install -r requirements.txt
./main.py
