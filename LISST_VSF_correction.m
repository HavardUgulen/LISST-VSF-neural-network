
%%%% Path to folder

Path='\\hallingskeid.uib.no\hug043\Documents\MonteCarlo\LISST_VSF\LISST_correction\Neural\NeuralNetwork\';

%%%%%%%% VSF to be corrected

VSF = readmatrix('\\hallingskeid.uib.no\hug043\Documents\MonteCarlo\LISST_VSF\LISST_correction\Neural\Koestner\DilCor\Lagoon_pro.txt');
numberOfSamples=length(VSF(1,:));
%%%%LISST-VSF angles

Angles=readmatrix(sprintf('%sAngles.txt',Path));

%%%% Load weights and biases

%%%% Weights

W{1}=readmatrix(sprintf('%sWeights_1.txt',Path));
W{2}=readmatrix(sprintf('%sWeights_2.txt',Path));
W{3}=readmatrix(sprintf('%sWeights_3.txt',Path));
W{4}=readmatrix(sprintf('%sWeights_4.txt',Path));

%%%%% Bias

B{1}=readmatrix(sprintf('%sBias_1.txt',Path));
B{2}=readmatrix(sprintf('%sBias_2.txt',Path));
B{3}=readmatrix(sprintf('%sBias_3.txt',Path));
B{4}=readmatrix(sprintf('%sBias_4.txt',Path));



%%%% Transformation values

avg_in=readmatrix(sprintf('%savg_in.txt',Path));
avg_out=readmatrix(sprintf('%savg_out.txt',Path));
std_in=readmatrix(sprintf('%sstd_in.txt',Path));
std_out=readmatrix(sprintf('%sstd_out.txt',Path));

%%%%% Transform input

VSF_input=VSF(1:158,:);    %%%%% Only want input for angles up to 140 degree

VSF_input=log(VSF_input);
VSF_input=(VSF_input-avg_in)./std_in;



%%%%% Make correction
layer=VSF_input;
for i=1:4
    Weights=W{i};
    Bias=B{i};
    new_layer=zeros(length(Bias), length(layer(1,:)));

    if i==4
        for j=1:length(layer(1,:))
            for k=1:length(Bias)
                new_layer(k,j)=dot(layer(:,j),Weights(:,k))+Bias(k);
            end
        end
    else
        for j=1:length(layer(1,:))
            for k=1:length(Bias)
                new_layer(k,j)=tanh(dot(layer(:,j),Weights(:,k))+Bias(k));
            end
        end    
    end
    layer=new_layer;

end

Prediction=layer;


%%%%%  Transform prediction

Prediction = Prediction .* std_out + avg_out;
Prediction = exp(Prediction);

%%%% Calculate scattering and backscattering coefficient

b_LISST=[];
bb_LISST=[];
b_NN=[];
bb_NN=[];
Angles_rad=Angles*pi/180;

for i=1:numberOfSamples
    
    %%%% LISST
    
    b_LISST = [b_LISST 2*pi*trapz(Angles_rad(1:168), VSF(1:168,i).*sin(Angles_rad(1:168)))];
    bb_LISST = [bb_LISST 2*pi*trapz(Angles_rad(108:168), VSF(108:168,i).*sin(Angles_rad(108:168)))];
    
    %%%% Neural network
    
    b_NN = [b_NN 2*pi*trapz(Angles_rad(1:168), Prediction(1:168,i).*sin(Angles_rad(1:168)))];
    bb_NN = [bb_NN 2*pi*trapz(Angles_rad(108:168), Prediction(108:168,i).*sin(Angles_rad(108:168)))];
end

%%%% Plot

figure();
    hold on;

    Pred=plot(Angles(1:length(Prediction)), Prediction,'Color',[0.7 0 0],'LineWidth', 1);
    LISST=plot(Angles(1:length(VSF)), VSF,'Color',[0 0 0],'LineWidth', 1);

    set(gca, 'YScale', 'log')
    xlabel('\theta (degrees)') 
    ylabel('VSF (m^{-1} sr^{-1})')
    legend([Pred(1), LISST(1)],{'Prediction', 'LISST-VSF'})

    box on;
