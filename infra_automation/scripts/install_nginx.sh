#!/bin/bash

LOG_FILE="infra_automation/logs/provisioning.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

if command -v nginx &> /dev/null; then
    log_message "Nginx is already installed."
    echo "Nginx is already installed."
    exit 0
fi

log_message "Nginx not installed installation in process ..."
if sudo apt-get update && sudo apt-get install -y nginx; then
    log_message "Nginx successfully installed."
    echo "Nginx successfully installed."
else
    log_message "Error: Failed to install Nginx."
    echo "Failed to install Nginx." >&2
    exit 1
fi
