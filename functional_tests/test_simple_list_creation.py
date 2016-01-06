from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

class NewVisitorTest(FunctionalTest):

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])	

	def test_can_start_a_list_and_retrieve_it_later(self):

		self.browser.get(self.server_url)

		#The page title and header both mentions 'To-Do lists'
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#Needs to enter a to-do list item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		#Test to see if we can enter a new item
		inputbox.send_keys('Buy a peacock feathers')
		inputbox.send_keys(Keys.ENTER)
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, 'lists/.+')

		self.check_for_row_in_list_table('1: Buy a peacock feathers')


		#Test to see if we can enter a second item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy a peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		self.browser.quit()

		## New user comes along and opens a new browser
		## Tests to make sure previous user's list is not there
		self.browser = webdriver.Chrome()
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn("Buy peacock feathers", page_text)
		self.assertNotIn("make a fly", page_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys("Buy milk")
		inputbox.send_keys(Keys.ENTER)

		self.assertRegex(edith_list_url, 'lists/.+')
		francis_list_url = self.browser.current_url
		self.assertNotEqual(francis_list_url, edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text

		self.assertNotIn("Buy peacock feathers", page_text)
		self.assertIn("Buy milk", page_text)

		
			




