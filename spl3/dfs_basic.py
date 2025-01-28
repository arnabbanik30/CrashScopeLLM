from check_visisted import check_visited
from get_activity_info import get_activity_info
from get_package_xpath import get_package_xpath
from globals import visited
from interact_ui import interact_ui
from visited import VISITED

import uiautomator2 as u2

def dfs(nodes, package_name, device: u2.Device):
    app_crashed = 0
    for node in nodes:
        before_activity = device.app_current()['activity']
        current_activity = before_activity
        if check_visited(node) == VISITED.NOT_EXPLORED:
            visited[node] = VISITED.EXPLORING
            # print("Exploring : ")
            # print(node.info)
            interact_ui(node, device)
            try:
                # app_status = device.app_wait(package_name)
                current_package = device.app_current()['package']
                if current_package != package_name:
                    print("App has stopped running!")
                    return 1
                # else:
                #     print("App is running.")
            except Exception as e:
                print(f"Error checking app status: {e}")

            current_activity = device.app_current()['activity']

            if before_activity != current_activity:
                print("Activity changed!")
                xpath = get_package_xpath(package_name)
                nodes = get_activity_info(xpath, device)
                app_crashed = dfs(nodes.all(), package_name, device)
        if app_crashed == 1:
            return 1
        visited[node] = VISITED.DONE_EXPLORING
        if before_activity != current_activity:
            device.press("back")