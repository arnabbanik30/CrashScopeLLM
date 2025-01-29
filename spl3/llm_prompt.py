import uiautomator2 as u2
import random

from bound_calculation import get_clickable_bound

def get_cmd(str):
    if "edit" in str.lower():
        return f"adb shell input text {random.randint(-100, 100)}"
    else:
        return ""


def get_prompt(node: u2.xpath.XMLElement):
    x, y = get_clickable_bound(node)
    x = int(x) + random.randint(-20, 20)
    y = int(y) + random.randint(-20, 20)
    prompt = f"[This is a {node.info['className']} element in an android app. "
    prompt += f"My label is '{node.attrib['text']}' "
    prompt += f"My content description is '{node.attrib['content-desc']}' "
    prompt += f"My resource id is {node.attrib['resource-id']}. "
    prompt += f"I am {'not' if node.attrib['clickable'] == 'false' else ''} clickable. "
    prompt +=  f"My shell command is: 'adb shell input tap {x} {y}.] "
    prompt = prompt + get_cmd(node.info['className'])
    prompt += "You can also press back with adb shell input keyevent KEYCODE_BACK"

    b = random.choices([True, False], weights=[6, 4])[0]
    shell = f"adb shell input tap {x} {y}" + get_cmd(node.info['className']) if b else "adb shell input keyevent KEYCODE_BACK"
    return prompt, shell
