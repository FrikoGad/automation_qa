from pages.forms_page import FormsPage


class TestForms:
    class TestFormsPage:
        def test_forms(self, driver):
            form_page = FormsPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_forms_fields()
            result = form_page.form_result()
            assert [person_info.first_name + " " + person_info.last_name, person_info.email] == [result[0], result[1]], "the form has not been filled"
