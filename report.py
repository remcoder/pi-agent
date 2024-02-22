import subprocess
import json, sys

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    return stdout.strip()

def collect_system_metrics():
    mpstat = run_command(["mpstat", "-o", "JSON"])
    system_report = {
        "cpu_usage": json.loads(mpstat),
        "disk_space": run_command(["df", "-h"]),
        "memory_usage": run_command(["free", "-h"]),
        "octoprint_status": "running" if run_command(["pgrep", "-f", "octoprint"]) else "stopped",
        "cpu_temperature": run_command(["vcgencmd", "measure_temp"])
    }
    return system_report

def main():
    sys.stderr.write('Gathering info\n')
    sys.stderr.flush()
    report = collect_system_metrics()
    # sys.stderr.write( json.dumps(report, indent=4))
    # sys.stderr.flush()

    # Directly output to stdout, with adjustments for Python 2.7:
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    main()