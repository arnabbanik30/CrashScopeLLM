import os
import sys

from apk_install import install_apk
from arg_parser import parser
from create_new_directory import create_next_directory
from dfs_basic import dfs
from dump_error_output import get_error_dump_after_crash
from formatted_time import get_formatted_time
from get_activity_info import get_activity_info
from get_package_xpath import get_package_xpath
from globals import start_time, run_report, replayable_script
from launch_app import launch_app
from package_name import get_package_name
import uiautomator2 as u2

from run_report import append_and_print_report
from save_files import save_files
from summarize_crash_report import get_crash_summary


def main():

    args = parser.parse_args()

    if args.analyze:
        if args.apk_path is None:
            print("the path option -p is required with --analyze")
            exit(1)

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

        ret = dfs(nodes.all(), package_name, device)

        append_and_print_report("Generating replayable script")
        script = "\n".join(replayable_script)


        append_and_print_report("Dumping Stack Trace of the crash...") if ret != 0 else ""
        dump = get_error_dump_after_crash() if ret != 0 else ""
        ai_summary = get_crash_summary(dump, package_name) if ret != 0 and args.enable_crash_summary else ""

        append_and_print_report("UI exploration complete.")
        dir_name = create_next_directory("dump")
        filepath = f"./dumps/{dir_name}"

        save_files(filepath, "\n".join(run_report), "run_report", "md")

        save_files(filepath, script, "replayable_script_commands", "txt")

        if len(dump) != 0:
            save_files(filepath, dump, "stack_trace", "txt")
        if len(ai_summary) != 0:
            save_files(filepath, ai_summary, "crash_report_summary", "md")


    except Exception as e:
        append_and_print_report(f"An error occurred: {e}")



if __name__ == "__main__":
    main()