import allure
from selene import have

from utils.base_session import demoshop


def test_open_account(register):
    register.open('')

    with allure.step('Open an account'):
        register.element('a.account').click()
        register.element('div.page-title > h1').should(have.text('My account - Customer info'))


def test_clear_cart(register):
    register.open('')

    with allure.step('Clear cart'):
        demoshop.post('/addproducttocart/catalog/31/1/1')
        register.element('.ico-cart').click()
        register.element('.qty-input').clear().send_keys(0).press_enter()
        register.element('div.order-summary-content').should(
            have.text('Your Shopping Cart is empty!')
        )


def test_successful_search(register):
    register.open('')

    with allure.step('Successful search'):
        register.element('.search-box-text').type('Нокиа 3310').press_enter()
        register.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(register):
    register.open('')
    with allure.step('Logout'):
        register.element('.ico-logout').click()
        response = demoshop.get('/logout', allow_redirects=False)
        assert response.status_code == 302
