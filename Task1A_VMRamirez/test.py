import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="7e560f56-8bb2-4ec8-8825-23a3a5f573e7",
    name="Submit Input Form with User Details",
    tc_id="TC-265",
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
    async with testmu.step('Navigate to https://www.testmuai.com/selenium-playground/', instruction_id='e629a7796a0d4efa93c82f4eddc916e2'):
        await page.goto("https://www.testmuai.com/selenium-playground/")
    
    async with testmu.step('PRIMARY: Input Form Submit; role=link; text="Input Form Submit" | HINTS: container=Selenium Playground list', instruction_id='dd5b80d57d7f47589d39262bd0ab4a4b'):
        _loc_1 = page.locator("internal:role=link[name=\"Input Form Submit\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the Input Form Submit page is present'):
        set_var('input_form_submit_page_displayed', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(20).textContent.trim() === 'Input form validations');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=heading[name="Input form validations"i]'], query='whether the Input Form Submit page is present (in the form demo content area)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the Input Form Submit page is displayed'))
    
    async with testmu.step('the Input Form Submit page is displayed', instruction_id='7b4ba6d29ff94630b3e1176aa9a710df'):
        await testmu.verify_assertion(page, 'the Input Form Submit page is displayed', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the Input Form Submit page is displayed', 'store_key': 'input_form_submit_page_displayed', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{input_form_submit_page_displayed}}', 'variable_refs': {'{{input_form_submit_page_displayed}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'the Input Form Submit page is displayed', 'claim': 'the Input Form Submit page is displayed'})
    
    async with testmu.step('queued plan (8 steps): type "Name"; type "Email*"; type "Password*"; type "Company"; type "Website"; select "combobox"; type "City"; type "Address 1"', instruction_id='8335f15dc80a4b6182825ac33877eb80'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('PRIMARY: Name; role=textbox; text="Name" | HINTS: container=input form validations', instruction_id='cf36b96a9b2d448b87035374a577d14f'):
        element_0 = page.locator("internal:role=textbox[name=\"Name\"i]")
        
        await testmu.fill(element_0, "Victor Ramirez")
    
    async with testmu.step('PRIMARY: Email; role=textbox; text="Email*" | HINTS: container=input form validations', instruction_id='fe7614604db2429f83dd30b41dbfe774'):
        element_1 = page.locator("internal:role=textbox[name=\"Email*\"i]")
        
        await testmu.fill(element_1, "victor.ramirez@test.com")
    
    async with testmu.step('PRIMARY: Password; role=textbox; text="Password*" | HINTS: container=input form validations', instruction_id='b5ed66f1941541159897cde6cec45bda'):
        element_2 = page.locator("internal:role=textbox[name=\"Password*\"i]")
        
        await testmu.fill(element_2, "Test@123")
    
    async with testmu.step('PRIMARY: Company; role=textbox; text="Company" | HINTS: container=input form validations', instruction_id='74a610e3b56f434a81199a95968b3b89'):
        element_3 = page.locator("internal:role=textbox[name=\"Company\"i]")
        
        await testmu.fill(element_3, "Test Company Name")
    
    async with testmu.step('PRIMARY: Website; role=textbox; text="Website" | HINTS: container=input form validations', instruction_id='556ef690dcd445a99fd7fd6507ca32d0'):
        element_4 = page.locator("internal:role=textbox[name=\"Website\"i]")
        
        await testmu.fill(element_4, "https://example.com")
    
    async with testmu.step('PRIMARY: Country; role=combobox; text="Country*" | HINTS: container=input form validations', instruction_id='8af5f4a3e1ff4f29939550980a01d3de'):
        element_5 = page.locator("internal:role=combobox")
        
        await element_5.select_option(value='Philippines')
    
    async with testmu.step('PRIMARY: City; role=textbox; text="City" | HINTS: container=input form validations', instruction_id='ad6ce6b40ca84b86ad4fb0ef19ca87f1'):
        element_6 = page.locator("internal:role=textbox[name=\"City\"s]")
        
        await testmu.fill(element_6, "Manila")
    
    async with testmu.step('PRIMARY: Address 1; role=textbox; text="Address 1" | HINTS: container=input form validations', instruction_id='249c70d22ba5400e9a0bb6a98b896c88'):
        element_7 = page.locator("internal:role=textbox[name=\"Address 1\"i]")
        
        await testmu.fill(element_7, "123 Carnation St.")
    
    async with testmu.step('queued plan (3 steps): type "Address 2"; type "City* State*"; type "Zip Code*"', instruction_id='a691a03f6e914501b5c8f0ec855cd11d'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('PRIMARY: Address 2; role=textbox; text="Address 2" | HINTS: container=input form validations', instruction_id='133c80b07d31408bb132ab73fb9487a1'):
        element_8 = page.locator("internal:role=textbox[name=\"Address 2\"i]")
        
        await testmu.fill(element_8, "Unit 3")
    
    async with testmu.step('PRIMARY: State; role=textbox; text="State*" | HINTS: container=input form validations', instruction_id='b87dce7576d744b891ee727ce44cda0e'):
        element_9 = page.locator("internal:role=textbox[name=\"City* State*\"i]")
        
        await testmu.fill(element_9, "Metro Manila")
    
    async with testmu.step('PRIMARY: Zip Code; role=textbox; text="Zip Code*" | HINTS: container=input form validations', instruction_id='6c57e70cabc74fbc9d0d5a48cb681e60'):
        element_10 = page.locator("internal:role=textbox[name=\"Zip Code*\"i]")
        
        await testmu.fill(element_10, "1600")
    
    async with testmu.step('PRIMARY: wait briefly after filling all required fields', instruction_id='6ca0109291f54979980d2f22ac140a93'):
        await page.wait_for_timeout(300)
    
    async with testmu.step('Scroll into view: PRIMARY: Submit button; role=button; text="Submit" | HINTS: container=input form validations; below Zip Code', instruction_id='53295989991d4006aa8bb02d6a9d8412'):
        element_11 = page.locator("internal:role=button[name=\"Submit\"i]")
        await element_11.evaluate("el => el.scrollIntoView({block: 'center'})")
    
    async with testmu.step('PRIMARY: Submit button; role=button; text="Submit" | HINTS: container=input form validations; below Zip Code', instruction_id='aff4434b30254c0394d1f03d227a9f32'):
        _loc_2 = page.locator("internal:role=button[name=\"Submit\"i]")
        
        await _loc_2.click()
    
    async with testmu.step('PRIMARY: wait for the submission result to appear', instruction_id='a0c74bcecc9446feba5d7d1ab69be901'):
        await page.wait_for_timeout(300)


if __name__ == "__main__":
    testmu.run(test)