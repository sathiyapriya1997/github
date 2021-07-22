from selenium import webdriver
import pytest
class Test_employee:
    @pytest.mark.parametrize("browser_name",["chrome","firefox","internet_explorer"])
    def test_login(self,browser_name):
        if browser_name == "chrome":
            print("chrome")
            self.driver = webdriver.Chrome(executable_path=r"C:\Users\Sathiyapriya\PycharmProjects\pythonProject1\sathiya\sathiya\chromedriver.exe")
        elif browser_name == "firefox":
            print("firefox")
            self.driver = webdriver.Firefox(executable_path=r"C:\Users\Sathiyapriya\PycharmProjects\pythonProject1\sathiya\sathiya\geckodriver.exe")
        elif browser_name == "internet_explorer":
            print("internet_explorer")
            self.driver = webdriver.Ie(executable_path=r"C:\Users\Sathiyapriya\PycharmProjects\pythonProject1\sathiya\sathiya\IEDriverServer.exe")
        else:
            print("invalid browser")

        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")













