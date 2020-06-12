from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class ResumeTestCase(TestCase):

	def setUp(self):
		self.resp = self.client.get(reverse('my_resume'))

	def test_resume_url(self):
		self.assertEqual(self.resp.status_code, 200)

	def test_resume_page_content(self):
		self.assertContains(self.resp, 'INTERESTS')

	def test_resume_page_sec_edu(self):
		self.assertContains(self.resp, 'EDUCATION')

	def test_resume_page_name(self):
		self.assertContains(self.resp, 'Ravi Kumar D')

	def test_resume_page_email(self):
		self.assertContains(self.resp, 'ivardu19@gmail.com')

	def test_resume_page_img(self):
		self.assertContains(self.resp, 'male_profile_image.jpg')