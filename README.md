# Activity-Recognition

This project focuses on detecting user activity (Walking/Running) using smart phone's accelerometer 

# Please find below a brief overview of the work done. You can find the details in the report uploaded

Problem Statement :
Activity recognition ( Walking and Running ) using accelerometer data value from a smartphone.

Device Information :
The accelerometer in Android phones measures the acceleration of the device on the x (lateral), y (longitudinal),
and z (vertical) axes. Accelerometers can be used to detect movement and the rate of change of the speed of
movement. The data received from the accelerometer was in the form of a three-valued vector
of floating point numbers that represented the individual accelerations of the smartphone device in the X, Y, and Z
axes subtracted by the gravity vector G.


Features Extraction –
Six features were extracted based on the study of the previous works using a sample window of 256 samples with
50 % overlap. 

The features are as follows:
- Mean 
- Standard Deviation
- Maximum amplitude
- Minimum amplitude
- Energy Time domain
- Energy Frequency domainRunning

There were other features as mentioned in the papers – correlation , percentiles , zero crossing , log energy .Only
minimum needed features were selected in order to avoid the curse of dimensionality

Classifier :
K- nearest neighbor algorithm was used to classify the data in walking or running . K nearest neighbors is a simple
algorithm that stores all available cases and classifies new cases based on a similarity measure (e.g., distance
functions). A case is classified by a majority vote of its neighbors, with the case being assigned to the class most
common amongst its K nearest neighbors measured by a distance function. If K = 1, then the case is simply
assigned to the class of its nearest neighbor.
Distance – Euclidean distance : Sum(X i - Y i ) where Xi and Yi are the feature vectors.

