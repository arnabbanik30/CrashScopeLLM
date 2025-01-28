import subprocess
import sys

def install_apk(apk_path):
    """
    Install the APK onto the connected device/emulator.
    """
    print("Installing APK...")
    result = subprocess.run(["adb", "install", "-r", apk_path], capture_output=True, text=True)
    if result.returncode == 0:
        print("APK installed successfully.")
    else:
        print(f"Error installing APK: {result.stderr}")
        sys.exit(1)