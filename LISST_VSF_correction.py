





import numpy as np
from matplotlib import pyplot as plt
import math
import scipy.integrate as integrate

pi=math.pi

nrOfInputs=158
layers=4

#######   Path to directory containing model

Filepath = 'Insert path do directory'

#######   import transformation values   ########

avg_in=np.loadtxt(Filepath + "/avg_in.txt")
avg_out=np.loadtxt(Filepath + "/avg_out.txt")
std_in=np.loadtxt(Filepath + "/std_in.txt")
std_out=np.loadtxt(Filepath + "/std_out.txt")

###### Import angles #######

angles=np.loadtxt(Filepath + "/Angles.txt")

#####  Path and file containg input VSF     #########
    
VSF_matrix=np.loadtxt(Filepath + "VSF_example.txt")
input_matrix=VSF_matrix[0:158,:]   ##### Only want input VSF up to 140 degrees


nrOfSamples=len(input_matrix[0])    


######## Apply transformation   ##########

input_matrix=np.log(input_matrix)
input_matrix=input_matrix.transpose()
input_matrix=(input_matrix-avg_in)/std_in

#####  Import weights and bias   ###########

W=[]
B=[]

for i in range (layers):
    W.append(np.loadtxt('Weights_'+str(i+1)+'.txt'))
    B.append(np.loadtxt('Bias_'+str(i+1)+'.txt'))

########   Neural network correction funtion   ##########

def activation(x):

    data = [math.tanh(value) for value in x] #0.5*(np.exp(value)-1) 

    return np.array(data, dtype=float)


def predict(input_matrix, layers, W, B):
        layer=input_matrix
        for i in range(layers): 
            if i==layers-1:
#                    print(len(layer))
                layer=np.dot(layer, W[i]) + B[i]
#                    print(np.dot(layer, W[i]) + B[i])
            else:
                layer = activation(np.dot(layer, W[i]) + B[i])
#                print(len(layer))
            
        prediction = layer
        
        return prediction        

        
###### Make correction  #####
        
prediction=[]    
    
for sample in range(nrOfSamples):        
    prediction.append(predict(input_matrix[sample], layers, W, B))

    
######### Apply reverse transformation    #############    
    
prediction=np.array(prediction) 
prediction=prediction.reshape(nrOfSamples, 168)

prediction=prediction*std_out+avg_out
prediction=np.exp(prediction)
prediction=prediction.transpose()

############# Make Figure ##############

fig, ax = plt.subplots()
ax.plot(angles, VSF_matrix[:,:], 'r', label='A')
ax.plot(angles, prediction[:,:], 'b', label='B')

y_label=ax.set_ylabel('VSF ['r'$m^{-1}sr^{-1}$]')
x_label=ax.set_xlabel(r'$\theta$ ''[degrees]')

handles, labels = ax.get_legend_handles_labels()
display = (0,nrOfSamples)
ax.legend([handle for i,handle in enumerate(handles) if i in display],['LISST-VSF', 'ANN'], loc=2)
plt.yscale('log')

x_label.set_fontsize(22)
y_label.set_fontsize(22)
ax.set_ylim(10**(-5), 10**6)
ax.set_frame_on(True)

plt.show()

################ Calculated scattering and backscattering coefficients #############   
 
ang_rad=angles*(pi/180)
ang_bb=ang_rad[107::]

b_all=np.zeros([nrOfSamples,2])
bb_all=np.zeros([nrOfSamples,2])
VSF_all_err=np.zeros([nrOfSamples,2])

for sample in range(0,nrOfSamples):

    b_all[sample,0]=(integrate.trapz(np.multiply(VSF_matrix[:,sample],2*pi*np.sin(ang_rad)), ang_rad))
    b_all[sample,1]=(integrate.trapz(np.multiply(prediction[:,sample],2*pi*np.sin(ang_rad)), ang_rad))

    bb_all[sample,0]=(integrate.trapz(np.multiply(VSF_matrix[107::,sample],2*pi*np.sin(ang_bb)), ang_bb))
    bb_all[sample,1]=(integrate.trapz(np.multiply(prediction[107:,sample],2*pi*np.sin(ang_bb)), ang_bb))



print(str(b_all))
print(str(bb_all))
