## LISST-VSF-neural-network

If you have any problems, please contact me at haavardugulen@gmail.com

#### General information

This neural network (NN) is developed to correct LISST-VSF measurements for multiple scattering errors. The input to the NN is the measured VSF and the output is the corrected VSF. 

Scripts to run the NN are found in the main folder titled "LISST_VSF_correction.py" (for python) and "LISST_VSF_correction.m" (for MATLAB). 

The NN model is found in the folder "NeuralNetwork". It contains the weights, biases, angles, transformation values, and an example VSF matrix called "VSF_example". 

You can correct multiple VSFs simultaneously, where the input VSFs should be arranged in a matrix of the form 168xNrOfSamples (see example file "VSF_example"). The NN only uses the first 158 measurement points (0.09-140 degrees) as inputs, but loading the VSF for all 168  measurement points (0.09-150 degrees) enables plotting of the input VSFs and calculation of the scattering coefficients. 

Further information about the neural network is provided in [1]. 


#### Example 

The example file "VSF_example" contains VSFs for a sample simulated with scattering coefficients b = [0.05, 0.17, 0.55, 1.8, 6.0, 20.0, 30.0, 40.0, 50.0]. The input VSF file is formated in a 168x9 matrix (9 samples with 168 measurement points per sample). If the script is working properly, the following scattering coeffcients should be obtained from the example:  

Input: b $\approx$ [0.05, 0.17, 0.57, 2.03, 9.9, 93.2, 336, 1129, 3730]. 

Output: b $\approx$ [0.05, 0.17, 0.55, 1.8, 6.0, 20.0, 30.0, 40.0, 50.0]

This example dataset is included in the training data, hence the accuaracy. 

#### Input data

In order for the model to produce reliable results, the measured VSFs used as input data to the model should be processed following the steps described in [2]. 



1. Håvard S. Ugulen, Daniel Koestner, Håkon Sandven, Børge Hamre, Arne S. Kristoffersen, and Camilla Saetre, "Neural network approach for correction of multiple scattering errors in the LISST-VSF instrument," Opt. Express 31, 32737-32751 (2023)

2. Lianbo Hu, Xiaodong Zhang, Yuanheng Xiong, and Ming-Xia He, "Calibration of the LISST-VSF to derive the volume scattering functions in clear waters," Opt. Express 27, A1188-A1206 (2019)
