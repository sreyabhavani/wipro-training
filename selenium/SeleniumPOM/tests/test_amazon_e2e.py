import pytest
from pages.home_page import HomePage
from pages.product_listing_page import ProductListingPage

@pytest.mark.parametrize("searchproduct","brandname","mensize"[
    ("shoes","Nike","9")
])

def test_product_ordering(driver,searchproduct,brandaname):
    homepage=HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searcng product - {searchproduct}")
    homepage.click_search_button()

    assert homepage.is_amazon_page_loaded(),'search results pages did not load'
    print(f"fSearch results pages loaded sucessfully - {searchproduct}")
