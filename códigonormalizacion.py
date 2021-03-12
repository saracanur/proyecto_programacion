import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydicom
import os
import cv2 as cv


print('sara')

path = "/media/bravo-z6/Shared/_Dataset/_DICOM_7SERIES/fase_2_path.csv"

data = pd.read_csv(path)
error = []
list_names =[]

for i in range(len(data)): 
    if data.iloc[i][0].split('/')[7] == 'DICOM_7SERIES_IV':
        os.mkdir('/media/bravo-z6/Shared/_Experiments/_Sara/Exp_ex/Imagenes_nuevas_dimensiones/' + 'Fase 2_' + data.iloc[i][0].split('/')[8])
    else:
        os.mkdir('/media/bravo-z6/Shared/_Experiments/_Sara/Exp_ex/Imagenes_nuevas_dimensiones/' + 'Fase 2_' + data.iloc[i][0].split('/')[7])
    for idx, file_name in enumerate(os.listdir(data.iloc[i][0])):
        print(file_name)
        print('---------------')
        imag = pydicom.dcmread(data.iloc[i][0] + '/' + file_name)
        #plt.imshow(imag.pixel_array, cmap = plt.cm.gray)
        imag_new = cv.resize(imag.pixel_array, (480,480))
        #print(imag_new.pixel_array)
        dim = np.shape(imag_new)
        
        if dim != (480,480):
           error.append(file_name) 
        
        
        """
        dim = np.shape(imag.pixel_array)
        imag_zeros = np.zeros(shape = (dim[0],dim[1]))
        imag_norml = cv.normalize(imag.pixel_array, imag_zeros, 0, 255, cv.NORM_INF) 
        """
        if data.iloc[i][0].split('/')[7] == 'DICOM_7SERIES_IV':
            name = '/media/bravo-z6/Shared/_Experiments/_Sara/Exp_ex/Imagenes_nuevas_dimensiones/' +  'Fase 2_' + data.iloc[i][0].split('/')[8] + '/' + file_name[0:-4]+ '_normalizada.npy'
        else:
            name = '/media/bravo-z6/Shared/_Experiments/_Sara/Exp_ex/Imagenes_nuevas_dimensiones/' + 'Fase 2_' + data.iloc[i][0].split('/')[7] + '/' + file_name[0:-4]+ '_normalizada.npy'
            
        np.save(name, imag_new)
        list_names.append(name)
        
data_dict = { "path" : list_names }
data_pd = pd.DataFrame.from_dict (data_dict)
data_pd.to_csv ("fase_2_path_norm.csv", index = False)


    
