import os
import testmu
from testmu import expect, var, set_var
from playwright.async_api import Page

testmu.configure(
    build="1f7eb194-d6ad-4053-a7fe-afe1639e1da6",
    name="Filter Table Data by Task Name",
    tc_id="TC-255",
    network=os.getenv("NETWORK", "false").lower() == "true",
    variables={"filtered_table_matching_rows_check": "true", "search_results_page_displayed": "true"},
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}],
    auto_heal_version="AH2",
    default_action_timeout_ms=60000,
    default_navigation_timeout_ms=60000,
    kane_run_v4=True,
)

@testmu.test
async def test(page: Page):
    async with testmu.step('Navigate to https://www.testmuai.com/selenium-playground/', instruction_id='a0d370887c8041f79378e171f34527de'):
        await page.goto("https://www.testmuai.com/selenium-playground/")
    
    async with testmu.step('PRIMARY: Table Data Search; role=link; text="Table Data Search" | HINTS: container=Selenium Playground demo list', instruction_id='f549df814125439ba02195fc0a4add77'):
        _loc_1 = page.locator("internal:role=link[name=\"Table Data Search\"i]")
        
        await _loc_1.click()
    
    async with testmu.step('PRIMARY: Run a search in Table Data Search; role=textbox; text="Filter by Task / Assignee / Status" | HINTS: position=above the task table; container=Table Search filter', instruction_id='3b8ff04edef8469f9be0b4fe6440a367'):
        element_0 = page.locator("internal:role=textbox[name=\"Filter by Task / Assignee /\"i]")
        
        try:
            await element_0.click(timeout=2000)
        except Exception:
            pass
        await element_0.fill("Development")
        try:
            await element_0.press("End", timeout=2000)
        except Exception:
            pass
    
    async with testmu.step("Checking the filtered table's visible rows"):
        set_var('filtered_table_matching_rows_check', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {21: 0};\n  const el = (i) => els[__m[i]];\n  const __v = ((()=>{const rows=[...el(21).querySelectorAll(\'tbody tr\')].filter(r=>getComputedStyle(r).display!=="none");return rows.length>0&&rows.every(r=>r.textContent.includes("Development"));})());\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['internal:text="#TaskAssigneeStatus1DevelopmentAku Soficompleted2TestingHalima"i'], query='whether the filtered table displaying only the matching rows is present (in the filtered task table)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the filtered table displays only the matching rows'))
    
    async with testmu.step('Checking whether the search results page is displayed'):
        set_var('search_results_page_displayed', await testmu.textual_analyzer(page, wrapped_js='(els) => {\n  const __m = {19: 0};\n  const el = (i) => els[__m[i]];\n  const __v = (el(19).textContent.trim()==="Table Search filter");\n  return (typeof __v === \'boolean\' ? String(__v) : __v);\n}', locators=['internal:role=heading[name="Table Search filter"i]'], query='whether the search results page is present (at the top of the page)', expected_value='true', needs_unit_conversion=False, operator='equals', transforms=[], condition='the search results page is displayed'))
    
    async with testmu.step('the filtered table displays only the matching rows', instruction_id='e9aab66ff2d14deaba60c802096b2a60'):
        await testmu.verify_assertion(page, 'the filtered table displays only the matching rows', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the filtered table displays only the matching rows', 'store_key': 'filtered_table_matching_rows_check', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{filtered_table_matching_rows_check}}', 'variable_refs': {'{{filtered_table_matching_rows_check}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'the filtered table displays only the matching rows', 'claim': 'the filtered table displays only the matching rows'})
    
    async with testmu.step('the search results page is displayed', instruction_id='6e6f028c684a4812a80e98155f2b5729'):
        await testmu.verify_assertion(page, 'the search results page is displayed', {'operator': ['equals'], 'assertion_operands': [], 'left_operand': None, 'right_operand': None, 'operands': [], 'sub_checks': [{'description': 'the search results page is displayed', 'store_key': 'search_results_page_displayed', 'expected_value': 'true', 'operator': 'equals', 'transforms': [], 'extracted_value': '{{search_results_page_displayed}}', 'variable_refs': {'{{search_results_page_displayed}}': 'true'}, 'json_path': None}], 'composite_operator': 'and', 'verification': 'the search results page is displayed', 'claim': 'the search results page is displayed'})


if __name__ == "__main__":
    testmu.run(test)