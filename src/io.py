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
    from crcns.org using the mne package. The argument is the name of the data file (ex: "ctrl01")
    """
    data_folder = os.path.join("data", filename)
    file_to_open = os.path.join(data_folder, "data_primary.bdf")
    raw = mne.io.read_raw_bdf(file_to_open, eog=None, misc=None, stim_channel='auto', exclude= 'None', preload=False, verbose=None)
    return raw 
  
def exclude_bad_channels(data,bad_channels):
    """
    This function marks bad channels, as specified by the user, so that future mne functions will ignore these channels in calculations.
    The arguments are data (the name of the data returned using the load_data function) and bad_channels (a list of bad channels as
    identified by the user). The function returns a list of the channel numbers that that are good (good_eeg) and a list of all of the
    channel numbers (all_eeg). Note that these lists are the indexes of the channels in order, not the names of the channels.
    """  
    data.info['bads'].extend(bad_channels)
    good_eeg = mne.pick_types(data.info, meg=False, eeg = True)
    all_eeg = mne.pick_types(data.info, meg=False, eeg=True, exclude=[])
    return(good_eeg, all_eeg)
  
def psd_plot(data,duration=5, n_channels=30):
    """
    This function uses the MNE package to first plot the data for a given duration and number of channels, then plots a power spectral 
    density plot of the loaded data. The required argument is the name of the data returned using the load_data function. The optional
    arguments are duration (the length of data that is desired to be plotted) and n_channels (the number of channels desired to plot,
    starting at the first channel). The default values for duration n_channels are 5 and 30, respectively.
    """  
    data.plot(duration=duration, n_channels=n_channels)
    data.plot_psd()

def filter(data,duration=5,n_channels=10,l_freq=1,h_freq=None):
    """
    This function uses the MNE package to filter the data. The required argument data is the name of the data returned using the
    load_data function, and optional arguments are duration (the length of the desired segment of data), n_channels (the number of  
    channels from the data set to which to apply the filter; beginning from the first channel), l_freq (the lowest frequency of data 
    to include), and h_freq (the highest frequency of data to include. If these values are not included when calling the function, 
    the values of 5, 10, 1, and 40 are used, for the respective optional arguments. The function plots the raw data, then applies the
    filer and plots the filtered data.
    """      
    data.plot(duration=duration, n_channels=n_channels)
    data.load_data().filter(l_freq=l_freq, h_freq=h_freq)
    data.plot(duration=duration, n_channels=n_channels)
    
def ica_fit(data,components):
    """
    This function uses the MNE package to implement the first step of independent component analysis (ICA), which is a tool to remove
    artifacts from the data. The required arguments are data(the name of the data returned using the load_data function), and
    components (the number of components from the principal component analysis (PCA) to use). Begin at a low number (about 15)
    for components; then, if artifacts in the ICA are still not visible, increase the number. The function fits the ICA to the data, 
    then plots a time series of the ICA components.
    """  
    ica = ICA(n_components=components, random_state=97)
    ica.fit(data)
    ica.plot_sources(data)
    return(ica)
    
def ica_apply(data,ica,exclude,duration=5,n_channels=20):
    """
    This function uses the IC components chosen by the user that contain artifacts to apply ICA to the data, to remove those same
    artifacts from the data. The required arguments are data (the name of the data returned using the load_data function) and
    exclude (a list of the IC components chosen by the user to contain artifacts). The optional components are duration
    (the duration of data to visualize) and n_channels (the number of channels to visualize). The defaults for these values are 5 and
    20, respectively. The function applies the ICA using the given exclusions, then plots the resulting data. 
    """  
    data.plot(duration=duration, n_channels=n_channels)
    ica.exclude = exclude
    ica.apply(data)
    data.plot(duration=5, n_channels=20) 
    
