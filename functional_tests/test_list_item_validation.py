from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):
	
	def test_cannot_add_empty_list_item(self):

		self.browser.get(self.server_url)

		#Find element and send an empty string.
		self.get_item_input_box().send_keys('\n')

		#Looks on page to find an error
		error = self.browser.find_element_by_css_selector('.has-error')

		#Checks the error text to verify that it indicates list cannot be blank
		self.assertEqual(error.text, "You can't have an empty list item")

		#Tries to enter another valid list item
		self.get_item_input_box().send_keys('Buy milk\n')

		#Tries to send an empty list item again
		self.get_item_input_box().send_keys('\n')

		#Checks that valid item is in list
		self.check_for_row_in_list_table('1: Buy milk')
		self.get_item_input_box().send_keys('\n')
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		#Adds another valid list item
		self.get_item_input_box().send_keys('Make tea\n')

		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')

	def test_cannot_add_duplicate_items(self):
		self.browser.get(self.server_url)

		#User enters the first item
		self.get_item_input_box().send_keys('Buy willies\n')
		self.check_for_row_in_list_table('1: Buy willies')

		#User tries to enter the same item, twice
		self.get_item_input_box().send_keys('Buy willies')

		#Checks for error on the page
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You've already got this in your list")





		
			




