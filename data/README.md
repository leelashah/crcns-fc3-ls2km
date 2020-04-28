# Data Retrieval

This project uses the PFC-5 dataset from the crcns.org database. This dataset contains human scalp EEG data collected from 14 patients with unilateral prefrontal cortex lesions and 20 age- and education-matched, healthy controls. Below are instructions for downloading a .gz folder for each of the 34 subjects.

Access data from the link https://portal.nersc.gov/project/crcns/download/index.php. This is a link to the PFC-5 dataset in the repository and will bring you to a list of folders. Under the "data" folder, download the files "ctrl01.tar.gz" and "pfc01.tar.gz". These are the files that were used in our analyses. Note that a CRCNS login is required to access these files, but a free account can be created by following this link: https://crcns.org/register.

To unpack the files, open a console in your anaconda environment of choice. Making sure that you set the path to the folder in which your files are saved, use the command ```tar -zxvf "data"``` to unpack the files, replacing the word "data" with the name of the file of interest.

Clone this repository using the command: ```git clone https://github.com/leelashah/crcns-fc3-ls2km``` in your environment of choice. Make sure that the data is downloaded into the "data" folder of this new repository. Ensure that you have the packages listed in the "requirements.txt" file installed (or use the command: ```pip install -r requirements-conda.txt```). If you have problems installing the mne package, see this website for solutions: https://mne.tools/0.17/install_mne_python.html. Set the current directory to the location of your repository, then type the command: ```jupyter-notebook``` into the environment to open Jupyter-notebook. Run the code in the notebook "PSYC 5270 Final Data Exploration-ls2km-sa2dy" to replicate our results.
    
