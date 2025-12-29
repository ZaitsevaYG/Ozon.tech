from playwright.sync_api import Page, expect

class SingInPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.locator("[data-test=\"email\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.show_password = page.locator("[data-icon=\"eye\"]")
        self.hide_password = page.locator("[data-icon=\"eye-slash\"]")
        self.submit_btn = page.locator("[data-test=\"login-submit\"]")
