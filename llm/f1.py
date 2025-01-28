import uiautomator2 as u2
import subprocess
import sys
import os
import time
import random
from enum import Enum

import langchain

from langchain_ollama import ChatOllama
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from uiautomator2.xpath import XMLElement

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
        time.sleep(2)  # Wait for the app to load
    else:
        print(f"Error launching app: {result.stderr}")
        sys.exit(1)


import random

# Numbers to insert into text fields
numbers_to_insert = [42, -17, 5, 123, -456]  # Add more numbers if needed

def print_node_name(element):
    print(element)

visited = dict()
class VISITED(Enum):
    NOT_EXPLORED=0
    EXPLORING=2
    DONE_EXPLORING=3


def checkVisited(node):
    if (node not in visited):
        visited[node] = VISITED.NOT_EXPLORED
        return VISITED.NOT_EXPLORED

    return visited[node]


def markVisited(node, val):
    visited[node] = val


def getChildXMLElements(node):
    children = node.all()[0].elem.getchildren()
    childXMLElements = []
    for c in children:
        xe = XMLElement(c, node._parent)
        childXMLElements.append(xe)

    return childXMLElements


def interact_ui(element: u2.xpath.XMLElement, device):
    element_text = element.info.get("text", "Unnamed Element")
    element_class = element.info.get("className", "Unknown Class")

    if element_class == "android.widget.Button":
        print(f"Pressing button: '{element_text}'")
        element.click()
        element.click()
        element.click()
        time.sleep(1)
    elif element_class == "android.widget.EditText":
        element.click()
        time.sleep(1)
        random_number = random.choice(numbers_to_insert)
        device.clear_text()
        print(f"Entering {random_number} into text field.")
        try:
            resource_id = element.info.get("resourceName")
            print("Resource Id - " + resource_id)
            if resource_id:
                device.send_keys(str(random_number))
            time.sleep(2)
        except Exception as e:
            print(f"Error setting text: {e}")

def get_concise_node_info(node):

    bounds = node.info['bounds']
    x = (bounds['left'] + bounds['right']) / 2
    y = (bounds['top'] + bounds['bottom']) / 2

    concise_node = {
        'element_text': node.info['text'],
        'resourceId' :  node.info['resourceId'],
        'packageName':  node.info['packageName'],
        'className' :   node.info['className'],
        'click_coordinates': (x, y),
        'element_type': node.info['className'],
        'is_clickable': node.info['clickable'],
        'bounds': bounds,

    }
    # print(concise_node)
    return concise_node
messages = []
def dfs(nodes, package_name, device: u2.Device):
    llm_messages = []
    for node in nodes:
        if node.info['resourceId'] == "" or "layout" in node.info['className'].lower():
            continue
        llm_messages.append(str(get_concise_node_info(node)))
        # print(get_concise_node_info(node))
        # print('\n' * 2)
    messages.append(
        {
        'role': 'user',
        'content': " ".join(llm_messages)
        })
    messages.append(
        {
            'role' : 'user',
            'content': 'based on whats given, write one or more adb shell inputs to interact with it. Only interact with Button or EditText elements. Use the click_coordinates to interact. prefer clicking input fields or buttons over labels. Only output shell commands(input, tap or sleep), write only the commands, not markdown'
            # 'content': 'select a button to press. output an adb shell tap command with proper coordinates.'
        })
    messages.append(
        {
            'role': 'assistant',
            'content': 'adb shell input tap 100 100',
        }
    )
    print("starting ollama")
    response = ollama.chat(
        model=model,
        messages=messages
    )
    
    assistant_message = response['message']['content']
    print(f"ADB Assistant: {assistant_message}\n")

    # llama_msgs = [{
    #     'role' : 'user'
    #
    # }]
    # for node in nodes:
    #     before_activity = device.app_current()['activity']
    #     current_activity = before_activity
    #     if checkVisited(node) == VISITED.NOT_EXPLORED:
    #         visited[node] = VISITED.EXPLORING
    #         # print("Exploring : ")
    #         # print(node.info)
    #         interact_ui(node, device)
    #         try:
    #             # app_status = device.app_wait(package_name)
    #             current_package = device.app_current()['package']
    #             if current_package != package_name:
    #                 print("App has stopped running!")
    #                 return 1
    #             # else:
    #             #     print("App is running.")
    #         except Exception as e:
    #             print(f"Error checking app status: {e}")

    #         current_activity = device.app_current()['activity']

    #         if before_activity != current_activity:
    #             print("Activity changed!")
    #             xpath = getPackageXpath(package_name)
    #             nodes = getActivityInfo(xpath, device)
    #             dfs(nodes.all(), package_name, device)

    #     visited[node] = VISITED.DONE_EXPLORING
    #     if before_activity != current_activity:
    #         device.press("back")

def getPackageXpath(package_name):
    return f"//*[@package='{package_name}']"

def getActivityInfo(xpath, device):
    nodes = device.xpath(xpath)
    return nodes

import ollama

# messages = [{
#     'role': 'system',
#     'content': 'You are a tool to generate bash commands. You can generate commands using adb shell only. Output the commands in plain text, not markdown. Do not write anything extra.'
# }]

# model="qwen2.5-coder:1.5b"
# model = "deepseek-r1:1.5b"
# model="deepseek-coder:1.3b"
model = "adbllm"
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

        xpath = getPackageXpath(package_name)

        nodes = getActivityInfo(xpath, device)

        dfs(nodes.all(), package_name, device)


    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("UI exploration complete.")

if __name__ == "__main__":
    main()