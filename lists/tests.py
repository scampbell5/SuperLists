from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
from lists.models import Item, List

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_homepage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	
	def test_url_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

class ListandItemModelsTest(TestCase):

	def test_saving_and_retrieving_an_item(self):

		list_ = List()
		list_.save()

		first_item = Item()
		first_item.text = 'The first (ever) list item'
		first_item.list = list_
		first_item.save()

		second_item = Item()
		second_item.text = 'Item the second'
		second_item.list = list_
		second_item.save()

		saved_items = Item.objects.all()
		self.assertEqual(saved_items.count(), 2)

		saved_list = List.objects.first()
		self.assertEqual(saved_list, list_)

		first_saved_item = saved_items[0]
		second_saved_item = saved_items[1]

		self.assertEqual(first_saved_item.text, 'The first (ever) list item')
		self.assertEqual(first_saved_item.list, saved_list)
		self.assertEqual(second_saved_item.text, 'Item the second')
		self.assertEqual(second_saved_item.list, saved_list)

class ListViewTestCase(TestCase):

	def test_uses_different_template(self):

		response = self.client.get('/lists/the-only-list-in-the-world/')
		self.assertTemplateUsed(response, 'list.html')

	def test_displays_items_for_that_list(self):
		correct_list = List.objects.create()

		Item.objects.create(text='itemey 1', list = correct_list)
		Item.objects.create(text='itemey 2', list = correct_list)

		other_list = List.objects.create()

		Item.objects.create(text='other list item 1', list = other_list)
		Item.objects.create(text='other list item 2', list = other_list)

		response = self.client.get('/lists/%d/', (correct_list,))

		self.assertContains(response, 'itemey 1')
		self.assertContains(response, 'itemey 2')
		self.assertNotContains(response, 'other list item 1')
		self.assertNotContains(response, 'other list item 2')

class NewListTest(TestCase):

	def test_saving_a_POST_request(self):
		self.client.post('/lists/new', data={'item_text' : 'A new list item' })
		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new list item')

	def test_url_can_redirect_after_a_POST_request(self):
		response = self.client.post('/lists/new', data={'item_text' : 'A new list item'})

		self.assertRedirects(response, '/lists/the-only-list-in-the-world/')		






