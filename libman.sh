#!/bin/bash

# Function to activate the virtual environment
activate_venv() {
    echo "Activating virtual environment..."
    source venv/bin/activate
}

# Function to deactivate the virtual environment
deactivate_venv() {
    echo "Deactivating virtual environment..."
    deactivate
}

# Function to check if tkinter is installed (specifically for Linux)
check_tkinter() {
    python -c "import tkinter" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "Tkinter is not installed. Installing Tkinter..."
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            # On Linux, we need to install Tkinter via package manager
            sudo apt-get install python3-tk -y
        else
            echo "Tkinter should be installed by default on MacOS and Windows."
        fi
    else
        echo "Tkinter is already installed."
    fi
}

# Function to check if Pillow is installed and install it if necessary
check_pillow() {
    python -c "import PIL" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "Pillow is not installed. Installing Pillow..."
        pip install Pillow
        if [ $? -ne 0 ]; then
            echo "Error: Failed to install Pillow."
            exit 1
        fi
    else
        echo "Pillow is already installed."
    fi
}

# Interactive prompt to proceed
echo "Welcome to the LibMan System setup!"
read -p "Do you want to set up the virtual environment and run the application? (y/n): " choice

if [[ "$choice" != "y" && "$choice" != "Y" ]]; then
    echo "Exiting the setup. Goodbye!"
    exit 0
fi

# Step 1: Check for libman.py script
if [ ! -f "libman.py" ]; then
    echo "Error: libman.py not found in the current directory."
    echo "Please ensure libman.py is in the same directory as this script."
    exit 1
fi

# Step 2: Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating a new virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        exit 1
    fi
    echo "Virtual environment created successfully."
else
    echo "Virtual environment already exists."
fi

# Step 3: Activate the virtual environment
activate_venv

# Step 4: Upgrade pip and install dependencies
echo "Upgrading pip..."
pip install --upgrade pip

# Step 5: Check and install Tkinter if necessary
check_tkinter

# Step 6: Check and install Pillow if necessary
check_pillow

# Step 7: Run libman.py
echo "Running libman.py..."
python libman.py
if [ $? -ne 0 ]; then
    echo "Error: Failed to run libman.py."
    deactivate_venv
    exit 1
fi

# Step 8: Deactivate virtual environment after closing the GUI
deactivate_venv

echo "Thank you for using the LibMan System!"
