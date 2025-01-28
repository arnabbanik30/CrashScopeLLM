import argparse
import argcomplete

parser = argparse.ArgumentParser(
description="This app explores the .apk file specified by the user."
)

parser.add_argument(
    "-p", "--apk-path",
    help="The path to the .apk file (required)",
    required=True
)

argcomplete.autocomplete(parser)