# -*- coding: utf-8 -*-
# -*- mode: python -*-

"""packages to import"""
import mne
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)

"""Functions for file IO"""


def load_data(filename):
    """
    This function loads the .bdf file containing the eeg data collected from a given subject from the data set PFC-5.
    from crcns.org using the mne package. The argument is the name of the data file (ex: "ctrl01").
    """
    data_folder = os.path.join("data", filename)
    file_to_open = os.path.join(data_folder, "data_primary.bdf")
    raw = mne.io.read_raw_bdf(file_to_open, eog=None, misc=None, stim_channel='auto', exclude= 'None', preload=False, verbose=None)
    return raw 

def psd_plot(data):
    """
    This function uses the MNE package to plot the loaded data. The argument is the name of the data returned using the load_data
    function
    """  
    data.plot_psd()
    data.plot(duration=5, n_channels=30)

def filter(data,duration=5,n_channels=10,l_freq=1,h_freq=40):
    """
    This function uses the MNE package to filter the data. The required argument data is the name of the data returned using the
    load_data function, and optional arguments are duration (the length of the desired segment of data), n_channels (the number of  
    channels from the data set to which to apply the filter; beginning from the first channel), l_freq (the lowest frequency of data 
    to include), and h_freq (the highest frequency of data to include. If these values are not included when calling the function, 
    the values of 5, 10, 1, and 40 are used, for the respective optional arguments.
    """      
    data.plot(duration=5, n_channels=10)
    data.load_data().filter(l_freq=1, h_freq=40)
    data.plot(duration=5, n_channels=10)
