#  **stock-points**
Automatically sets up pivot points for thinkorswim

## **What is this?**
I needed a tool to fetch data from a website and calculate some values. And plot the values on graphs within ThinkOrSwim.
*At the moment the only way to plot the pivot points is to manually update the file in TOS each day.*

## **How to use it:**
*Dependencies:*
- Git
- Python 3
   - pip
      - requests
- ThinkOrSwim

### **Downloading/Installation**
Cloning Repo (Using OS Shell)
```
git clone https://github.com/dannydiaz17/pivot-points.git
cd pivot-points
```
Run the python script
```
python pivot_points.py
```

After running > python stock_points.py, {product}_STUDY.ts files will be created in the default 'Documents' directory from the 'watchlist' variable.
##### Default 'Documents' directory is /home/{Your_Username}/Documents on Linux,
      /Users/{Your_Username}/Documents on Mac, and 
      C:\Users\{Your_Username}\Documents\ on Windows

Add the pivotsSTUDY.ts file to TOS

> If you get a ModuleNotFoundError: No module named 'requests'
> or any similar Error, make sure you have pip installed.
> Also make sure pip is up to date and you have the necessary modules installed via pip
## Useful Shell Commands:

```
python -m pip install -U pip    #Installs 'pip'

python -m pip install requests  #Installs 'requests' module via pip
```

## Color Codes for Price Levels

Resistance  -  Orange

Support     -  Purple

Open        -  White

Close       -  Gray

High        -  Green

Low         -  Red


## To do:

- [ ] Make shortcut to run script and start TOS
- [ ] Add more precise scraping
- [ ] Get pivotsSTUDY.ts to update automatically in TOS
- [ ] Make Windows Installer?
