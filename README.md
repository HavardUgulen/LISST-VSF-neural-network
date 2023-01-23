# LISST-VSF-neural-network


This neural network (NN) is developed to correct LISST-VSF measurements for multiple scattering errors. The input to the NN is the measured VSF and the output is the corrected VSF. 

Scripts to run the NN are found in the main folder titled "LISST_VSF_correction.py" (for python) and "LISST_VSF_correction.m" (for MATLAB). 

The NN model is found in the folder "NeuralNetwork". It contains the weights, biases, angles, transformation values, and an example VSF matrix called "VSF_example". 

You can correct multiple VSFs simultaneously, where the input VSFs should be arranged in a matrix of the form 168xNrOfSamples (see example file "VSF_example"). The NN only uses the first 158 measurement points (0.09-140 degrees) as inputs, but loading the VSF for all 168  measurement points (0.09-150 degrees) enables plotting of the input VSFs and calculation of their scattering coefficients. 

Example: 

The example file "VSF_example" contains VSFs for a sample simulated with scattering coefficients b = [0.05, 0.17, 0.55, 1.8, 6.0, 20.0, 30.0, 40.0, 50.0]. The input VSF file is formated in a 168x9 matrix (9 samples with 168 measurement points per sample).  The output of the NN for these VSFs should have similar (not identical) scattering coefficients to those used to simulate the VSFs, i.e., b = [0.05, 0.17, 0.55, 1.8, 6.0, 20.0, 30.0, 40.0, 50.0]. The input VSFs should have scattering coefficients b = [0.05, 0.17, 0.57, 2.03, 9.9, 93.2, 336, 1129, 3730]. If you get these numbers, the script is working properly. 

Input data:

The measured VSFs used as input data to the model should be processed in the following way to obtain VSF input data that is similar to the training data.

