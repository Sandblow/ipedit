# ipedit
IP Address changer for Windows 
Manual for the IP Address Changer Utility
Table of Contents
Introduction
Prerequisites
Features
How to Use
Code Description
Conclusion
1. Introduction
This utility is designed to provide an easy-to-use graphical interface for users to change their IP address on their Windows system. The utility also fetches the details of the active network interfaces and displays them for the user's convenience.

2. Prerequisites
Operating System: Windows (The utility uses Windows-specific commands)
Python: At least Python 3.x should be installed.
Python Libraries:
tkinter: For GUI creation.
ctypes: To check and execute the script with administrative privileges.
os: To run system commands.
subprocess: To execute and retrieve results from command line operations.
3. Features
Admin Privilege Check: Ensures the script is run with administrative rights, which is required to change IP addresses.
Active Network Interface Detection: Lists all active network interfaces (excluding loopback).
Automatic Subnet Mask Prediction: Predicts the subnet mask based on the IP address entered.
Detailed Interface Information: Displays current IP configuration details.
Easy-to-use GUI: Simplifies the IP address changing process.
4. How to Use
Run the script. If not executed with administrative privileges, it will prompt for them.
On the left side:
Select your network interface from the drop-down.
Enter the new IP address you wish to assign.
The subnet mask will be predicted and filled in based on the IP address. However, you can change it if needed.
Click the "Change IP" button.
On the right side, you can view detailed information about your network interfaces.
A success or error message will be displayed based on the outcome of the IP change process.
5. Code Description
is_admin(): Checks if the script is run with admin rights.
get_interfaces_details(): Fetches detailed information about network interfaces.
get_active_interfaces(): Retrieves a list of currently active network interfaces.
auto_subnet(): Automatically sets the subnet mask based on the IP address entered.
change_ip(): Executes the command to change the IP address of the selected network interface.
tkinter GUI: Provides a graphical interface with labels, buttons, and input fields, organized in a user-friendly manner.
6. Conclusion
This utility offers a simplified way for users to change their IP address without delving into the intricacies of the command line. Whether you're a network professional or a casual user, this tool is designed to assist you swiftly.

Note: This tool is meant for legal and ethical uses only. Always ensure you have permission and are in compliance with all relevant policies and laws when changing IP addresses.
