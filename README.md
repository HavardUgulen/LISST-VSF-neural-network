# LISST-VSF-neural-network

This neural network (NN) is developed to correct LISST-VSF measurements for multiple scattering errors. The input to the NN is the measured VSF and the output is the corrected VSF. It is important that the input VSF is processed in a specific way, so that it is similar to the training data. 

You can correct multiple VSFs simultaneously, where the input VSFs should be arranged in a matrix of the form 168xNrOfSamples (see example file).
