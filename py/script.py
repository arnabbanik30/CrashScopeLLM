import uiautomator2 as u2
import subprocess
import sys
import os
import time
import random

# Numbers to insert into text fields
numbers_to_insert = [42, -17, 0, 123, -456]
# device: u2.Device
def get_package_name(apk_path):
    """
    Extract the package name from the APK using the 'aapt' tool.
    """
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

def launch_app(package_name):
    """
    Launch the app using the package name.
    """
    print("Launching the app...")
    result = subprocess.run(
        ["adb", "shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("App launched successfully.")
        time.sleep(5)  # Wait for the app to load
    else:
        print(f"Error launching app: {result.stderr}")
        sys.exit(1)


import random

# Numbers to insert into text fields
numbers_to_insert = [42, -17, 5, 123, -456]  # Add more numbers if needed

def interact_with_ui(element : u2.xpath.XMLElement, device):
    """
    Interact with a single UI element based on its type and print its details.
    """
    element_text = element.info.get("text", "Unnamed Element")
    element_class = element.info.get("className", "Unknown Class")

    # Print the element's details
    # print(f"Found element - Text: '{element_text}', Class: '{element_class}'")
    text = element.attrib.get('text', '')
    clickable = element.attrib.get('clickable') == 'true'
    resource_id = element.attrib.get('resource-id', '')
    element_class = element.attrib.get('class', '')
    bounds = element.attrib.get('bounds', '')

    print(f"\nFound element:")
    print(f"- Text: {text}")
    print(f"- Resource ID: {resource_id}")
    print(f"- Class: {element_class}")
    print(f"- Bounds: {bounds}")
    print(f"- Clickable: {clickable}")



    if element_class == "android.widget.Button":
        # Tap the button
        print(f"Pressing button: '{element_text}'")
        element.click()
        time.sleep(1)

    elif element_class == "android.widget.EditText":
        # Enter random numbers into the text field
        random_number = random.choice(numbers_to_insert)
        # element.click()
        # time.sleep(1)
        device.clear_text();
        print(f"Entering {random_number} into text field.")
        try:
            # Use the device object to set text
            resource_id = element.info.get("resourceName")
            print("Resource Id - " + resource_id)
            if resource_id:
                # device.set_text(resource_id, str(random_number))
                device.send_keys(str(random_number))
            time.sleep(1)  # Wait for UI updates
        except Exception as e:
            print(f"Error setting text: {e}")

    # else:
        # For other elements, only print details
        # print(f"Skipping interaction with element of class: {element_class}")

# def explore_ui(device, current_xpath="//*", depth=0, max_depth=5, visited=None):
#     if visited is None:
#         visited = set()
#
#     if depth > max_depth:
#         return
#
#     if current_xpath in visited:
#         return
#
#     visited.add(current_xpath)
#
#     try:
#         # Fetch and process current element
#         element = device.xpath(current_xpath).get()
#
#         # Only process elements with actual content or interaction possibilities
#         if (element.attrib.get('text') or
#                 element.attrib.get('clickable') == 'true' or
#                 element.attrib.get('resource-id')):
#             print(f"\n{'=' * 50}")
#             print(f"Exploring at depth {depth}: {current_xpath}")
#             interact_with_ui(element, device)
#
#         # Get all children of current element
#         children = device.xpath(current_xpath + "/*").all()
#
#         # DFS: Process each child's entire subtree before moving to next sibling
#         for index in range(len(children)):
#             child_xpath = f"{current_xpath}/*[{index + 1}]"
#             explore_ui(device, child_xpath, depth + 1, max_depth, visited)
#
#     except Exception as e:
#         print(f"Error processing element at {current_xpath}: {e}")


def explore_ui(device, app_package, visited_nodes=None, depth=0):
    """
    Explore the app's UI dynamically in a depth-first manner.
    """
    if visited_nodes is None:
        visited_nodes = []

    # Dump the current UI hierarchy
    ui_hierarchy = device.dump_hierarchy()
    root = device.xpath("//*")

    # Iterate through all visible elements
    for element in root.all():
        class_name = element.attrib.get("class")
        resource_id = element.attrib.get("resource-id", "")
        text = element.attrib.get("text", "")
        clickable = element.attrib.get("clickable", "false") == "true"

        package = element.attrib.get("package", "")

        if package != app_package:
            continue
        # Skip already visited nodes
        if resource_id in visited_nodes:
            continue

        # Mark the node as visited
        visited_nodes.append(resource_id)

        # Print current node
        print(f"{'  ' * depth}Class: {class_name}, Resource ID: {resource_id}, Text: {text}, Clickable: {clickable}")

        if clickable:
            # Interact with the clickable element
            print(f"{'  ' * depth}-> Clicking element...")
            # element.click()
            interact_with_ui(element, device)
            time.sleep(1)  # Wait for UI to settle

            # Recursively explore the new screen
            explore_ui(device, app_package, visited_nodes, depth + 1)

            # Go back to the previous screen
            print(f"{'  ' * depth}<-- Navigating back...")
            device.press("back")
            time.sleep(1)  # Wait for UI to settle again

def explore_page(device, app_package, visited_nodes=None, depth=0):
    """
    Recursively explore the app's UI in a DFS manner.
    """
    if visited_nodes is None:
        visited_nodes = []

    # Dump the current UI hierarchy
    root = device.xpath("//*")

    # Iterate through all visible elements
    for element in root.all():
        class_name = element.attrib.get("class", "")
        resource_id = element.attrib.get("resource-id", "")
        text = element.attrib.get("text", "")
        clickable = element.attrib.get("clickable", "false") == "true"
        package = element.attrib.get("package", "")

        # Stay within the app package
        if package != app_package:
            continue

        # Skip already visited nodes
        if resource_id in visited_nodes:
            continue

        # Mark the node as visited
        visited_nodes.append(resource_id)

        # Print the current element's details
        print(f"{'  ' * depth}Class: {class_name}, Resource ID: {resource_id}, Text: {text}, Clickable: {clickable}")

        # Handle Buttons
        if class_name == "android.widget.Button" and clickable:
            print(f"{'  ' * depth}-> Clicking button: {text}")
            element.click()
            time.sleep(1)  # Wait for UI to settle

            # Explore the new page
            explore_page(device, app_package, visited_nodes, depth + 1)

            # Navigate back after exploring the new page
            print(f"{'  ' * depth}<-- Navigating back from: {text}")
            device.press("back")
            time.sleep(1)  # Wait for UI to settle again

        # Handle Text Fields
        elif class_name == "android.widget.EditText":
            dummy_text = "12345"  # Example input
            print(f"{'  ' * depth}-> Entering '{dummy_text}' into text field: {text}")
            try:
                element.set_text(dummy_text)
                time.sleep(1)  # Wait for input to be processed
            except Exception as e:
                print(f"{'  ' * depth}Error entering text: {e}")
def main():
    """
    Main function to start the script.
    """
    if len(sys.argv) != 2:
        print("Usage: python explore_ui.py <path-to-apk>")
        sys.exit(1)

    apk_path = sys.argv[1]
    if not os.path.exists(apk_path):
        print(f"Error: APK file not found at {apk_path}")
        sys.exit(1)

    # Extract package name from APK
    package_name = get_package_name(apk_path)
    if not package_name:
        print("Failed to extract package name. Exiting.")
        sys.exit(1)

    # Install the APK
    install_apk(apk_path)

    # Connect to the device/emulator
    print("Connecting to device/emulator...")
    device = u2.connect()  # Connects to the default device/emulator

    # Launch the app
    launch_app(package_name)

    # Start exploring the UI
    print("Starting UI exploration...")
    try:
        # explore_ui(device, package_name)
        explore_page(device, package_name)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("UI exploration complete.")

if __name__ == "__main__":
    main()
