import sys

from dwave_web_handler import DwaveWebHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from io_handler import write_tokens, write_history


def main():
    # for edge
    # driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    # for chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if len(sys.argv) > 2:
        print("INVALID ARGUMENTS")
        return
    if len(sys.argv) == 1:
        email = input("Enter email address to create account:\n")

    elif len(sys.argv) == 2:
        email = sys.argv[1]

    # Phase 1
    dwh = DwaveWebHandler(driver)
    dwh.signup(email)

    # Phase 2
    activation_link = input("Enter activation link:\n")
    dwh = DwaveWebHandler(driver)
    dwh.login(email, activation_link)
    dwave_token = dwh.get_dwave_token()
    print("\nToken:\n", dwave_token)
    write_tokens(dwave_token)
    write_history(dwave_token)


if __name__ == '__main__':
    # get temp email at: https://temp-mail.org/
    main()






