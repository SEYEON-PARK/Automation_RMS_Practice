'''
이 코드는 결과 보고서를 작성하고자 시도 중인 코드입니다.
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import HtmlTestRunner
from urllib.parse import quote  # URL 인코딩을 위한 모듈
import html  # HTML 이스케이프 처리를 위한 모듈

class SeleniumTestReport(unittest.TestCase):
    screenshots = []  # 스크린샷 경로를 저장할 클래스 변수
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://example.com")  # 테스트할 URL로 변경
        
    def take_screenshot(self, test_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        # UTF-8 인코딩으로 파일 이름 생성
        screenshot_name = f"{test_name}_{timestamp}.png".encode('utf-8').decode('utf-8')
        screenshot_path = os.path.abspath(os.path.join("screenshots", screenshot_name))
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")
        return screenshot_path

    def test_example_success(self):
        try:
            element = self.driver.find_element(By.XPATH, "//h1")
            self.assertTrue(element.is_displayed())
            print("테스트 성공")
        except Exception as e:
            screenshot_path = self.take_screenshot("test_example_success")
            self._add_screenshot_to_report(screenshot_path)
            raise

    def test_example_failure(self):
        try:
            element = self.driver.find_element(By.XPATH, "//non_existing_element")
            self.assertTrue(element.is_displayed())
        except Exception as e:
            screenshot_path = self.take_screenshot("test_example_failure")
            self._add_screenshot_to_report(screenshot_path)
            raise

    def _add_screenshot_to_report(self, screenshot_path):
        # 백슬래시를 슬래시로 변환
        screenshot_path = screenshot_path.replace("\\", "/")
        # URL 인코딩 적용
        encoded_path = quote(screenshot_path)
        # HTML 이스케이프 처리
        screenshot_html = f"<div><strong>Screenshot:</strong><br><img src='file:///{encoded_path}' width='400'></div>"
        print(html.escape(screenshot_html))  # HTML 이스케이프 처리

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="report",
            report_name="Selenium_Test_Report",
            combine_reports=True
        )
    )




'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import HtmlTestRunner

class SeleniumTestReport(unittest.TestCase):
    screenshots = []  # 스크린샷 경로를 저장할 클래스 변수
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://example.com")  # 테스트할 URL로 변경
        
    def take_screenshot(self, test_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.abspath(os.path.join("screenshots", screenshot_name))
        # SeleniumTestReport.screenshots.append(screenshot_path)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")
        return screenshot_path

    def test_example_success(self):
        try:
            element = self.driver.find_element(By.XPATH, "//h1")
            self.assertTrue(element.is_displayed())
            print("테스트 성공")
        except Exception as e:
            screenshot_path = self.take_screenshot("test_example_success")
            self._add_screenshot_to_report(screenshot_path)
            raise

    def test_example_failure(self):
        try:
            element = self.driver.find_element(By.XPATH, "//non_existing_element")
            self.assertTrue(element.is_displayed())
        except Exception as e:
            screenshot_path = self.take_screenshot("test_example_failure")
            self._add_screenshot_to_report(screenshot_path)
            raise

    def _add_screenshot_to_report(self, screenshot_path):
        # HTML로 스크린샷을 절대 경로로 보고서에 포함
        screenshot_html = f"<div><strong>Screenshot:</strong><br><img src='file:////{screenshot_path}' width='400'></div>"
        print(screenshot_html)

    @classmethod
    def tearDownClass(cls):
        # print(SeleniumTestReport.screenshots)
        cls.driver.quit()

if __name__ == "__main__":
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="report",
            report_name="Selenium_Test_Report",
            combine_reports=True
        )
    )
'''


"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner  # HTMLTestRunner 모듈

class SeleniumTestReport(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://example.com")  # 테스트할 URL로 변경

    def test_example_success(self):
        try:
            element = self.driver.find_element(By.XPATH, "//h1")
            self.assertTrue(element.is_displayed())
            print("테스트 성공")
        except Exception as e:
            print(f"테스트 실패: {e}")
            self.driver.save_screenshot("test_example_success_failed.png")
            raise

    def test_example_failure(self):
        try:
            element = self.driver.find_element(By.XPATH, "//non_existing_element")
            self.assertTrue(element.is_displayed())
        except Exception as e:
            print(f"테스트 실패: {e}")
            self.driver.save_screenshot("test_example_failure_failed.png")
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="report",  # HTML 보고서 파일이 생성될 폴더
            report_name="Selenium_Test_Report",
            combine_reports=True
        )
    )
"""

'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class TestWithScreenshots(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://naver.com")  # 테스트할 URL로 변경

    def take_screenshot(self, test_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")

    def test_example_success(self):
        try:
            element = self.driver.find_element(By.XPATH, "//h1")
            self.assertTrue(element.is_displayed())
        except Exception as e:
            self.take_screenshot("test_example_success")
            raise

    def test_example_failure(self):
        try:
            element = self.driver.find_element(By.XPATH, "//non_existing_element")
            self.assertTrue(element.is_displayed())
        except Exception as e:
            self.take_screenshot("test_example_failure")
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    unittest.main()
'''