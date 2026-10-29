import os
import testmu_appium
from testmu_appium import var, set_var

testmu_appium.configure(
    kane_run_v4=True,
    platform="android",
    app_id="com.lambdatest.proverbial",
    app="lt://APP10160231331793247765862229",
    device_name="^(?!.*(Tab|Fold|Xiaomi|Redmi|Oppo|Moto|OnePlus|Vivo|Huawei|Realme)).*",
    platform_version="15",
    build="db9d0e34-d968-4291-8a1d-686e6ad8224c",
    name="Test Button Interactions and Navigation in Proverbial App",
    tc_id="TC-257",
    test_params={"Email": "prince.ronquillo@bnext.tech", "email_address_cert": "test.account@gmail.com", "email_jp": "testmuaijp@test.com", "Email_PCR": "test.account@gmail.com", "FIORI_PHDC": "https://192.168.8.33:44300/sap/bc/ui2/flp?sap-client=300&sap-language=EN", "JP_SecretPassword": "testpass", "login_cert": "test.account@gmail.com", "Password": "Pcr!199617pcr2", "password_cert": "Testaccount123", "password_jp": "testpass", "Password_Russel": "TestPacific@123", "User_Russel": "TEST_FI", "Username": "PRONQUILLO"},
    global_variables=[{"id": 143728, "name": "Asset_Class", "value": "3200", "session_value": "3200", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143727, "name": "Company_Code", "value": "5810", "session_value": "5810", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 143752, "name": "Cost_Center", "value": "58101501", "session_value": "58101501", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351297, "name": "FirstName", "value": "John", "session_value": "John", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 417794, "name": "loginPassword", "value": "Test@12345", "session_value": "Test@12345", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 349418, "name": "phdc_bp", "value": "100", "session_value": "100", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 351317, "name": "PHDC_TCODE", "value": "Maintain Business Partner", "session_value": "Maintain Business Partner", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 337953, "name": "product_cert", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411786, "name": "product_search", "value": "iPhone", "session_value": "iPhone", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 411799, "name": "register_email", "value": "testmuaijp3@test.com", "session_value": "testmuaijp3@test.com", "is_persist": True, "environment_id": 0, "environment_name": "No Env"}, {"id": 133664, "name": "Username", "value": "PRONQUILLO", "session_value": "PRONQUILLO", "is_persist": False, "environment_id": 0, "environment_name": "No Env"}],
    default_action_timeout_ms=10000,
)

@testmu_appium.test
def test(driver):
    with testmu_appium.step('PRIMARY: Color button; role=button; text="COLOR" | HINTS: position=middle-left; container=main app screen', instruction_id='6c9044cdd2ff4cfb96c4adfaddbe5b57'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "com.lambdatest.proverbial:id/color", "score": 90, "isXPath": False, "strategy": "view_id"},
                {"selector": "COLOR", "score": 60, "isXPath": False, "strategy": "text"},
                {"selector": "{\"v\":1,\"op\":\"attrs_xpath\",\"target\":{\"resource_id\":\"com.lambdatest.proverbial:id/color\",\"text\":\"COLOR\"}}", "score": 51, "isXPath": False, "strategy": "attrs_xpath"},
            ],
            description='PRIMARY: Color button; role=button; text="COLOR" | HINTS: position=middle-left; container=main app screen',
        )

    with testmu_appium.step('PRIMARY: Text button; role=button; text="TEXT" | HINTS: position=middle-left; container=main app screen', instruction_id='18069f506f5740cfb51595beb2c034e0'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "com.lambdatest.proverbial:id/Text", "score": 90, "isXPath": False, "strategy": "view_id"},
                {"selector": "TEXT", "score": 60, "isXPath": False, "strategy": "text"},
                {"selector": "{\"v\":1,\"op\":\"attrs_xpath\",\"target\":{\"resource_id\":\"com.lambdatest.proverbial:id/Text\",\"text\":\"TEXT\"}}", "score": 51, "isXPath": False, "strategy": "attrs_xpath"},
            ],
            description='PRIMARY: Text button; role=button; text="TEXT" | HINTS: position=middle-left; container=main app screen',
        )

    with testmu_appium.step('PRIMARY: Toast button; role=button; text="TOAST" | HINTS: position=middle-left; container=main Proverbial screen', instruction_id='e44d2486e8394611b63eaad8598ff7cb'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "com.lambdatest.proverbial:id/toast", "score": 90, "isXPath": False, "strategy": "view_id"},
                {"selector": "TOAST", "score": 60, "isXPath": False, "strategy": "text"},
                {"selector": "{\"v\":1,\"op\":\"attrs_xpath\",\"target\":{\"resource_id\":\"com.lambdatest.proverbial:id/toast\",\"text\":\"TOAST\"}}", "score": 51, "isXPath": False, "strategy": "attrs_xpath"},
            ],
            description='PRIMARY: Toast button; role=button; text="TOAST" | HINTS: position=middle-left; container=main Proverbial screen',
        )

    with testmu_appium.step('PRIMARY: Geolocation button; role=button; text="GEOLOCATION" | HINTS: position=middle-right; container=main content', instruction_id='af796fe14d514671964b06e564c91bd9'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "com.lambdatest.proverbial:id/geoLocation", "score": 90, "isXPath": False, "strategy": "view_id"},
                {"selector": "GEOLOCATION", "score": 60, "isXPath": False, "strategy": "text"},
                {"selector": "{\"v\":1,\"op\":\"attrs_xpath\",\"target\":{\"resource_id\":\"com.lambdatest.proverbial:id/geoLocation\",\"text\":\"GEOLOCATION\"}}", "score": 51, "isXPath": False, "strategy": "attrs_xpath"},
            ],
            description='PRIMARY: Geolocation button; role=button; text="GEOLOCATION" | HINTS: position=middle-right; container=main content',
        )

    with testmu_appium.step('PRIMARY: Home navigation button; role=group; text="Home" | HINTS: position=bottom-right; container=bottom navigation bar', instruction_id='5999a0dd1ca3418b9f1f7c331bd2a61d'):
        testmu_appium.click(
            driver,
            selectors=[
                {"selector": "com.lambdatest.proverbial:id/buttonPage", "score": 90, "isXPath": False, "strategy": "view_id"},
                {"selector": "{\"v\":1,\"op\":\"attrs_xpath\",\"target\":{\"resource_id\":\"com.lambdatest.proverbial:id/buttonPage\",\"description\":\"Home\"}}", "score": 51, "isXPath": False, "strategy": "attrs_xpath"},
                {"selector": "Home", "score": 35, "isXPath": False, "strategy": "accessibility_id"},
            ],
            description='PRIMARY: Home navigation button; role=group; text="Home" | HINTS: position=bottom-right; container=bottom navigation bar',
        )

    with testmu_appium.step('Close the Proverbial app', instruction_id='c1bc4b813ccd4ff28b7b315c1827fba4'):
        testmu_appium.app_lifecycle(
            driver,
            "terminate",
            app_id="com.lambdatest.proverbial",
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

