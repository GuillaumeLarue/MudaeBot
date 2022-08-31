import argparse
import sys
import time

import schedule
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def get_arguments():
    """
    Get id and password from arguments
    :return:
    """
    if len(sys.argv) == 1:
        print("Please enter the id and password")
        sys.exit(1)
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", help="Id")
    parser.add_argument("-p", "--password", help="Password")
    args = parser.parse_args()
    print("Arguments received")
    return args


def init_driver():
    """
    Initialize the driver
    :return: the driver
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.headless = False
    driver = None
    good = False
    for i in range(10):
        try:
            driver = webdriver.Remote(command_executor='http://seleniumweb:4444/wd/hub', options=options)
            # driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

        except Exception as exception:
            print(f"Error {i}: {str(exception)}")
            time.sleep(10)
            continue
        else:
            good = True
            break

    if not good:
        print("Error: driver not found")
        sys.exit(1)

    print("Driver initialized")
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

    try:
        # Send id and password
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys(
            id)
        print("Id found")

        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys(
            mdp)
        print("Password found")
        # Click on login button
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div").click()
        time.sleep(10)
        print("Login button found and clicked")

        # Go to the channel
        driver.get("https://discord.com/channels/758063518355554375/782706641355014144")
        time.sleep(10)
        print("Channel found")

        # Send a message in the channel
        driver.find_elements(By.CSS_SELECTOR, "[aria-label='Envoyer un message dans #pokemon-🐲']")[0].send_keys("$p")
        time.sleep(10)
        print("Message input found and sent")
        # Send enter
        driver.find_element(By.XPATH, "/html/body").send_keys(Keys.RETURN + Keys.ENTER + Keys.SHIFT)
        time.sleep(5)
        # Print
        print("$p sent")
    except Exception as exception:
        print("Error: " + str(exception))
    finally:
        driver.close()
        driver.quit()


def job():
    """
    Main function
    :return: nothing
    """
    print(time.strftime("%H:%M:%S"))
    print("Starting the automation")
    args = get_arguments()
    driver = init_driver()
    send_dollar_p(driver, args)
    print("Bot automation stopped")
    print(time.strftime("%H:%M:%S"))


if __name__ == '__main__':
    # TODO Logging https://github.com/CoreyMSchafer/code_snippets/blob/master/Logging-Basics/log-sample.py
    # TODO Add environment variable for id and password https://stackoverflow.com/questions/40454470/how-can-i-use-a-variable-inside-a-dockerfile-cmd
    # IDEA: one function that connect and init, and a second function that send the message

    print(f"Starting the bot {time.strftime('%H:%M:%S')}")
    schedule.every().hour.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
