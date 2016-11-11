

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

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

    def enshore_login(self, username, passwd):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, passwd)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def enshure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

