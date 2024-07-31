from datetime import datetime

ADMIN_COOKIE = {
    'name': 'token',
    'value': ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjlmMmE0ZGRlY'
              'mI5YzAwMTM0MWE4ZWQiLCJpYXQiOjE3MjIxNDY0MTV9'
              '._sSTBx1Mers5iC1Oma3bs9_XzRkMGZjKc26Oir-HJWc'),
    'domain': 'thinking-tester-contact-list.herokuapp.com',
    'path': '/',
    'expiry': int(datetime(2025, 7, 28, 16, 0, 15).timestamp()),
    'size': 154,
    'priority': 'medium'
}


class Cookie:

    @staticmethod
    def set_admin_cookie(driver):
        driver.get("https://thinking-tester-contact-list.herokuapp.com")

        driver.add_cookie(ADMIN_COOKIE)
        return driver
