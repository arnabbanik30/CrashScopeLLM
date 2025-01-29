import uiautomator2 as u2
import time

from action_interaction import ACTION
from random_number import generate_random_int
from replayable_script_generator import add_to_replayable_script
from run_report import append_and_print_report


def interact_ui(element: u2.xpath.XMLElement, device):
    element_text = element.info.get("text", "Unnamed Element")
    element_class = element.info.get("className", "Unknown Class")

    if element_class == "android.widget.Button":
        pressing_btn = f"Pressing button: '{element_text}, resource-id: '{element.info['resourceId']}'"
        append_and_print_report(pressing_btn)
        element.click()
        add_to_replayable_script(element, ACTION.CLICK)
        element.click()
        add_to_replayable_script(element, ACTION.CLICK)
        element.click()
        add_to_replayable_script(element, ACTION.CLICK)

        time.sleep(1)
        add_to_replayable_script(element, ACTION.SLEEP, 1)

    elif element_class == "android.widget.EditText":
        element.click()
        add_to_replayable_script(element, ACTION.CLICK)

        time.sleep(1)
        add_to_replayable_script(element, ACTION.SLEEP, 1)

        pressing_btn = f"Pressing textfield: '{element_text}, resource-id: '{element.info['resourceId']}'"
        append_and_print_report(pressing_btn)
        random_number = generate_random_int()

        device.clear_text()
        add_to_replayable_script(element, ACTION.CLEAR_TEXT)

        entering_number = f"Clearing text, and entering {random_number} into text field, resource-id: '{element.info['resourceId']}'"
        append_and_print_report(entering_number)

        try:
            resource_id = element.info.get("resourceName")
            # print("Resource Id - " + resource_id)
            if resource_id:
                device.send_keys(str(random_number))
                add_to_replayable_script(element, ACTION.INPUT, random_number)
            time.sleep(1)
            add_to_replayable_script(element, ACTION.SLEEP, 1)

        except Exception as e:
            error = f"Error setting text: {e}"
            append_and_print_report(error)
