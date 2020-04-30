#  **pivot-points**
Automatically sets up pivot points for thinkorswim

## **What is this?**
I needed a tool to fetch data from a website and calculate some values. And plot the values on graphs within ThinkOrSwim.
*At the moment the only way to plot the pivot points is to manually update the file in TOS each day.*

## **How to use it:**
*Dependencies:*
- Git
- Python 3
   - Pip
- ThinkOrSwim

### **Downloading/Installation**
Cloning Repo (Using OS Shell)
```
git clone https://github.com/dannydiaz17/pivot-points.git
cd pivot-points
```
Linux or MacOS (Run the python script)
```
python pivot_points.py
```
Windows
```
\.pivot_points.py
```

After running > python pivot_points.py, a pivotsSTUDY.ts file will be created in the same directory.
Add the pivotsSTUDY.ts file to TOS

> If you get a ModuleNotFoundError: No module named 'requests'
> or any similar Error, make sure you have pip installed. 
> Or it may just need an update.
> Run this command in shell

Windows
```
python -m pip install -U pip
```

## To do:

- [ ] Make shortcut to run script and start TOS
- [ ] Add more precise scraping
- [ ] Get pivotsSTUDY.ts to update automatically in TOS
- [ ] Make Windows Installer?
