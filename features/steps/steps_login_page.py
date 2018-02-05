from behave import step
from hamcrest import *
from page_objects import HomePage, LibraryPage


@step(u'the user is on the login page')
def step_impl(ctx):
    home_page = HomePage(ctx.browser)
    ctx.login_page = home_page.click_login_button()


@step(u'the user does not fill any field')
def step_impl(ctx):
    ctx.login_page.email_field.clear()
    ctx.login_page.password_field.clear()


@step(u'the user clicks on login button')
def step_impl(ctx):
    ctx.login_page.click_on_login_button()


@step(u'the user should stay in the same page')
def step_impl(ctx):
    pass


@step(u'should see the email field with red borders')
def step_impl(ctx):
    assert_that(ctx.login_page.email_field.value_of_css_property("border-top-color"), is_('rgba(220, 78, 65, 1)'))
    assert_that(ctx.login_page.email_field.value_of_css_property("border-right-color"), is_('rgba(220, 78, 65, 1)'))
    assert_that(ctx.login_page.email_field.value_of_css_property("border-bottom-color"), is_('rgba(220, 78, 65, 1)'))
    assert_that(ctx.login_page.email_field.value_of_css_property("border-left-color"), is_('rgba(220, 78, 65, 1)'))


@step(u'should see the password field with red borders')
def step_impl(ctx):
    assert_that(ctx.login_page.password_field.value_of_css_property("border-top-color"), is_('rgba(220, 78, 65, 1)'))
    assert_that(ctx.login_page.password_field.value_of_css_property("border-right-color"), is_('rgba(220, 78, 65, 1)'))
    assert_that(ctx.login_page.password_field.value_of_css_property("border-bottom-color"), is_('rgba(220, 78, 65, 1)'))
    assert_that(ctx.login_page.password_field.value_of_css_property("border-left-color"), is_('rgba(220, 78, 65, 1)'))


@step(u'the user fill in only email field')
def step_impl(ctx):
    ctx.login_page.fill_email_field("user@domain.com")


@step(u'the user fill in only password field')
def step_impl(ctx):
    ctx.login_page.fill_password_field("Pa$$w0rd")


@step(u'the user inform the email "{email}"')
def step_impl(ctx, email):
    ctx.login_page.fill_email_field(email)


@step(u'the user inform the password "{password}"')
def step_impl(ctx, password):
    ctx.login_page.fill_password_field(password)


@step(u'the user should be redirected to the Library page')
def step_impl(ctx):
    ctx.library_page = LibraryPage(ctx.browser)


@step(u'should see the main menu')
def step_impl(ctx):
    assert_that(ctx.library_page.is_main_menu_visible(), is_(True))


@step(u'should see the section Upcomming Product')
def step_impl(ctx):
    assert_that(ctx.library_page.is_upcomming_product_session_visible(), is_(True))


@step(u'the email "{email}"')
def step_impl(ctx, email):
    ctx.login_page.fill_email_field(email)


@step(u'the password "{password}"')
def step_impl(ctx, password):
    ctx.login_page.fill_password_field(password)


@step(u'the user should see the error message "{error_message}"')
def step_impl(ctx, error_message):
    assert_that(ctx.login_page.get_error_message(), equal_to(error_message))


@step(u'the user access the login page')
def step_impl(ctx):
    ctx.login_page = HomePage(ctx.browser).click_login_button()


@step(u'the user clicks on "Forgot your password? Recover password" link')
def step_impl(ctx):
    ctx.forgot_password = ctx.login_page.click_on_forgot_password()


@step(u'the user should be redirected to "Reset Password" page')
def step_impl(ctx):
    pass


@step(u'should see the email field')
def step_impl(ctx):
    ctx.forgot_password.email_field.is_visible()


@step(u'should see the send button')
def step_impl(ctx):
    ctx.forgot_password.send_button.is_visible()
