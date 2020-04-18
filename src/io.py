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

