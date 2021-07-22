from selenium import webdriver

class Base:
    def Launch_Browser(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Sathiyapriya\Documents\webdrivers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver
    def load_url(self,url):
        self.driver.get(url)
    def send_text(self,e,data):
        e.send_keys(data)
    def btn_click(self,h):
        h.click()
    def quit_browser(self):
        self.driver.quit()
