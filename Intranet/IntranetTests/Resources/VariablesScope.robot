*** Settings ***
Library  SeleniumLibrary

*** Variables ***
# Global
${BROWSER}  chrome
${HOST_READER}  http:/localhost:8080/
${URL_ODOO}  https://demo4.odoo.com/web#cids=1&action=menu

# Odoo Reader Variables ---------------------

${verifying_text_active}  Active Project Names
${verifying_text_favorite}  Favorite Project Names


# Odoo Demo Variables ---------------------

${login_odoo}  admin
${password_odoo}  admin
