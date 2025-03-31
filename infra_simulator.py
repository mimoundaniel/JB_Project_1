import json
import os
import subprocess
import logging
from infra_automation.src.machine import Machine
from pydantic import ValidationError

def save_data_in_json(data):
    config_dir = os.path.join("infra_automation", "configs")
    file_path = os.path.join(config_dir, "instances.json")

    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []
    else:
        existing_data = []

    existing_data.append(data)

    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)

def input_from_user():
    name = input("Enter a name of the device: ")
    os_type = input("Enter the OS: ")
    cpu = input("Enter a number of CPU: ")
    ram = input("Enter a number of RAM: ")
    logging.basicConfig(level=logging.INFO, filename='infra_automation/logs/provisioning.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        cpu = int(cpu)
        ram = int(ram)
    except ValueError:
        logging.error("Invalid input for CPU or RAM. They must be integers.")
        print("Error: CPU and RAM must be integers.")
        return None

    try:
        machine = Machine(name=name, os=os_type, cpu=cpu, ram=ram)
        return machine.to_dict()
    except ValidationError as e:
        logging.error(f"Validation error: {e}")
        print(f"Validation error: {e}")
        return None

def run_bashfile():
    script_path = os.path.join(os.getcwd(), "infra_automation", "scripts", "install_nginx.sh")

    if not os.path.exists(script_path):
        print(f"Script {script_path} not found!")
        return False

    result = subprocess.run(script_path, shell=True)

    if result.returncode == 0:
        print("Nginx installation successful.")
        return True
    else:
        print("Error while running bash script.")
        return False

vm_data = input_from_user()

if vm_data:
    save_data_in_json(vm_data)
    print("Machine created successfully.")

    if run_bashfile():
        print("Nginx installation completed successfully.")
    else:
        print("Nginx installation failed.")
