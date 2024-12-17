# Cisco Switch Command Logger

This project provides a Python script (`run.py`) to connect to multiple Cisco switches via SSH, execute commands, and log the output into separate files for each switch.

---

## Features
- Connects to Cisco switches using credentials specified in a CSV file (`inv.csv`).
- Executes commands provided in a text file (`cmd.txt`).
- Saves the output for each switch into a uniquely named log file (e.g., `switch1.log`).

---

## Project Structure

'''
project_directory/
├── run.py               # The main Python script
├── inv.csv              # CSV file containing switch details
├── cmd.txt              # Text file with commands to execute
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
''' 

---

## Prerequisites

- Python 3.6 or later.
- SSH access to the Cisco switches.
- Required Python library: `paramiko`.

---

## Installation

1. Clone this repository or download the files to your local machine.
2. Install the required dependencies using pip:
   '''
   pip install -r requirements.txt
   ''' 

---

## Configuration

### 1. `inv.csv`
This file contains the details of the switches to connect to. The format is as follows:
''' 
hostname,ip,user,pass
''' 

Example:
''' 
hostname,ip,user,pass
switch1,192.168.1.1,admin,password123
switch2,192.168.1.2,admin,password123
''' 

### 2. `cmd.txt`
This file contains the list of commands to be executed on each switch. Each command should be written on a new line.

Example:
''' 
show running-config
show version
''' 

---

## Usage

Run the script using the following command:
''' 
python run.py
''' 

### Output
- The script will create a log file for each switch, named `<hostname>.log`.
- Each log file will contain the output of the commands executed on the corresponding switch.

Example log files:
- `switch1.log`
- `switch2.log`

---

## Error Handling

- If a switch is unreachable or credentials are incorrect, the script will display an error message and move on to the next switch.
- Ensure that `inv.csv` and `cmd.txt` are properly formatted to avoid errors.

---

## Example Log File

An example of what a log file (`switch1.log`) might look like:
''' 
Command: show running-config
<output of show running-config>

Command: show version
<output of show version>
'''

---

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

---

## Contact

For questions or feedback, please contact:
help@mcsolutions.io
