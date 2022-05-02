CONFIGURACION

Build:
1) Luego de clonar el proyecto: git clone

2) Instalar las dependencias: 
Install python. Versión 3.8 
python -m pip install pytest pytest-bdd seleniumbase pytest-html

3) Ejecucion con el navegador: 
pytest .\step_defs\homepage_test.py --browser=chrome

4) Ejecución con reporte sin warnings: 
pytest .\step_defs\homepage_test.py --html=report.html --disable-warnings

5) Ejecución con navegador en backgroud y reporte: 
pytest .\step_defs\homepage_test.py --headless --browser=chrome --dashboard --html=report.html --junit-xml=report.xml

6) Actualizar archivos
git add .
git commit -m "Mi Primer Commit"
git push -u origin main

DOCUMENTACIÓN

Usar https://seleniumbase.io/

from seleniumbase import BaseCase

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.saucedemo.com")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce\n")
        self.assert_element("#inventory_container")
        self.assert_text("PRODUCTS", "span.title")
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        self.assert_text("YOUR CART", "span.title")
        self.assert_text("Backpack", "div.cart_item")
        self.click("button#checkout")
        self.type("#first-name", "SeleniumBase")
        self.type("#last-name", "Automation")
        self.type("#postal-code", "77123")
        self.click("input#continue")
        self.assert_text("CHECKOUT: OVERVIEW")
        self.assert_text("Backpack", "div.cart_item")
        self.click("button#finish")
        self.assert_exact_text("THANK YOU FOR YOUR ORDER", "h2")
        self.assert_element('img[alt="Pony Express"]')
        self.js_click("a#logout_sidebar_link")



