# Filename: test_preorder_check.py
# Author: Ryan Blushke
# Created: October 27, 2020
# Description: test to check preorder availability
#
# Copyright 2020 Ryan Blushke
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver

class TestPreorderCheck():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path='webdrivers/chromedriver')
    self.vars = {}

  def teardown_method(self, method):
    self.driver.quit()

  def test_availability(self):
    self.driver.get("https://www.bestbuy.ca/en-ca/search?search=RTX+3070+series")
    self.driver.set_window_size(1280, 720)
    available_cards = self.driver.find_elements_by_css_selector("product")
    print(available_cards)
