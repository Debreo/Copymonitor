# Copymonitor
Monitor a directory and copy the files that match the parameters. 
This script will monitor changes to the directory and look for exe's, dll's and msi's that are added to the directory during an infection. 
Most malicious executables will delete itself and their compeonents after execution. This script will allow the user to copy these files 
before the deletion takes place. 


In order to use the script the python library watchdog must be installed.

pip install watchdog 

To execute the script

python copymon.py 
