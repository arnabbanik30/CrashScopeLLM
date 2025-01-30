import random
import subprocess
import time
import ollama
import uiautomator2 as u2

from concise_node_info import get_concise_node_info
from get_activity_info import get_activity_info
from get_package_xpath import get_package_xpath
from llm_prompt import get_prompt


def llm_explore(package_name, device: u2.Device):
    # random.seed(time.)
    xpath = get_package_xpath(package_name)

    nodes = get_activity_info(xpath, device)

    llm_messages = []
    llm_responses = []

    for node in nodes.all():
        if "view" in node.info['resourceId'].lower() or node.info['resourceId'] == "" or "layout" in node.info['className'].lower():
            continue
        msg, res = get_prompt(node)
        # print("msg: " + msg)
        # print("res: " + res)
        llm_messages.append(msg)
        llm_responses.append(res)

    try:
        messages = [{
            'role': 'user',
            'content': " ".join(llm_messages)
        }, {
            'role': 'assistant',
            'content': random.choice(llm_responses)
        }, {
            'role': 'user',
            'content': ' '.join(llm_messages)
        }]
        print("Analyzing...")
        response = ollama.chat(
            model="adbllm",
            messages=messages
        )

        assistant_message = response['message']['content']
        print(f"ADB Assistant: {assistant_message}\n")

        print(f"Executing Command: {assistant_message}")
        result = subprocess.run(assistant_message, shell=True, text=True)
        if result.returncode != 0:
            print(f"Command failed: {assistant_message}")

    except Exception:
        print("App out of bounds")
        exit(1)
    llm_explore(package_name, device)