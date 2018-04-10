from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Login and password for hh.ru
login = ''
password = ''

keyWords = input('Профессия:')
region = input('Город:')
salary = input('Зарплата от:')
letter = input('Текст отклика:')

class HeadHunterResponse:
    def init_browser():
        browser = webdriver.Chrome()
        return browser

    def response(browser):
        browser.get('https://hh.ru/')
        loginInput = browser.find_element_by_xpath("//label[@class='login-input']//input[@type='text']")
        loginInput.send_keys(login)
        passwordInput = browser.find_element_by_xpath("//label[@class='login-input']//input[@type='password']")
        passwordInput.send_keys(password)
        passwordInput.submit()
        advancedSearch = browser.find_element_by_xpath("//a[@href='/search/vacancy/advanced'][contains(text(),'Расширенный поиск')]")
        advancedSearch.click()
        keyWordInput = browser.find_element_by_xpath("//input[@id='advancedsearchmainfield']")
        keyWordInput.send_keys(keyWords)
        salaryInput = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[1]/div/form/div[6]/div[2]/div[1]/div[1]/input[1]")
        salaryInput.send_keys(salary)
        elemsPerPage = browser.find_element_by_xpath("//span[@class='bloko-radio__text'][contains(text(),'100 вакансий')]")
        elemsPerPage.click()
        searchButton = browser.find_element_by_xpath("//input[@id='submit-bottom']")
        searchButton.click()
        respondButton = browser.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[3]/div/div/div[2]/div[2]/div/div/div[1]/div[3]/div/span/a")
        respondButton.click()
        responseLetter = browser.find_element_by_xpath("//span[contains(text(),'Сопроводительное письмо')]")
        responseLetter.click()
        letterText = browser.find_element_by_xpath("//textarea[@name='letter']")
        letterText.send_keys(letter)
        browser.save_screenshot('sreenshot.png')
        confirmButton = browser.find_element_by_xpath("//div[@class='bloko-form-spacer']//button[@type='submit']")
        confirmButton.click()

    response(init_browser())
