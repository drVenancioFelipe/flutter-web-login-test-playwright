def login(page, email, password):
    page.fill("input[type='email']", email)
    page.fill("input[type='password']", password)
    page.click("button:has-text('Entrar')")