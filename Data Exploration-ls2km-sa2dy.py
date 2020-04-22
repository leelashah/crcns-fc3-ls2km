#!/usr/bin/env python
# coding: utf-8

# In[146]:


import mne
import matplotlib.pyplot as plt
import numpy as np
import os
import os.path
#import sklearn
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs,
                               corrmap)


# In[147]:


#loaded the data
def load_data(filename):
    data_folder = os.path.join("data", filename)
    file_to_open = os.path.join(data_folder, "data_primary.bdf")
    raw = mne.io.read_raw_bdf(file_to_open, eog=None, misc=None, stim_channel='auto', exclude= 'None', preload=False, verbose=None)
    return raw 

filename = "ctrl01"
raw = load_data("ctrl01")
print(raw)
print(raw.info)
raw.crop(tmax=54.022)


# In[148]:


#visualize the data
def psd_plot(data, duration=5, n_channels =30):
  data.plot_psd()
  data.plot(duration=duration, n_channels=n_channels)
data = raw
psd_plot(data)


# In[149]:


#remove bad channels
def exclude_bad_channels(data,bad_channels):
    data.info['bads'].extend(bad_channels)
    good_eeg = mne.pick_types(raw.info, meg=False, eeg = True)
    all_eeg = mne.pick_types(raw.info, meg=False, eeg=True, exclude=[])
    return(good_eeg, all_eeg)
drop = ['P9', 'Fpz','Fz']
good_eeg, all_eeg = exclude_bad_channels(raw, drop)


# In[150]:


#filtering data to remove slow drifts
raw.plot(duration=5, n_channels=30)
raw.load_data().filter(l_freq=1, h_freq=40)
raw.plot(duration=5, n_channels=10)


# In[151]:


#fit the ICA
ica = ICA(n_components=10, random_state=97)
ica.fit(raw,start=0.0, stop=5.0)
ica.plot_sources(raw)


# In[152]:


#visualize different ICA components
ica.plot_overlay(raw, exclude=[1], picks='eeg')
ica.plot_overlay(raw, exclude=[7], picks='eeg')
ica.plot_overlay(raw, exclude=[8], picks='eeg')


# In[153]:


#apply the ICA
raw.plot(duration=5, n_channels=20)
ica.exclude = [1,7,8]
ica.apply(raw)
raw.plot(duration=5, n_channels=20)


# In[154]:


#plot the data again
data = raw
psd_plot(data)


# In[155]:


#do the same for the pfc patient dataset

#load the data
filename = "pfc02"
raw2 = load_data("pfc02")
print(raw2)
print(raw2.info)
raw2.crop(tmin=980,tmax=1000)

#plot the data
data = raw2
psd_plot(data)

#no bad channels in this data set

#filtering data to remove slow drifts
raw2.plot(duration=5, n_channels=10)
raw2.load_data().filter(l_freq=1, h_freq=40)
raw2.plot(duration=5, n_channels=10)


# In[156]:


#fit the ICA
ica = ICA(n_components=15, random_state=97)
ica.fit(raw2)
ica.plot_sources(raw2)


# In[157]:


#visualize different ICA components
ica.plot_overlay(raw2, exclude=[0], picks='eeg')
ica.plot_overlay(raw2, exclude=[7], picks='eeg')


# In[158]:


#apply the ICA
raw2.plot(duration=5, n_channels=20)
ica.exclude = [0,7]
ica.apply(raw2)
raw2.plot(duration=5, n_channels=20)


# In[159]:


#compare the two
raw.plot(duration=5, n_channels=20)
raw2.plot(duration=5, n_channels=20)

