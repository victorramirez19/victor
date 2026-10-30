import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="0ea422d7-b4e6-4505-8e15-dea180435f0f",
    name="Verify Disabled Checkbox Status",
    tc_id="TC-276",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"option_1_completed_check": "true"},
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 504951, "name": "api_get_selenium_playground_status", "value": "200", "session_value": "200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 504856, "name": "num1", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 504857, "name": "num2", "value": "200", "session_value": "200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 498726, "name": "ProductName", "value": "macbook", "session_value": "macbook", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}],
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://www.testmuai.com/selenium-playground/', instruction_id='72df4b0524084c6eb6fb28390046ec8a'):
        await page.goto("https://www.testmuai.com/selenium-playground/")
    
    async with testmu.step('PRIMARY: Click Checkbox Demo; role=link; text="Checkbox Demo" | HINTS: container=Selenium Playground link grid', instruction_id='515995be8a7d4fbd8056b5ca6cb327ed'):
        _loc_1 = page.locator("internal:role=link[name=\"Checkbox Demo\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('PRIMARY: Click on Option 1 in Disabled Checkbox Demo; role=checkbox; text="Option 1" | HINTS: container=Disabled Checkbox Demo, below Single Checkbox Demo', instruction_id='e87e7f44887842b0999aa41ac524fab2'):
        _loc_2 = page.locator("internal:role=checkbox[name=\"Option\"i] >> nth=0")
        
        await _loc_2.click()
    
    async with testmu.step('Checking whether Option 1 is completed'):
        set_var('option_1_completed_check', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {24: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(24).checked);\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=checkbox[name="Option"i] >> nth=0'], query='whether Option 1 completed is present (in the Disabled Checkbox Demo)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='Option 1 is completed'))
    
    async with testmu.step('Option 1 is completed', instruction_id='83107b56cd07486986a6648e92f7923c'):
        await testmu.verify_assertion(page, 'Option 1 is completed', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'Option 1 is completed', 'store_key': 'option_1_completed_check', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{option_1_completed_check}}', 'variable_refs': {'{{option_1_completed_check}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'Whether Option 1 is completed in the current browser state.', 'claim': 'Option 1 is completed'})


if __name__ == "__main__":
    testmu.run(test)