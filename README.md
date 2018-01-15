# Track Prediction with Kalman Filter, K-NN and LSTMs

The actual Data set can be download from KITTI datasets. Below are the sample output from each track prediction method. Postion of the obejct is estimated in the next frame using the position in the previous frames using Kalman Filter, K-NN and LSTMs. KNN and LSTMs were trained on some part of the dataset and model was saved and then it was tested on the remaining part of the dataset to test the models.
### Output from Kalman Filter
<p align="center">
  <img src="Kalman Filter-output.gif" alt="Track Prediction using Kalman Filter" />
</p>

### Output from K-Nearest Neighbors
<p align="center">
  <img src="K-Nearest-Neighbor-output.gif" alt="Track Prediction usingK-Nearest Neighbors" />
</p>

### Output from Long Short Term Memory model
<p align="center">
  <img src="LSTM-output.gif" alt="Track Prediction using LSTM" />
</p>

# References -
http://www.cvlibs.net/datasets/kitti/
