from pages.side_menu_component import SideMenuComponent


class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.side_menu=SideMenuComponent(driver)
    def go_to_leave(self):
        self.side_menu.open_leave()

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.side_menu=SideMenuComponent(driver)
    def go_to_admin(self):
        self.side_menu.open_admin()

    def open_admin_page(self):
        pass
