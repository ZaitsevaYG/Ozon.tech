from playwright.sync_api import Page
from src.tool_shop.data.data import Product


class ProductPage:
    def __init__(self, product: Product, page: Page):
        self.page = page
        self.product = product

        self.product_price = page.locator("[data-test=\"unit-price\"]")
        self.product_name = page.locator("[data-test=\"product-name\"]")
        self.product_description = page.locator("[data-test=\"product-description\"]")
        self.co_rating = page.locator("[data-test=\"co2-rating-badge\"]")

        self.quantity = page.locator("[data-test=\"quantity\"]")
        self.increase_quantity = page.locator("[data-test=\"increase-quantity\"]")
        self.decrease_quantity = page.locator("[data-test=\"decrease-quantity\"]")

        self.add_to_card = page.locator("[data-test=\"add-to-cart\"]")
        self.add_to_favorites = page.locator("[data-test=\"add-to-favorites\"]")
        
        self.alert_message = page.get_by_role("alert")
        self.go_to_cart = page.locator("[data-test=\"nav-cart\"]")
        self.cart_quantity = page.locator("[data-test=\"cart-quantity\"]")
