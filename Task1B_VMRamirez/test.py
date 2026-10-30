import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="43bd511b-f406-4ba0-9d66-b606f13c1246",
    name="Filter Table Data by Country",
    tc_id="TC-266",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"table_visible": "true", "filter_search_input_field_visible": "true", "firstRowName": "Ben", "filtered_table_contains_first_row_name": "true"},
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 498726, "name": "ProductName", "value": "macbook", "session_value": "macbook", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}],
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://www.testmuai.com/selenium-playground/', instruction_id='6b07a06e4acb45a9ad1cc3d30c38928e'):
        await page.goto("https://www.testmuai.com/selenium-playground/")
    
    async with testmu.step('PRIMARY: Navigate to the Table Data Search page; role=link; text="Table Data Search" | HINTS: container=Selenium Playground links', instruction_id='3ddfcc60793e42b98ea719880c7b5bc0'):
        _loc_1 = page.locator("internal:role=link[name=\"Table Data Search\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('Checking whether the table is present'):
        set_var('table_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {21: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(21).getClientRects().length && getComputedStyle(el(21)).display !== 'none' && getComputedStyle(el(21)).visibility !== 'hidden'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:text="#TaskAssigneeStatus1DevelopmentAku Soficompleted2TestingHalima"i'], query='whether the table is present (in the table search filter section)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the table is visible'))
    
    async with testmu.step('Checking whether the filter/search input field is present'):
        set_var('filter_search_input_field_visible', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {20: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (!!(el(20).getClientRects().length && getComputedStyle(el(20)).display !== 'none' && getComputedStyle(el(20)).visibility !== 'hidden'));\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=textbox[name="Filter by Task / Assignee /"i]'], query='whether the filter/search input field is present (in the table search filter section)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the filter/search input field is visible'))
    
    async with testmu.step('the table and filter/search input field are visible', instruction_id='d59ee8aa239c4fc8890ce31fac077550'):
        await testmu.verify_assertion(page, 'the table and filter/search input field are visible', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the table is visible', 'store_key': 'table_visible', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{table_visible}}', 'variable_refs': {'{{table_visible}}': 'true'}, 'json_path': None}, {'description': 'the filter/search input field is visible', 'store_key': 'filter_search_input_field_visible', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{filter_search_input_field_visible}}', 'variable_refs': {'{{filter_search_input_field_visible}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'the visibility of the table and filter/search input field', 'claim': 'the table and filter/search input field are visible'})
    
    async with testmu.step('PRIMARY: Enter "Philippines" in the filter field; role=textbox; text="Filter by Task / Assignee / Status" | HINTS: container=main content below the "Table Search filter" heading', instruction_id='fe5bee9b219c4dd59e07fdb94480fd14'):
        element_0 = page.locator("internal:role=textbox[name=\"Filter by Task / Assignee /\"i]")
        
        await testmu.fill(element_0, "Philippines")
    
    async with testmu.step('PRIMARY: Wait for the table results to update', instruction_id='bfa95b7270344d53acc645e513228db0'):
        await page.wait_for_timeout(1000)
    
    async with testmu.step('Reading the Name value from the first visible data row'):
        set_var('firstRowName', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {44: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(44).textContent.trim());\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=cell[name="Ben"s]'], query='the Name value from the first visible data row in the table', expected_value='', needs_unit_conversion=False, operator='equals', transforms=['strip'], condition='the Name value from the first visible data row is stored in a LOCAL variable named firstRowName'))
    
    async with testmu.step('Checking whether the stored first-row Name is present in the filtered table'):
        set_var('filtered_table_contains_first_row_name', await testmu.textual_analyzer(page, wrapped_js="(els) => {\n  const __m = {44: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(44).textContent.trim() === 'Ben');\n  return (typeof __v === 'boolean' ? String(__v) : __v);\n}", locators=['internal:role=cell[name="Ben"s]'], query='whether the value stored in {{firstRowName}} in the filtered table is present (in the filtered table)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the filtered table contains the value stored in {{firstRowName}}'))
    
    async with testmu.step('the filtered table contains the value stored in {{firstRowName}}', instruction_id='0678ded686c542669bb02bd9294c60b9'):
        await testmu.verify_assertion(page, 'the filtered table contains the value stored in {{firstRowName}}', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the filtered table contains the value stored in {{firstRowName}}', 'store_key': 'filtered_table_contains_first_row_name', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{filtered_table_contains_first_row_name}}', 'variable_refs': {'{{filtered_table_contains_first_row_name}}': 'true', '{{firstRowName}}': 'Ben'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'the filtered table contains the value stored in {{firstRowName}}', 'claim': 'the filtered table contains the value stored in {{firstRowName}}'})


if __name__ == "__main__":
    testmu.run(test)