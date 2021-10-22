#!/usr/bin/env python3
# Leonardo José Zanotti
# https://github.com/LeonardoZanotti/petition-bot

from time import sleep

from selenium import webdriver


def main():
    driver = webdriver.Firefox()

    htmlBody = '/html/body/form/div[4]'
    firstButton = '/html/body/form/div[4]/div/table/tbody/tr/td[2]/div[2]/a'
    nameInput = '//*[@id="ctl00_cmain_txtNome"]'
    emailInput = '//*[@id="ctl00_cmain_txtEmail"]'
    termsInput = '//*[@id="ctl00_cmain_chkAutorizoContacto"]'
    lastButton = '//*[@id="ctl00_cmain_cmdSign"]'

    for i in range(10):
        driver.get('https://peticaopublica.com.br/psign.aspx?pi=BR120937')
        driver.find_element_by_xpath(nameInput).send_keys('username' + i)
        sleep(1)
        driver.find_element_by_xpath(
            emailInput).send_keys('username1' + i + '@gmail.com')
        sleep(1)
        driver.find_element_by_xpath(termsInput).click()
        sleep(1)
        driver.find_element_by_xpath(lastButton).click()
        sleep(10)

    driver.quit()


if __name__ == '__main__':
    main()
