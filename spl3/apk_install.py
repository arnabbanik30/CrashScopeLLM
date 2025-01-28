import subprocess
import sys

from run_report import append_and_print_report


def install_apk(apk_path):

    append_and_print_report("Installing APK...")
    result = subprocess.run(["adb", "install", "-r", apk_path], capture_output=True, text=True)
    if result.returncode == 0:
        append_and_print_report("APK installed successfully.")
    else:
        append_and_print_report(f"Error installing APK: {result.stderr}")
        sys.exit(1)