import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="d0039acb-204a-4bdc-86f9-2209c4e00168",
    name="Verify Sum Calculation in Simple Form Demo",
    tc_id="TC-268",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"simple_form_demo_page_displayed": "true", "num1": "12", "num2": "8", "displayed_sum_equals_expected_sum": "20"},
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 498726, "name": "ProductName", "value": "macbook", "session_value": "macbook", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}, {"name": "num1", "value": "100", "environment_id": 0, "scope": "global", "session_value": "100", "environment_name": "", "is_persist": True, "id": 504856}, {"name": "num2", "value": "200", "environment_id": 0, "scope": "global", "session_value": "200", "environment_name": "", "is_persist": True, "id": 504857}],
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://www.testmuai.com/selenium-playground/simple-form-demo/', instruction_id='8edd9039b1564117a6a73dfcec324212'):
        await page.goto("https://www.testmuai.com/selenium-playground/simple-form-demo/")
    
    async with testmu.step('Checking whether the Simple Form Demo page is present'):
        set_var('simple_form_demo_page_displayed', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {19: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(19).textContent.trim() === 'Simple Form Demo');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Simple Form Demo"i]'], query='whether Simple Form Demo page is present (in the main page heading)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the Simple Form Demo page is displayed'))
    
    async with testmu.step('the Simple Form Demo page is displayed', instruction_id='c62e55cfc0d9488b97a16783a07a0b17'):
        await testmu.verify_assertion(page, 'the Simple Form Demo page is displayed', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the Simple Form Demo page is displayed', 'store_key': 'simple_form_demo_page_displayed', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{simple_form_demo_page_displayed}}', 'variable_refs': {'{{simple_form_demo_page_displayed}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'Simple Form Demo page display', 'claim': 'the Simple Form Demo page is displayed'})
    
    async with testmu.step('PRIMARY: locate the two number input fields used for addition and create or use dataset parameters named num1 for the first number and num2 for the second number', instruction_id='fc77f275735a4f7387cd7e55edd7ee2f'):
        await page.wait_for_timeout(500)
    
    async with testmu.step('queued plan (3 steps): type "Please enter first value"; type "Please enter second value"; click "Get Sum"', instruction_id='0274ca9128b6477eba55f48a6972c699'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Storing the first numeric value', instruction_id='e3dfb9934edc4d1da1d632b5ca6b0f8f'):
        set_var('num1', "12")
    
    async with testmu.step('Storing the second numeric value', instruction_id='dbfc9382a5144fec96152b26da405b49'):
        set_var('num2', "8")
    
    async with testmu.step('queued plan (3 steps): type "Please enter first value"; type "Please enter second value"; click "Get Sum"', instruction_id='97f1fa7d61a843c9bc22d4a66410099c'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('PRIMARY: first number field; role=textbox; text="Please enter first value" | HINTS: container=Two Input Fields section', instruction_id='a405cbd016e24d2a83023a28e6d3b7e8'):
        element_0 = page.locator("internal:role=textbox[name=\"Please enter first value\"i]")
        variable_value_1 = var('${num1}')
        
        await testmu.fill(element_0, variable_value_1)
    
    async with testmu.step('Scroll into view: PRIMARY: second number field; role=textbox; text="Please enter second value" | HINTS: container=Two Input Fields section', instruction_id='5a11a3e2c1c44d60a93bdab4b9a8ccd3'):
        element_2 = page.locator("internal:role=textbox[name=\"Please enter second value\"i]")
        await element_2.evaluate("el => el.scrollIntoView({block: 'center'})")
    
    async with testmu.step('PRIMARY: second number field; role=textbox; text="Please enter second value" | HINTS: container=Two Input Fields section', instruction_id='3e833db904da4918a88d74ecccf63307'):
        element_3 = page.locator("internal:role=textbox[name=\"Please enter second value\"i]")
        variable_value_4 = var('${num2}')
        
        await testmu.fill(element_3, variable_value_4)
    
    async with testmu.step('PRIMARY: Get Sum button; role=button; text="Get Sum" | HINTS: container=Two Input Fields section, below the number fields', instruction_id='c0892b2d19a74f9ab6c0c261d3067c3c'):
        _loc_1 = page.locator("internal:role=button[name=\"Get Sum\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('PRIMARY: enter 12 into the first number field and enter 8 into the second number field', instruction_id='1364cb359c154aeba85241720dea0c32'):
        await page.wait_for_timeout(300)
    
    async with testmu.step('PRIMARY: click the Get Sum button, read the displayed sum, and calculate the expected sum by adding 12 and 8', instruction_id='7d8b515f1eb84f01add9c7b14b64a592'):
        await page.wait_for_timeout(300)
    
    async with testmu.step('Reading the displayed sum from the two-input form'):
        set_var('displayed_sum_equals_expected_sum', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {38: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(38).textContent.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="20"s'], query='the displayed sum result in the two-input form', expected_value='20', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the displayed sum equals the calculated expected sum by adding ${num1} and ${num2}'))
    
    async with testmu.step('the displayed sum equals the calculated expected sum by adding ${num1} and ${num2}', instruction_id='785b53b614054f00b8709c34394aeb96'):
        await testmu.verify_assertion(page, 'the displayed sum equals the calculated expected sum by adding ${num1} and ${num2}', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the displayed sum equals the calculated expected sum by adding ${num1} and ${num2}', 'store_key': 'displayed_sum_equals_expected_sum', 'expected_value': '20', 'operator': 'equals', 'transforms': ['strip'], 'extracted_value': '{{displayed_sum_equals_expected_sum}}', 'variable_refs': {'{{displayed_sum_equals_expected_sum}}': '20'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'displayed sum and calculated expected sum', 'claim': 'the displayed sum equals the calculated expected sum by adding ${num1} and ${num2}'})


if __name__ == "__main__":
    testmu.run(test)