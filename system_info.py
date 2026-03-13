#!/usr/bin/env python3
"""
System Information Fetcher
A Python script that retrieves and displays detailed system information
including OS details, hardware specifications, and system status.
"""

import platform
import socket
import datetime
import os
import sys
import json
import subprocess
import shutil


def get_system_info():
    """Retrieve comprehensive system information."""
    
    # Basic system information
    system_info = {
        "System Information": {
            "Operating System": platform.system(),
            "OS Version": platform.version(),
            "OS Release": platform.release(),
            "Platform": platform.platform(),
            "Architecture": platform.architecture()[0],
            "Processor": platform.processor(),
            "Machine Type": platform.machine(),
            "Hostname": socket.gethostname(),
            "Current Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        
        "CPU Information": {},
        
        "Memory Information": {},
        
        "Disk Information": {},
        
        "Network Information": {
            "Hostname": socket.gethostname(),
            "IP Address": socket.gethostbyname(socket.gethostname()) if socket.gethostbyname(socket.gethostname()) != "127.0.0.1" else "localhost"
        },
        
        "Python Information": {
            "Python Version": sys.version.split()[0],
            "Python Executable": sys.executable,
            "Python Path": sys.path[0] if sys.path else "N/A"
        }
    }
    
    # CPU Information using subprocess
    try:
        # Get CPU cores
        cpu_cores = os.cpu_count()
        system_info["CPU Information"]["Total Cores"] = cpu_cores
        
        # Get CPU usage (simple approximation)
        try:
            with open('/proc/stat', 'r') as f:
                cpu_times = f.readline().split()[1:8]
                idle_time = int(cpu_times[3])
                total_time = sum(int(x) for x in cpu_times)
                system_info["CPU Information"]["CPU Usage"] = "N/A (requires calculation)"
        except:
            system_info["CPU Information"]["CPU Usage"] = "N/A"
            
    except Exception as e:
        system_info["CPU Information"]["Error"] = str(e)
    
    # Memory Information using subprocess
    try:
        # Get memory info from /proc/meminfo
        with open('/proc/meminfo', 'r') as f:
            meminfo = f.read()
        
        # Parse memory information
        mem_total = None
        mem_free = None
        mem_available = None
        
        for line in meminfo.split('\n'):
            if line.startswith('MemTotal:'):
                mem_total = int(line.split()[1]) * 1024  # Convert KB to bytes
            elif line.startswith('MemFree:'):
                mem_free = int(line.split()[1]) * 1024
            elif line.startswith('MemAvailable:'):
                mem_available = int(line.split()[1]) * 1024
        
        if mem_total:
            system_info["Memory Information"]["Total Memory"] = f"{mem_total / (1024**3):.2f} GB"
        if mem_available:
            system_info["Memory Information"]["Available Memory"] = f"{mem_available / (1024**3):.2f} GB"
        if mem_free:
            system_info["Memory Information"]["Free Memory"] = f"{mem_free / (1024**3):.2f} GB"
        
        if mem_total and mem_available:
            used_memory = mem_total - mem_available
            system_info["Memory Information"]["Used Memory"] = f"{used_memory / (1024**3):.2f} GB"
            system_info["Memory Information"]["Memory Usage"] = f"{(used_memory / mem_total) * 100:.2f}%"
            
    except Exception as e:
        system_info["Memory Information"]["Error"] = str(e)
    
    # Disk Information using subprocess
    try:
        # Get disk usage using shutil
        total, used, free = shutil.disk_usage('/')
        system_info["Disk Information"] = {
            "Total Disk Space": f"{total / (1024**3):.2f} GB",
            "Used Disk Space": f"{used / (1024**3):.2f} GB",
            "Free Disk Space": f"{free / (1024**3):.2f} GB",
            "Disk Usage": f"{(used / total) * 100:.2f}%"
        }
    except Exception as e:
        system_info["Disk Information"]["Error"] = str(e)
    
    # Network interfaces using subprocess
    try:
        network_info = {}
        # Try to get network interface info
        try:
            result = subprocess.run(['ip', 'addr', 'show'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if 'inet ' in line and 'inet6' not in line:
                        parts = line.strip().split()
                        if len(parts) >= 2:
                            ip_addr = parts[1].split('/')[0]
                            interface = parts[-1]
                            if interface not in network_info:
                                network_info[interface] = []
                            network_info[interface].append(f"IP: {ip_addr}")
        except:
            # Fallback to simple interface listing
            network_info["Network"] = ["IP information not available without additional tools"]
        
        system_info["Network Interfaces"] = network_info
    except Exception as e:
        system_info["Network Interfaces"] = {"Error": str(e)}
    
    return system_info


def display_system_info(system_info):
    """Display system information in a formatted way."""
    
    print("=" * 60)
    print("           SYSTEM INFORMATION REPORT")
    print("=" * 60)
    print()
    
    for category, info in system_info.items():
        print(f"\n{category}:")
        print("-" * len(category))
        
        if isinstance(info, dict):
            for key, value in info.items():
                if isinstance(value, list):
                    print(f"  {key}:")
                    for item in value:
                        print(f"    - {item}")
                else:
                    print(f"  {key}: {value}")
        else:
            print(f"  {info}")
    
    print("\n" + "=" * 60)
    print("           END OF REPORT")
    print("=" * 60)


def save_to_file(system_info, filename="system_report.txt"):
    """Save system information to a text file."""
    try:
        with open(filename, 'w') as f:
            f.write("SYSTEM INFORMATION REPORT\n")
            f.write("=" * 40 + "\n\n")
            
            for category, info in system_info.items():
                f.write(f"\n{category}:\n")
                f.write("-" * len(category) + "\n")
                
                if isinstance(info, dict):
                    for key, value in info.items():
                        if isinstance(value, list):
                            f.write(f"  {key}:\n")
                            for item in value:
                                f.write(f"    - {item}\n")
                        else:
                            f.write(f"  {key}: {value}\n")
                else:
                    f.write(f"  {info}\n")
        
        print(f"\nSystem information saved to: {filename}")
        return True
    except Exception as e:
        print(f"Error saving to file: {e}")
        return False


def main():
    """Main function to fetch and display system information."""
    print("Fetching system information...")
    print("This may take a moment...\n")
    
    try:
        # Get system information
        system_info = get_system_info()
        
        # Display information
        display_system_info(system_info)
        
        # Ask user if they want to save to file
        save_choice = input("\nWould you like to save this information to a file? (y/n): ").lower().strip()
        
        if save_choice in ['y', 'yes']:
            filename = input("Enter filename (default: system_report.txt): ").strip()
            if not filename:
                filename = "system_report.txt"
            
            save_to_file(system_info, filename)
        
        print("\nThank you for using System Information Fetcher!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please make sure you have the required permissions to access system information.")


if __name__ == "__main__":
    main()