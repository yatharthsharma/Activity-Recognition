import siganalysis as sa
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import math
from scipy.fftpack import *
import scipy



data_path = 'C:/Python27/features_unnormal_final2.csv'



file_data = np.loadtxt(data_path,delimiter=',')

data =[]
final_data= []
target_data = []

valmean_nor = ((file_data[:,0]) - min(file_data[:,0]))/(max(file_data[:,0]) - min(file_data[:,0]))
valmax_nor = ((file_data[:,1]) - min(file_data[:,1]))/(max(file_data[:,1]) - min(file_data[:,1]))
valmin_nor = ((file_data[:,2]) - min(file_data[:,2]))/(max(file_data[:,2]) - min(file_data[:,2]))
valstd_nor = ((file_data[:,3]) - min(file_data[:,3]))/(max(file_data[:,3]) - min(file_data[:,3]))
valenergy_nor = ((file_data[:,4]) - min(file_data[:,4]))/(max(file_data[:,4]) - min(file_data[:,4]))
energy_signal_nor = ((file_data[:,5]) - min(file_data[:,5]))/(max(file_data[:,5]) - min(file_data[:,5]))


for i ,val in enumerate(valmean_nor):
    saveFile = open ('features_normal_final2.csv','a')
    saveFile.write(str(valmean_nor[i]) + ',' +str(valmax_nor[i]) + ',' + str(valmin_nor[i]) + ',' + str(valstd_nor[i]) + ',' + str(valenergy_nor[i])+','+ str(energy_signal_nor[i]) + ',' + str(file_data[i][6]))
    saveFile.write('\n')
    saveFile.close()
