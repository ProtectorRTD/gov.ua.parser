# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chrome_driver_path = "/path/to/chromedriver"

    # Create a new ChromeOptions instance with the "invisible" reCAPTCHA option
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Create a new ChromeDriver with the ChromeOptions instance
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

    # Navigate to the website with the reCAPTCHA and wait for it to load
    driver.get("https://www.example.com")
    driver.implicitly_wait(10)

    # Call the execute_script method to simulate a user action
    driver.execute_script('document.querySelector(".g-recaptcha").click()')

    # ... wait for the reCAPTCHA to be solved ...

    # Quit the ChromeDriver instance
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
