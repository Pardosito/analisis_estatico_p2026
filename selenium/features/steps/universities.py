"""Step definitions for the Google search Behave feature."""

# pylint: disable=import-error

from behave import given, step, then, when  # pylint: disable=no-name-in-module
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver


@given("I am on the Google homepage")  # pylint: disable=not-callable
def open_browser(context):
    """Opens Google in Chrome."""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.google.com")
    context.driver.maximize_window()


@when('I search for "{query}"')  # pylint: disable=not-callable
def search(context, query):
    """Searches university in Google."""
    search_box = context.driver.find_element("id", "APjFqb")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    delay = 5  # seconds
    wait = WebDriverWait(context.driver, delay)
    wait.until(EC.presence_of_element_located((By.ID, "rcnt")))


@then(  # pylint: disable=not-callable
    'the results page title should start with "{query}"'
)
def verify_results(context, query):
    """Prints the title of the Google search results page."""
    title = context.driver.title
    assert title.startswith(query) is True


@step('I click on "{query}"')  # pylint: disable=not-callable
def enter_page(context, query):
    """Enters the top result"""
    del query
    wait = WebDriverWait(context.driver, 10)
    first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
    first_result.click()


@step(
    'the new page title should start with "{expected_title}"'
)  # pylint: disable=not-callable
def verify_university(context, expected_title):
    """Checks the universities title page"""
    title = context.driver.title
    assert title.startswith(expected_title) is True


@step('inside the page I click on "{careers}"')  # pylint: disable=not-callable
def click_careers_section(context, careers):
    """Clicks a link based on its visible text."""
    wait = WebDriverWait(context.driver, 10)
    clean_careers = careers.strip()

    try:
        lower_careers = clean_careers.lower()
        xpath = (
            "//a["
            "contains(translate(normalize-space(.), "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ', 'abcdefghijklmnopqrstuvwxyzáéíóú'), "
            f"'{lower_careers}') or "
            "contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ', "
            f"'abcdefghijklmnopqrstuvwxyzáéíóú'), '{lower_careers}') or "
            "contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ', "
            f"'abcdefghijklmnopqrstuvwxyzáéíóú'), '{lower_careers}')"
            "]"
        )
        enlaces = wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
        click = False
        for enlace in enlaces:
            try:
                context.driver.execute_script("arguments[0].click();", enlace)
                click = True
                break
            except WebDriverException:
                continue

        if not click:
            raise RuntimeError(
                "se encontraron enlaces pero no se pudo hacer clic en ninguno, toy jodio"
            )

    except WebDriverException as exc:
        print(f"no se pudo encontrar y/o hacer clic en la seccion: '{clean_careers}'")
        with open("error_dom.html", "w", encoding="utf-8") as f:
            f.write(context.driver.page_source)
        raise exc
