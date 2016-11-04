

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, passwd):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passwd)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[4]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
