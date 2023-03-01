from selene import have
from utils.base_session import demoshop
import allure

def test_open_account(register):
    with allure.step('Create an account'):
        register.open('')
        register.element('a.account').click()
        register.element('div.page-title > h1').should(have.text('My account - Customer info'))


def test_clear_cart(register):
    with allure.step('Clear cart'):
        register.open('')
        demoshop.post('/addproducttocart/catalog/31/1/1')
        register.element('.ico-cart').click()
        register.element('.qty-input').clear().send_keys(0).press_enter()
        register.element('div.order-summary-content').should(
            have.text('Your Shopping Cart is empty!')
        )


def test_successful_search(register):
    with allure.step('Successful search'):
        register.open('')
        register.element('.search-box-text').type('Нокиа 3310').press_enter()
        register.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(register):
    with allure.step('Logout'):
        register.open('')
        register.element('.ico-logout').click()
        response = demoshop.get('/logout', allow_redirects=False)
        assert response.status_code == 302
