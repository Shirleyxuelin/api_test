"""执行所有用例入口文件"""
import unittest

from config import config as cf
from lib.HTMLTestRunner_PY3 import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(cf.testcase_path)
with open(cf.report_file,'wb') as f:
    HTMLTestRunner(stream=f,
                   title="api test",
                   description="test").run(suite)