import sys
import os
import ctypes
import tkinter as tk
from tkinter import messagebox, ttk, font
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def get_interfaces_details():
    try:
        cmd_result = subprocess.check_output("netsh interface ip show config", shell=True).decode()
        return cmd_result
    except Exception as e:
        return str(e)

def get_active_interfaces():
    try:
        cmd_result = subprocess.check_output("netsh interface ip show interface", shell=True).decode()
        lines = cmd_result.split("\n")
        interfaces = []

        for line in lines:
            parts = line.split()
            if "connected" in line and "Loopback" not in line:
                interface_name = line.split(maxsplit=4)[-1]
                interfaces.append(interface_name)

        return interfaces
    except Exception as e:
        return []

def auto_subnet(*args):
    ip = ip_var.get()
    if ip.startswith("192."):
        subnet_var.set("255.255.255.0")
    elif ip.startswith("10."):
        subnet_var.set("255.0.0.0")

def change_ip():
    interface = interface_combobox.get()
    new_ip = ip_entry.get()
    subnet_mask = subnet_entry.get()

    if not interface:
        messagebox.showerror("Error", "Please select a network interface.")
        return

    cmd = f"netsh interface ip set address name=\"{interface}\" static {new_ip} {subnet_mask}"
    
    result = os.system(cmd)
    if result == 0:
        messagebox.showinfo("Success", "IP Address changed successfully!")
    else:
        messagebox.showerror("Error", "Failed to change the IP address.")

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

app = tk.Tk()
app.title("Change IP Address")

# Styling
dark_bg = "#2E2E2E"
dark_fg = "#FFFFFF"
input_bg = "#555555"
button_bg = "#444444"
button_fg = "#FFFFFF"
label_font_style = "Helvetica 12"
bold_font_style = "Helvetica 12 bold"

# Applying Styles
app.configure(bg=dark_bg)

main_frame = tk.Frame(app, bg=dark_bg)
main_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Right panel for interfaces' info
info_frame = tk.Frame(app, bd=2, relief=tk.GROOVE, bg=dark_bg)
info_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

scrollbar = ttk.Scrollbar(info_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

interfaces_text = tk.Text(info_frame, width=60, height=10, bg=input_bg, fg=dark_fg, font=label_font_style, yscrollcommand=scrollbar.set)
interfaces_text.insert(tk.END, get_interfaces_details())
interfaces_text.config(state=tk.DISABLED)
interfaces_text.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=interfaces_text.yview)

interface_label = tk.Label(main_frame, text="Network Interface:", bg=dark_bg, fg=dark_fg, font=bold_font_style)
interface_label.pack(pady=10)

interface_combobox = ttk.Combobox(main_frame, values=get_active_interfaces(), width=30, font=label_font_style)
interface_combobox.pack(pady=10)

ip_label = tk.Label(main_frame, text="New IP Address:", bg=dark_bg, fg=dark_fg, font=bold_font_style)
ip_label.pack(pady=10)

ip_var = tk.StringVar()
ip_var.trace("w", auto_subnet)
ip_entry = tk.Entry(main_frame, width=30, font=label_font_style, textvariable=ip_var, bg=input_bg, fg=dark_fg)
ip_entry.pack(pady=10)

subnet_label = tk.Label(main_frame, text="Subnet Mask:", bg=dark_bg, fg=dark_fg, font=label_font_style)
subnet_label.pack(pady=10)

subnet_var = tk.StringVar()
subnet_entry = tk.Entry(main_frame, width=30, font=label_font_style, textvariable=subnet_var, bg=input_bg, fg=dark_fg)
subnet_entry.pack(pady=10)

change_button = tk.Button(main_frame, text="Change IP", command=change_ip, font=label_font_style, bg=button_bg, fg=button_fg)
change_button.pack(pady=40)

app.mainloop()
