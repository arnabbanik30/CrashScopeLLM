import uiautomator2 as u2
import time


from random_number import generate_random_int
from run_report import append_and_print_report


def interact_ui(element: u2.xpath.XMLElement, device):
    element_text = element.info.get("text", "Unnamed Element")
    element_class = element.info.get("className", "Unknown Class")

    if element_class == "android.widget.Button":
        pressing_btn = f"Pressing button: '{element_text}, resource-id: '{element.info['resourceId']}'"
        append_and_print_report(pressing_btn)
        element.click()
        element.click()
        element.click()
        time.sleep(1)
    elif element_class == "android.widget.EditText":
        element.click()
        time.sleep(1)
        pressing_btn = f"Pressing textfield: '{element_text}, resource-id: '{element.info['resourceId']}'"
        append_and_print_report(pressing_btn)
        random_number = generate_random_int()
        device.clear_text()
        entering_number = f"Clearing text, and entering {random_number} into text field, resource-id: '{element.info['resourceId']}'"
        append_and_print_report(entering_number)
        try:
            resource_id = element.info.get("resourceName")
            # print("Resource Id - " + resource_id)
            if resource_id:
                device.send_keys(str(random_number))
            time.sleep(2)
        except Exception as e:
            error = f"Error setting text: {e}"
            append_and_print_report(error)
