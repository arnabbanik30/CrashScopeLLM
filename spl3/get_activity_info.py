def get_activity_info(xpath, device):
    nodes = device.xpath(xpath)
    return nodes