import allure
from selene import have


def test_register(window, demoqa):
    response = demoqa.post(
        '/login',
        json={'Email': 'sopemoc825@vootin.com', 'Password': '4!sG!enS!Kieg'},
        allow_redirects=False
    )
    authorization_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    window.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})


def test_open_account(window):
    with allure.step('Open an account'):
        window.element('a.account').click()
        window.element('div.page-title > h1').should(have.text('My account - Customer info'))


def test_clear_cart(window, demoqa):
    with allure.step('Clear cart'):
        demoqa.post('/addproducttocart/catalog/31/1/1')
        window.element('.ico-cart').click()
        window.element('.qty-input').clear().send_keys(0).press_enter()
        window.element('div.order-summary-content').should(
            have.text('Your Shopping Cart is empty!')
        )


def test_successful_search(window):
    with allure.step('Successful search'):
        window.element('.search-box-text').type('Нокиа 3310').press_enter()
        window.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_logout(window, demoqa):
    with allure.step('Logout'):
        window.element('.ico-logout').click()
        response = demoqa.get('/logout', allow_redirects=False)
        assert response.status_code == 302
