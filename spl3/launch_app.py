import subprocess
import sys
import time

from run_report import append_and_print_report


def launch_app(package_name):

    append_and_print_report("Launching the app...")
    result = subprocess.run(
        ["adb", "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        append_and_print_report("App launched successfully.")
        time.sleep(2)
    else:
        append_and_print_report(f"Error launching app: {result.stderr}")
        sys.exit(1)

