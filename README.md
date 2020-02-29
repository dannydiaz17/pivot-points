#  **pivot-points**
Automatically sets up pivot points for thinkorswim

## **What is this?**
I needed a tool to fetch data from a website and calculate some values. And plot the values on graphs within ThinkOrSwim.
*At the moment the only way to plot the pivot points is to manually update the file in TOS each day.*

## **How to use it:**
*Dependencies:*
- Git
- Python 3
- ThinkOrSwim

### **Downloading/Installation**
Using CMD / Terminal
```
git clone https://github.com/dannydiaz17/pivot-points.git
cd pivot-points
python pivot-points.py
```
After running > python pivot-points.py, a pivotsSTUDY.ts file will be created in the same directory.
Add the pivotsSTUDY.ts file to TOS

> Within TOS: Charts > Studies > Edit Studies... > Import... > "Select pivotsSTUDY.ts file"


## To do:

- [ ] Make shortcut to run script and start TOS
- [ ] Add more precise scraping
- [ ] Get pivotsSTUDY.ts to update automatically in TOS
- [ ] Make Windows Installer?
