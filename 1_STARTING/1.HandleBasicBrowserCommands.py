from Basic_browser_commands import Basic_selenium

class HandleBasicBrowser(Basic_selenium):
    def verify_commands(self):
# to load title of tab
        print(self.driver.title)
# to load link url
        print(self.driver.current_url)
#receive id of current opened tab
        print(self.driver.current_window_handle)
# to print created url - html source code
        print(self.driver.page_source)
h=HandleBasicBrowser()
h.initialize_browser()
h.verify_commands()

#****************************************************************






