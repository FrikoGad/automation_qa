from pages.forms_page import FormsPage


class TestForms:
    class TestFormsPage:
        def test_forms(self, driver):
            form_page = FormsPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            form_page.fill_forms_fields()