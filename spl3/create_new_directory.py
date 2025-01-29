import os

def create_next_directory(prefix: str, base_path: str = "./dumps"):

    directory = "./dumps/"
    os.makedirs(directory, exist_ok=True)

    existing_dirs = [d for d in os.listdir(base_path) if
                     os.path.isdir(os.path.join(base_path, d)) and d.startswith(prefix)]

    dir_numbers = len(existing_dirs)
    next_number = dir_numbers + 1
    # print(dir)
    new_dir_name = f"{prefix}_{next_number}"
    new_dir = os.path.join(base_path, new_dir_name)

    os.makedirs(new_dir, exist_ok=True)

    return new_dir_name