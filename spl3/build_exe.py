import subprocess
import sys
import os
import glob
import pkg_resources

def install_requirements():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])

    if os.path.exists('requirements.txt'):
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])


def find_assets():
    assets = []

    jar_files = glob.glob('**/*.jar', recursive=True)
    for jar in jar_files:

        assets.append((jar, os.path.dirname(jar)))

    asset_patterns = [
        '**/*.json',
        '**/*.xml',
        '**/*.yaml',
        '**/*.yml',
        '**/*.properties',
        '**/*.config',
        '**/resources/*',
        # Add more patterns as needed
    ]

    for pattern in asset_patterns:
        files = glob.glob(pattern, recursive=True)
        for file in files:
            assets.append((file, os.path.dirname(file)))

    assets.extend(find_uiautomator2_assets())
    return assets


def find_uiautomator2_assets():
    """Find uiautomator2 specific assets"""
    assets = []

    # Find uiautomator2 package location
    try:
        u2_location = pkg_resources.resource_filename('uiautomator2', '')
        assets_dir = os.path.join(u2_location, 'assets')

        if os.path.exists(assets_dir):
            # Add all files from assets directory
            for root, _, files in os.walk(assets_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    # Keep the relative path structure starting from 'assets'
                    rel_path = os.path.relpath(root, u2_location)
                    assets.append((full_path, f'uiautomator2/{rel_path}'))
    except Exception as e:
        print(f"Warning: Could not find uiautomator2 assets: {e}")

    return assets

def build_executable(main_script, output_name=None):

    if not output_name:
        output_name = os.path.splitext(main_script)[0]


    assets = find_assets()


    cmd = [
        'pyinstaller',
        '--onefile',  # Create a single executable file
        '--clean',  # Clean PyInstaller cache
        '--noconfirm',  # Replace output directory without asking
        '--name', output_name,
    ]


    for src, dest in assets:
        cmd.extend(['--add-data', f'{src}{os.pathsep}{dest}'])


    cmd.append(main_script)

    print("Including the following assets:")
    for src, dest in assets:
        print(f"  - {src} -> {dest}")

    subprocess.check_call(cmd)


def get_resource_path(relative_path):
    """Helper function to get resource path in both development and PyInstaller"""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in normal Python environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == '__main__':

    print("Installing required packages...")
    install_requirements()

    # Build the executable
    print("Building executable...")
    main_script = 'main.py'
    build_executable(main_script, "spl3exec")

    print(f"\nBuild complete! Check the 'dist' folder for your executable.")