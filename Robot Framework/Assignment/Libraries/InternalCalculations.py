from robot.api.deco import keyword
from SeleniumLibrary import SeleniumLibrary


class ProductPage:

    def __init__(self):
        self.selenium_lib = SeleniumLibrary()

    @keyword
    def get_product_price_by_name(self, product_name):

        products = self.selenium_lib.get_webelements(
            "xpath://div[@class='inventory_item']"
        )

        for product in products:

            name = product.find_element(
                "xpath",
                ".//div[@class='inventory_item_name']"
            ).text

            if name == product_name:

                price = product.find_element(
                    "xpath",
                    ".//div[@class='inventory_item_price']"
                ).text

                return price.replace("$", "")

        return None