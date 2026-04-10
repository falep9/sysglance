import subprocess
import socket
import platform

def get_ip_address():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(('8.8.8.8', 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL)
        return result.decode('utf-8', errors='ignore').strip()
    except Exception:
        return "N/A"

def display_audit():
    system_os = platform.system()
    ip = get_ip_address()
    
    print(f"OS: {system_os} | IP: {ip}")
    
    if system_os == "Windows":
        hw = run_command("wmic bios get serialnumber").split('\n')[-1]
        processes = run_command("tasklist").split('\n')[3:15]
    else:
        hw = run_command("cat /sys/class/dmi/id/product_uuid")
        processes = run_command("ps -eo comm | head -n 12").split('\n')[1:]
    
    print(f"Hardware ID: {hw}")
    print("Processos:")
    for p in processes:
        print(p.strip())

if __name__ == "__main__":
    display_audit()
