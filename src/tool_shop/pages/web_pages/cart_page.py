from playwright.sync_api import Page
from src.tool_shop.data.data import Product


class CartPage:
    def __init__(self, product: Product, page: Page):
        self.page = page
        self.product = product

        self.product_quantity = page.get_by_role("spinbutton", name=f"Quantity for {product.name}")
        self.subtotal = page.locator("[data-test=\"cart-subtotal\"]")
        self.total = page.locator("[data-test=\"cart-total\"]")
        self.discount = page.locator("[data-test=\"cart-eco-discount\"]")
        self.delete_from_cart_btn = page.locator(".btn.btn-danger")
        self.proceed_to_checkout_cart = page.locator("[data-test=\"proceed-1\"]")

        self.logged_text = page.locator("app-login")
        self.proceed_to_checkout_singin = page.locator("[data-test=\"proceed-2\"]")

        self.billing_street = page.locator("[data-test=\"street\"]")
        self.billing_city = page.locator("[data-test=\"city\"]")
        self.billing_state = page.locator("[data-test=\"state\"]")
        self.billing_country = page.locator("[data-test=\"country\"]")
        self.billing_postcode = page.locator("[data-test=\"postal_code\"]")
        self.proceed_to_checkout_billing = page.locator("[data-test=\"proceed-3\"]")

        self.payment_method = page.locator("[data-test=\"payment-method\"]")
        self.credit_card_number = page.locator("[data-test=\"credit_card_number\"]")
        self.expiration_date = page.locator("[data-test=\"expiration_date\"]")
        self.cvv = page.locator("[data-test=\"cvv\"]")
        self.card_holder_name = page.locator("[data-test=\"card_holder_name\"]")
        self.confirm_btn = page.locator("[data-test=\"finish\"]")
        self.payment_message = page.locator("[data-test=\"payment-success-message\"]")





