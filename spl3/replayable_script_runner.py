import subprocess
import time

def script_runner(filepath):
    # print(filepath)
    try:
        with open(filepath, "r") as file:
            commands = file.readlines()

        for command in commands:
            print(f"Executing: {command}")
            command = command.strip()
            if command.startswith("sleep"):
                _, duration = command.split()
                time.sleep(float(duration))
            elif command:
                result = subprocess.run(command, shell=True, text=True)
                if result.returncode != 0:
                    print(f"Command failed: {command}")
    except FileNotFoundError:
        print(f"File not found: {filepath}")

    except Exception as e:
        print(f"An error occurred: {e}")
