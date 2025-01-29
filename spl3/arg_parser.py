import argparse
import argcomplete


parser = argparse.ArgumentParser(
description="This app explores the .apk file specified by the user."
)

parser.add_argument(
    "-p", "--apk-path",
    help="The path to the .apk file (required)",
    required=False
)


parser.add_argument(
    "--analyze",
    help="Analyze the specified .apk file.",
    action="store_true"
)

parser.add_argument(
    "--enable-crash-summary",
    help="Enable AI generated summary of crash report",
    action="store_true"
)


parser.add_argument(
    "--run-replayable-script",
    help="flag to run the replayable script",
    action="store_true"
)

parser.add_argument(
    "-s", "--script-path",
    help="The path to the script file (required)",
    required=False
)
argcomplete.autocomplete(parser)