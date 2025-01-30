from bound_calculation import get_clickable_bound


def get_concise_node_info(node):

    x,y = get_clickable_bound(node)

    concise_node = {
        'element_text': node.info['text'],
        'resourceId' :  node.info['resourceId'],
        'packageName':  node.info['packageName'],
        'className' :   node.info['className'],
        'click_coordinates': (x, y),
        'element_type': node.info['className'],
        'is_clickable': node.info['clickable'],
        'bounds': node.info['bounds'],

    }

    return concise_node