"""Checking respons methods"""
import json


class CheckAll():

    """Checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, "Status code incorrect"


    """Checking keys required response fields"""
    @staticmethod
    def check_token(result, response_value):
        token = json.loads(result.text)
        assert list(token) == response_value, "Missing required tokens"

    """Checking values required response fields"""
    @staticmethod
    def check_token_values(result, key_name, response_value):
        check = result.json()
        check_info = check.get(key_name)
        assert check_info == response_value, "Value in response not equal expected"

