#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:26:43 2020

@author: bravo-z6
"""
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydicom
import os
import cv2 as cv
from scipy import stats

path = "/media/bravo-z6/Shared/_Dataset/_DICOM_7SERIES/fase_2_path.csv"

data = pd.read_csv(path)

list_names =[]
dim_a = []
dim_b = []
for i in range(len(data)): 
    for idx, file_name in enumerate(os.listdir(data.iloc[i][0])):
        print(file_name)
        print('---------------')
        imag = pydicom.dcmread(data.iloc[i][0] + '/' + file_name)
        dim = np.shape(imag.pixel_array)
        dim_a.append(dim[0])
        dim_b.append(dim[1])
mode_dim_a = stats.mode(np.asarray(dim_a))
mode_dim_b = stats.mode(np.asarray(dim_b))      
