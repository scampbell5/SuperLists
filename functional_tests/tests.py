from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	browser = webdriver.Chrome()
		
	def setUp(self):
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()


	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		self.browser.get(self.live_server_url)

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
		self.check_for_row_in_list_table('1: Buy a peacock feathers')


		#Test to see if we can enter a second item
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1: Buy a peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


		# There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
		self.fail('Finish the test!')





