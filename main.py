import argparse
import time

import schedule
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_arguments():
    """
    Get id and password from arguments
    :return:
    """
    if not len(sys.argv) > 1:
        print("Please enter the id and password")
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="Id")
    parser.add_argument("-p", "--password", help="Password")
    args = parser.parse_args()
    return args


def init_driver():
    """
    Initialize the driver
    :return: the driver
    """
    options = webdriver.ChromeOptions()
    options.headless = False
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def send_dollar_p(driver, args):
    """
    Send the id and password to the bot function
    :param driver: the driver for selenium execution
    :param args: the arguments for discord connexion
    :return: nothing
    """

    # Go to discord connexion
    driver.get("https://discord.com/login")
    time.sleep(1)

    # Get id and password
    mdp = args.password
    id = args.id

    # Send id and password
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys(
        id)
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys(
        mdp)

    # Click on login button
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div").click()
    time.sleep(5)

    # Go to the channel
    driver.get("https://discord.com/channels/758063518355554375/782706641355014144")
    time.sleep(5)

    # Send a message in the channel
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]/div").send_keys(
        "$p")
    time.sleep(3)

    # Send enter
    driver.find_element(By.XPATH, "/html/body").send_keys(Keys.RETURN + Keys.ENTER + Keys.SHIFT)
    time.sleep(5)
    driver.quit()


def job():
    """
    Main function
    :return: nothing
    """
    args = get_arguments()
    driver = init_driver()
    send_dollar_p(driver, args)


if __name__ == '__main__':
    # TODO: Docker
    schedule.every(2).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
