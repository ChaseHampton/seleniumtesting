import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--no-sandbox")  # Adding no-sandbox option for troubleshooting
    opts.add_argument("--disable-dev-shm-usage")  # Disable dev shm usage
    opts.add_extension("3.1.0_0.crx")
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.google.com/recaptcha/api2/demo")

    main_frame = driver.find_element(By.XPATH, '//iframe[@title="reCAPTCHA"]')
    driver.switch_to.frame(main_frame)
    chkbox = driver.find_element(By.XPATH, '//div[@class="recaptcha-checkbox-border"]')
    chkbox.click()

    driver.switch_to.default_content()
    time.sleep(2)
    challenge_frame = driver.find_element(
        By.XPATH, '//iframe[contains(@title, "recaptcha challenge expires")]'
    )
    driver.get_screenshot_as_file("outs/beforesolve.png")
    if challenge_frame.is_displayed():
        print("Challenge frame is displayed")
        driver.switch_to.frame(challenge_frame)
        bust_div = driver.find_element(
            By.XPATH, "//div[contains(@class, 'help-button-holder')]"
        )
        bust_div.click()
        driver.get_screenshot_as_file("outs/duringsolve.png")
    time.sleep(3)
    driver.get_screenshot_as_file("outs/aftersolve.png")

    # solved by here
    submit_btn = driver.find_element(By.XPATH, '//button[@id="recaptcha-demo-submit"]')


if __name__ == "__main__":
    main()
