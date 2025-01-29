from run_report import append_and_print_report


def save_files(filepath, content, filename, file_extension):
    new_file_path = f"{filepath}/{filename}.{file_extension}"
    with open(new_file_path, "w") as file:
        file.write(content)

    append_and_print_report(f"Generated: {new_file_path}")