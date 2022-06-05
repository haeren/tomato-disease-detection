# Tomato Disease Detection
Tomato disease detection using 2D CNN on leaf images

## Dataset
Tomato leaf disease detection:
https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf

256x256 RGB images divided into 10 classes (Each class consists of 1100 samples):
- Bacterial Spot
- Early Blight
- Healthy
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites Two Spotted Spider Mite
- Target Spot
- Tomato Mosaic Virus
- Tomato Yellow Leaf Curl Virus

## Method
Transforms:
- Random Rotation (20)
- Random Horizontal Flip

Data Split:
- Train 80%
- Validation 10%
- Test 10%

Network Architecture:
- 256x256x3 image ->
- Conv 2D (16, (3,3)) -> ReLU -> Max Pooling (2,2) ->
- Conv 2D (32, (3,3)) -> ReLU -> Max Pooling (2,2) ->
- Conv 2D (64, (3,3)) -> ReLU -> Max Pooling (2,2) ->
- Conv 2D (128, (3,3)) -> ReLU -> Max Pooling (2,2) ->
- Conv 2D (256, (3,3)) -> ReLU -> Max Pooling (2,2) ->
- Fully Connected (256) -> Dropout (0.25) -> Fully Connected (10) ->
- Log Softmax -> Class Label

Parameters:
- Batch size = 32
- Criterion = NLLLOSS (The negative log likelihood loss)
- Optimizer = Adam
- Learning rate = 1e-3 (Scheduler step size = 10, gamma = 0.9)
- Epoch = 100
- Patience = 10

## Results
Early-stopped after the 65th epoch.
The best validation loss was achieved at 55th epoch.

| Metric | Value |
| --- | --- |
| Train Loss | 0.04263541102409363 |
| Validation Loss | 0.13380034267902374 |
| Test Loss | 0.11292929202318192 |
| Train Accuracy | 0.9867030382156372 |
| Validation Accuracy | 0.964545488357544 |
| Test Accuracy | 0.9745454788208008 |

## Dependencies
Modules:
- Numpy
- PyTorch
- Matplotlib
- Scikit-Learn

Optional:
- CUDA Toolkit (GPU for faster training)

## Reference
- Trivedi, N. K., Gautam, V., Anand, A., Aljahdali, H. M., Villar, S. G., Anand, D., ... & Kadry, S. (2021). Early Detection and Classification of Tomato Leaf Disease Using High-Performance Deep Neural Network. Sensors, 21(23), 7987.
