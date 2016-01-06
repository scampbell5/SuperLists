from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_item(self):

		self.browser.get(self.server_url)

		#Find element and send an empty string.
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		#Looks on page to find an error
		error = self.browser.find_element_by_css_selector('.has-error')

		#Checks the error text to verify that it indicates list cannot be blank
		self.assertEqual(error.text, "You can't have an empty list item")

		#Tries to enter another valid list item
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')

		#Tries to send an empty list item again
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		#Checks that valid item is in list
		self.check_for_row_list_in_table('1. Buy milk')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#Adds another valid list item
		self.browser.find_element_by_id('id_new_item').send_keys('Make tea')

		self.check_for_row_list_in_table('1. Buy milk')
		self.check_for_row_list_in_table('2. Make tea')

		
			




