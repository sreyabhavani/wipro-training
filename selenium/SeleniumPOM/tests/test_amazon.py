import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage

'''def test_open_amazon(driver):
    assert "amazon" in driver.current_url,'URL for amazon is not correct'
    print("\nOpened Amazon Homepage.Title&URL verified")


def test_search_product(driver):
    homepage=HomePage(driver)

    homepage.type_search_input()
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(),'search results pages did not load'
    print("\nSearch results pages loaded sucessfully")
'''

@pytest.mark.parametrize("searchproduct",[
    ('wireless mouse'),('shoes')
])
def test_find_elements_amazon(driver,searchproduct):
    homepage=HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")

    homepage.click_search_button()
    assert homepage.is_amazon_page_loaded(),"Search results page did not load."

    productlistingpage=ProductListingPage(driver)

    val=productlistingpage.all_products()
    assert val,"No products found  on Amazon page"


def test_brand_filter(driver):
    productlistingpage=ProductListingPage(driver)

    productlistingpage.select_brand_filter()

    assert productlistingpage.check_product_titles_for_brand_filter('Logitech'),'Brand filter not applied properly'


