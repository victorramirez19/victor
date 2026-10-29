import os
import testmu_appium
from testmu_appium import var, set_var

testmu_appium.configure(
    kane_run_v4=True,
    platform="ios",
    app="lt://APP10160222121793249551598179",
    device_name="iPhone.*",
    platform_version="18",
    build="375de3d3-18d1-4465-aab4-e2a520ff1921",
    name="Navigate and Interact with App Features",
    tc_id="TC-259",
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}],
    default_action_timeout_ms=10000,
)

@testmu_appium.test
def test(driver):
    with testmu_appium.step('PRIMARY: Toast Button; role=button; text="Toast" | HINTS: position=middle-left', instruction_id='dc67882339c347178b8030423e7ba18e'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "toast", "score": 80, "isXPath": False, "strategy": "accessibility_id"},
                {"selector": "Toast", "score": 15, "isXPath": False, "strategy": "text"},
            ],
            description='PRIMARY: Toast Button; role=button; text="Toast" | HINTS: position=middle-left',
        )

    with testmu_appium.step('PRIMARY: Colour button; role=button; text="Colour" | HINTS: position=middle-left; container=main action grid', instruction_id='de8451dd7fae45a4b948f2380059b6b9'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "color", "score": 80, "isXPath": False, "strategy": "accessibility_id"},
                {"selector": "Colour", "score": 15, "isXPath": False, "strategy": "text"},
            ],
            description='PRIMARY: Colour button; role=button; text="Colour" | HINTS: position=middle-left; container=main action grid',
        )

    with testmu_appium.step('PRIMARY: Text button; role=button; text="Text" | HINTS: position=middle-left; container=main button grid', instruction_id='d613ae01f2bb4871815932b8f6698af1'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "type == \"XCUIElementTypeButton\" AND name == \"Text\"", "score": 85, "isXPath": False, "strategy": "predicate"},
                {"selector": "Text", "score": 35, "isXPath": False, "strategy": "accessibility_id"},
            ],
            description='PRIMARY: Text button; role=button; text="Text" | HINTS: position=middle-left; container=main button grid',
        )

    with testmu_appium.step('PRIMARY: Notification button; role=button; text="Notification" | HINTS: position=middle-right; neighbor=Toast button', instruction_id='f2420d9e511949aea66a278e4ae6295f'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "notification", "score": 80, "isXPath": False, "strategy": "accessibility_id"},
                {"selector": "Notification", "score": 15, "isXPath": False, "strategy": "text"},
            ],
            description='PRIMARY: Notification button; role=button; text="Notification" | HINTS: position=middle-right; neighbor=Toast button',
        )

    with testmu_appium.step('PRIMARY: GeoLocation button; role=button; text="GeoLocation" | HINTS: position=middle-right; container=main controls', instruction_id='a2d922bcd477455e900cd10880a4bbc3'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "geoLocation", "score": 80, "isXPath": False, "strategy": "accessibility_id"},
                {"selector": "GeoLocation", "score": 15, "isXPath": False, "strategy": "text"},
            ],
            description='PRIMARY: GeoLocation button; role=button; text="GeoLocation" | HINTS: position=middle-right; container=main controls',
        )

    with testmu_appium.step('PRIMARY: Back navigation button; role=button; text="Back" | HINTS: position=top-left', instruction_id='eb83a38906374fafaf3c54a1f87a55b0'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "Back", "score": 80, "isXPath": False, "strategy": "accessibility_id"},
            ],
            description='PRIMARY: Back navigation button; role=button; text="Back" | HINTS: position=top-left',
        )

    with testmu_appium.step('Close the Proverbial app', instruction_id='3f96e188a9534aba87dc7dedd272008b'):
        testmu_appium.app_lifecycle(
            driver,
            "terminate",
            app_id="proverbial",
            description='Close the Proverbial app',
        )


def _apply_test_config(path, instance_id):
    import json
    with open(path) as f:
        groups = json.load(f)
    entry = None
    for tests in groups.values():
        for candidate in tests:
            if instance_id in (None, "", candidate.get("test_instance_id")):
                entry = candidate
                break
        if entry is not None:
            break
    if entry is None:
        raise SystemExit(
            "test instance %r not found in %s" % (instance_id, path)
        )
    testmu_appium.configure(**testmu_appium.test_config_overrides(entry))


if __name__ == "__main__":
    import argparse
    _parser = argparse.ArgumentParser()
    _parser.add_argument("--test-config")
    _parser.add_argument("--test-instance-id")
    # Accepted for run.sh compatibility; the V4 artifact has no ops metadata.
    _parser.add_argument("--operations-meta-data")
    _args, _ = _parser.parse_known_args()
    if _args.test_config:
        _apply_test_config(_args.test_config, _args.test_instance_id)
    testmu_appium.run(test)

