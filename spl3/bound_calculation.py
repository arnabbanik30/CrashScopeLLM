import uiautomator2 as u2

def get_clickable_bound(node: u2.xpath.XMLElement):
    bounds = node.info['bounds']
    x = (bounds['left'] + bounds['right']) / 2
    y = (bounds['top'] + bounds['bottom']) / 2

    return x, y