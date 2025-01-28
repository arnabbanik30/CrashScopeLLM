import subprocess

def get_package_name(apk_path):

    print("Extracting package name from the APK...")
    try:
        # Use aapt to get package details
        result = subprocess.run(
            ["aapt", "dump", "badging", apk_path],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.splitlines():
            if line.startswith("package:"):
                package_name = line.split("'")[1]
                print(f"Package name: {package_name}")
                return package_name
    except FileNotFoundError:
        print("Error: 'aapt' tool is not installed or not in PATH. Install Android SDK Build-Tools.")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting package name: {e.stderr}")
    return None
