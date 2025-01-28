import os
import sys

from apk_install import install_apk
from arg_parser import parser
from dfs_basic import dfs
from formatted_time import get_formatted_time
from get_activity_info import get_activity_info
from get_package_xpath import get_package_xpath
from globals import start_time
from launch_app import launch_app
from package_name import get_package_name
import uiautomator2 as u2

from run_report import append_and_print_report


def main():

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit()

    apk_path = args.apk_path
    if not os.path.exists(apk_path):
        append_and_print_report(f"Error: APK file not found at {apk_path}")
        sys.exit(1)

    package_name = get_package_name(apk_path)
    if not package_name:
        append_and_print_report("Failed to extract package name. Exiting.")
        sys.exit(1)

    install_apk(apk_path)

    append_and_print_report("Connecting to device/emulator...")
    device = u2.connect()

    launch_app(package_name)

    # set_start_time()

    append_and_print_report("Starting UI exploration...")
    append_and_print_report(f"Exploration Start Time: {start_time}")
    try:
        xpath = get_package_xpath(package_name)

        nodes = get_activity_info(xpath, device)
        dfs(nodes.all(), package_name, device)


    except Exception as e:
        append_and_print_report(f"An error occurred: {e}")
    finally:
        append_and_print_report("UI exploration complete.")



if __name__ == "__main__":
    main()