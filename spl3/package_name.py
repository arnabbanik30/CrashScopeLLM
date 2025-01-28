import subprocess

from run_report import append_and_print_report


def get_package_name(apk_path):

    append_and_print_report("Extracting package name from the APK...")
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
                append_and_print_report(f"Package name: {package_name}")
                return package_name
    except FileNotFoundError:
        append_and_print_report("Error: 'aapt' tool is not installed or not in PATH. Install Android SDK Build-Tools.")
    except subprocess.CalledProcessError as e:
        append_and_print_report(f"Error extracting package name: {e.stderr}")
    return None
