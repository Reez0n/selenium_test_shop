from selenium.webdriver.common.by import By

class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "div.alert-info strong")