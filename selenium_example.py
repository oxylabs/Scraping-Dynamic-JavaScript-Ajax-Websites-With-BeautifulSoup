from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

# update executable_path as required
driver = Chrome(ChromeDriverManager().install())

driver.get('https://quotes.toscrape.com/js/')

try:
    # print first author
    author_element = driver.find_element_by_tag_name("small")
    print(author_element.text)

    # print all authors
    all_author_elements = driver.find_elements_by_tag_name("small")
    for element in all_author_elements:
        print(element.text)
finally:
    # always close the browser
    driver.quit()
