from crawl.repository.crawl_repository import CrawlRepository

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class CrawlRepositoryImpl(CrawlRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://tago.kr/model/index.htm"

    def crawl(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        dataset = []

        for i in range(1, 49):
            if i == 9:
                continue
            try:
                self._navigate_to_car_detail(i)
                car_data = self._extract_car_data()

                dataset.append(car_data)
                self.driver.get(self.base_url)  # 메인 페이지로 돌아가기
                time.sleep(1)

            except Exception as e:
                print(f"Error processing car {i}: {str(e)}")
                continue

        self.driver.quit()
        return dataset

    def _navigate_to_car_detail(self, index):
        xpath = f'//*[@id="container"]/div/div/div[2]/div[{index}]/div/a[1]'
        self.driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
        time.sleep(1)

    def _extract_car_data(self):
        return {
            "url": self._get_car_url(),
            "text": self._get_text('//*[@id="container"]/div/div[3]/h4[1]/span'),
            "drive_range": self._get_text('//*[@id="container"]/div/div[3]/div[2]/div[1]/div'),
            "charge_time": self._get_text('//*[@id="container"]/div/div[3]/div[2]/div[2]/div'),
            "power": self._get_text('//*[@id="container"]/div/div[3]/div[2]/div[3]/div'),
            "전장": self._get_text('//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[1]/td[2]'),
            "전폭": self._get_text('//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[2]/td[2]'),
            "전고": self._get_text('//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[3]/td[2]'),
            "축거": self._get_text('//*[@id="container"]/div/div[3]/div[6]/div[1]/table/tbody/tr[4]/td[2]')
        }

    def _get_car_url(self):
        return self.driver.current_url[22:-4]

    def _get_text(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except Exception as e:
            print(f"Error getting text for xpath {xpath}: {str(e)}")
            return "값 추출 못함"
    