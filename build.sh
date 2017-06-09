



# Create a python environment for firebeard:
source deactivate firebeard
conda env remove --name firebeard
conda env create --name firebeard --file ./anaconda/environment.yml
source activate firebeard
conda env update --name firebeard --file ./anaconda/environment.yml
