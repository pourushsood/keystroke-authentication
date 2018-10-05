# Keystroke authentication #
Authenticates a user based on his keystroke patterns on a keyboard.

The data is provided as hold times for individual keys, and latencies between any and all pairs of consecutive key presses. These two quantities are treated as features. So there could be a maximum of 26+26x26 features. There could be less if the user does not use some pairs of letters consecutively (for latencies) or does not use some letters at all (for hold times). 

# Folders #
## data preparation ##

This folder contains code for the preparation of data.
* *common_feature_subset.py* - finds the common subset of all available features (hold times and latencies)


## classification ##

This folder contains code for training multiple one class SVMs for authentication of the data of each user
* *one_class_svm.py* - implements one class svm using Radial Basis Function (RBF) of one user and then classifies over other data. This is implemented using Five fold cross validation.
