import uiautomator2 as u2

from action_interaction import ACTION
from bound_calculation import get_clickable_bound
from globals import replayable_script


def add_to_replayable_script(element: u2.xpath.XMLElement, action: ACTION, value=None):

    x, y = get_clickable_bound(element) if element is not None else (0,0)

    if action == ACTION.CLICK:
        replayable_script.append(f"adb shell input tap {x} {y}")
        return
    if action == ACTION.BACK:
        replayable_script.append(f"adb shell input keyevent KEYCODE_BACK")
        return
    if action == ACTION.INPUT:
        replayable_script.append(f"adb shell input text {value}")
        return
    if action == ACTION.SLEEP:
        replayable_script.append(f"sleep {value}")
        return
    if action == ACTION.CLEAR_TEXT:
        replayable_script.append(f"adb shell input keyevent KEYCODE_DEL")
        return