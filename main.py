import argparse
import sys
import time

from selenium import webdriver
from selenium.webdriver import Keys
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
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
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

    # Send id and password
    try:
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input").send_keys(
            id)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input").send_keys(
            mdp)
        # Click on login button
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div").click()
        time.sleep(10)

        # Go to the channel
        driver.get("https://discord.com/channels/758063518355554375/782706641355014144")
        time.sleep(10)

        # Send a message in the channel
        driver.find_elements(By.CSS_SELECTOR, "[aria-label='Envoyer un message dans #pokemon-🐲']")[0].send_keys("$p")
        time.sleep(10)
        # Send enter
        driver.find_element(By.XPATH, "/html/body").send_keys(Keys.RETURN + Keys.ENTER + Keys.SHIFT)
        time.sleep(5)
        # Print
        print("$p sent")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        driver.close()
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
    # Print the time
    print(time.strftime("%H:%M:%S"))
    print("Starting the bot")
    job()
    print("Bot stopped")
    print(time.strftime("%H:%M:%S"))

    # schedule.every(2).minutes.do(job)

    # while True:
    #    schedule.run_pending()
    #    time.sleep(1)
