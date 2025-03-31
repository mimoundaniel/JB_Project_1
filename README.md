# Infra Automation Project

> This project is to simulate create of virtual machines and install service (like Nginx) with Python and Bash.

## Project Overview

The project is for learn automation DevOps.  
We use Python for simulate VM creation, and Bash for install service.  
This script only simulate. It don’t create real VM.

## Project Structure



infra-automation/
├── scripts/               # content a bash script
│   └── install_nginx.sh
├── configs/               # content all machin (date file)
│   └── instances.json
├── logs/                  # content log file
│   └── provisioning.log
├── src/                   # content a ressource for my script 
│   └── machine.py        
├── infra_simulator.py     # a main script
├── requirements.txt       # a framwors list to need 
└── README.md


## Setup

1. Clone the repo:
   ```
   git clone https://github.com/JB-Devops-35690-2/mimoundaniel
   ```

2. Create a virtual env:
   ```
   python -m venv venv
   ```

3. Actvate the virtual env:
   ```
   source venv/Scripts/activate  
   ```

4. Install requirements:
   ```
   pip install -r requirements.txt
   ```

## Usge

Run the Python script to start the automation:
```
python infra_simulator.py
```


Then, answer the questions:
- Write name of machine
- Write OS 
- Write CPU number
- Write RAM 

After that, the script will save data in file: `configs/instances.json`  
Then, it try install Nginx with Bash script.


## Logs

All messages and errors go in file: `logs/provisioning.log`  
If something is broken, you can see the log.

## Features

- Ask user for VM info
- Check if info is correct
- Save machine in JSON
- Run Bash to install service
- Log actions and errors

## Future Plans
- Add AWS and Terraform integration.
- Improve error handeling.

