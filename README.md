Python script to update the `icons.js` file every time a new icon is added to the `icons` directory

# Step by Step
1. install python3 (https://realpython.com/installing-python/)
2. 
```sh
pip3 install watchdog
```

3. Open the script 
4. Change the global variables to your context (`DIRECTORY_TO_WATCH`, `DIRECTORY_TO_ICON_FILE`)
5. 
```sh
python3 ./fileListener.py
```

> You can create a daemon to run the script on the OS startup
