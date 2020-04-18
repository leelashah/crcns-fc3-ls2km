# Data Retrieval

This project uses the PFC-5 dataset from the crcns.org database. This dataset contains human scalp EEG data collected from 14 patients with unilateral prefrontal cortex lesions and 20 ag- and education-matched, healthy controls. Below are instructions for downloadin a .gz folder for each of the 34 subjects.

Access data from the link https://portal.nersc.gov/project/crcns/download/index.php. This is a link to the PFC-5 dataset in the repository and will bring you to a list of folders. Under the "data" folder, download the files "ctrl01.tar.gz" and "pfc01.tar.gz". These are the files that were used in our analyses. Note that a CRCNS login is required to access these files, but a free account can be created by following this link: https://crcns.org/register.

To unpack the files, open a console in your anaconda environment of choice. Making sure that you set the path to the folder in which your files are saved, use the command tar -zxvf "data" to unpack the files, replacing the word "data" with the name of the file of interest.
    
