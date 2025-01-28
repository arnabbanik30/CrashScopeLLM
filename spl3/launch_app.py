import subprocess
import sys
import time

def launch_app(package_name):
    """
    Launch the app using the package name.
    """
    print("Launching the app...")
    result = subprocess.run(
        ["adb", "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("App launched successfully.")
        time.sleep(2)
    else:
        print(f"Error launching app: {result.stderr}")
        sys.exit(1)

