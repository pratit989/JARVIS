import time
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Browser:

    def __init__(self, path_init, initiate=True, implicit_wait_time=10, explicit_wait_time=2):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=options)
        self.driver.implicitly_wait(self.implicit_wait_time)
        self.path = path_init
        self.implicit_wait_time = implicit_wait_time  # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        self.explicit_wait_time = explicit_wait_time  # http://www.aptuz.com/blog/selenium-implicit-vs-explicit-waits/
        if initiate:
            self.start()
        return

    def start(self):
        return

    def end(self):
        self.driver.quit()
        return

    def go_to_url(self, url, wait_time=None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        self.driver.get(url)
        print('[*] Fetching results from: {}'.format(url))
        time.sleep(wait_time)
        return

    def get_search_url(self, query, page_num=0, per_page=10, lang='en'):
        query = quote_plus(query)
        url = 'https://www.google.co.in/search?q={}&num={}&start={}&nl={}'.format(query, per_page, page_num * per_page,
                                                                               lang)
        return url

    def scrape(self):
        # xpath migth change in future
        knowledge_panel_1 = self.driver.find_element_by_class_name("ILfuVd")
        if knowledge_panel_1.text != None:
            print(knowledge_panel_1.text)
        else:
            result = self.driver.find_element_by_class_name("st")
            print(result.text)
        return

    def search(self, query, page_num=0, per_page=10, lang='en', wait_time=None):
        if wait_time is None:
            wait_time = self.explicit_wait_time
        url = self.get_search_url(query, page_num, per_page, lang)
        self.go_to_url(url, wait_time)
        results = self.scrape()
        return results


path = "C:\\chromedriver.exe"  # SET YOU PATH TO phantomjs
br = Browser(path)
results = br.search('who is barack obama')

br.end()
