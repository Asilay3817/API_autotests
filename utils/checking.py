"""Checking respons methods"""
import json


class CheckAll():

    """Checking status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code, "Status code incorrect"


    """Checking required response fields"""
    @staticmethod
    def check_token(result, response_value):
        token = json.loads(result.text)
        assert list(token) == response_value, "Missing required tokens"
