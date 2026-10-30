import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="1b97bc3c-0031-4fa7-8426-f03fc5dc9529",
    name="Complete and Submit Input Form",
    tc_id="TC-267",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"input_form_submit_page_displayed": "true"},
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 498726, "name": "ProductName", "value": "macbook", "session_value": "macbook", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}],
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://www.testmuai.com/selenium-playground/input-form-demo/', instruction_id='ef10a353829746c3b7ab398070fafee6'):
        await page.goto("https://www.testmuai.com/selenium-playground/input-form-demo/")
    
    async with testmu.step('whether the Input Form Submit page is present (in the main page content)', instruction_id='8aae8c035471409e93d6ec411d7984f0'):
        set_var('input_form_submit_page_displayed', await testmu.vision_query(page, "whether the Input Form Submit page is present (in the main page content)", "", expected_value='true'))
    
    async with testmu.step('the Input Form Submit page is displayed', instruction_id='2bcf74170e6b401da29bf73e97982d27'):
        await testmu.verify_assertion(page, 'the Input Form Submit page is displayed', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the Input Form Submit page is displayed', 'store_key': 'input_form_submit_page_displayed', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{input_form_submit_page_displayed}}', 'variable_refs': {'{{input_form_submit_page_displayed}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'the Input Form Submit page', 'claim': 'the Input Form Submit page is displayed'})
    
    async with testmu.step('queued plan (8 steps): type "Name"; type "Email*"; type "Password*"; type "Company"; type "Website"; select "combobox"; type "City"; type "Address 1"', instruction_id='ea215a188c82422d9425f9e0478a0f55'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Name; role=textbox; text="Name" | HINTS: container=Input form validations', instruction_id='6c8f19fcd9194e8c9fb352db6917c89d'):
        element_0 = page.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Victor Ramirez")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Email; role=textbox; text="Email*" | HINTS: container=Input form validations', instruction_id='f1d7c431863a446e9ce3636b64aef753'):
        element_1 = page.locator("internal:role=textbox[name=\"Email*\"i]")
        
        await testmu.fill(element_1, "victor.ramirez@test.com")
    
    async with testmu.step('queued plan (8 steps): type "Password*"; type "Company"; type "Website"; select "combobox"; type "City"; type "Address 1"; type "Address 2"; type "City* State*"', instruction_id='852d8b2c02764d7abe8587b2c9b0fd36'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Password; role=textbox; text="Password*" | HINTS: container=Input form validations', instruction_id='f6f51fcc14c94f36887c0d9a4b20c393'):
        element_2 = page.locator("internal:role=textbox[name=\"Password*\"i]")
        
        await testmu.fill(element_2, "Test@12345")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Company; role=textbox; text="Company" | HINTS: container=Input form validations', instruction_id='442e8d2d1ae142b1ac842e0c5ff8afaa'):
        element_3 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_3, "Test Company New")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Website; role=textbox; text="Website" | HINTS: container=Input form validations', instruction_id='29f28e335ab04a34a7faaf57fcd58d2b'):
        element_4 = page.locator("internal:role=textbox[name=\"Website\"i]")
        
        await testmu.fill(element_4, "https://test.com")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Country; role=combobox; text="Country*" | HINTS: container=Input form validations', instruction_id='85907c97f4a04572997f660121dc844b'):
        element_5 = page.locator("internal:role=combobox")
        
        await element_5.select_option(value='Philippines')
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: City; role=textbox; text="City" | HINTS: container=Input form validations', instruction_id='a5553595ead348348b3705490fc7f58e'):
        element_6 = page.locator("internal:role=textbox[name=\"City\"s]")
        
        await testmu.fill(element_6, "Manila")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Address 1; role=textbox; text="Address 1" | HINTS: container=Input form validations', instruction_id='b1f636241315440a8571f6b19e911e59'):
        element_7 = page.locator("internal:role=textbox[name=\"Address 1\"i]")
        
        await testmu.fill(element_7, "456 Carnation Street")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Address 2; role=textbox; text="Address 2" | HINTS: container=Input form validations', instruction_id='2ddc32a1713b4a78bd1854909be3cbf1'):
        element_8 = page.locator("internal:role=textbox[name=\"Address 2\"i]")
        
        await testmu.fill(element_8, "Unit 23")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: State; role=textbox; text="State*" | HINTS: container=Input form validations', instruction_id='5ef67a5c4f1941cab65d2a113fa71cde'):
        element_9 = page.locator("internal:role=textbox[name=\"City* State*\"i]")
        
        await testmu.fill(element_9, "Metro Manila")
    
    async with testmu.step('PRIMARY: Fill in all required fields with valid test data: Zip Code; role=textbox; text="Zip Code*" | HINTS: container=Input form validations', instruction_id='fc265f3b084442c0a9bd10c6e152d1bd'):
        element_10 = page.locator("internal:role=textbox[name=\"Zip Code*\"i]")
        
        await testmu.fill(element_10, "1600")
    
    async with testmu.step('Scroll into view: PRIMARY: Click the Submit button; role=button; text="Submit" | HINTS: container=Input form validations', instruction_id='833a1232a46343c680d315e34f1522ed'):
        element_11 = page.locator("internal:role=button[name=\"Submit\"i]")
        await element_11.evaluate("el => el.scrollIntoView({block: 'center'})")
    
    async with testmu.step('PRIMARY: Click the Submit button; role=button; text="Submit" | HINTS: container=Input form validations', instruction_id='15ce7f23ff164584a140437cd50aaaad'):
        _loc_1 = page.locator("internal:role=button[name=\"Submit\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('PRIMARY: Wait for the form submission result', instruction_id='d62365ddd52b49448c1212c9e3dc255c'):
        await page.wait_for_timeout(1000)


if __name__ == "__main__":
    testmu.run(test)