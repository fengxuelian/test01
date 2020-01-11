import pytest
import requests

def test_login_01():
    url="http://sip14xse559fpdnhmzr.dev.syzkcf.com/login"
    parm={
        "username": "lihe",
        "password":"12345678"
    }
    r=requests.post(url,json=parm)
    print(r.text)