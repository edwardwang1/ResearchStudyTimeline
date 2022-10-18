# Installation Instructions
## Requirements
1. [Anaconda](https://www.anaconda.com/products/distribution) (Newest version should be fine)
2. Run the installer and follow the instructions (Check Yes when prompted about adding Anaconda to PATH)

## Create a python virtual environment (instructions for Anaconda shown)
1. `conda create -n timeline python=3.8`
2. `conda activate timeline` or `activate timeline`
3. `pip install flask`
4. `pip install pandas`

## Running App
1. Open command prompt
2. Use the following command to change into the directory: `cd Directory`
3. Activate virtual environment with `conda activate timeline`
4. Run `flask --app timeline run`
