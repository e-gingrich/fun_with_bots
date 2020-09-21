from profiles import profile1
from selenium import webdriver

def func1(key):
    driver = webdriver.Chrome('./chromedriver.exe')
    
    driver.get('https://www.google.com')

if __name__ == "__main__":
    func1(profile1)