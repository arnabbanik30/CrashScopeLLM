import uiautomator2 as u2
import time

from random_number import generate_random_int


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
        random_number = generate_random_int()
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
