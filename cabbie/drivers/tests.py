from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Description, Driver

class DriverModelTests(TestCase):
	def test_unique_email_enforced(self):
		email = 'me@example.com'
		Driver.objects.create(
			first_name="Driver", 
			last_name="1",
			email=email,
			status = Driver.ACTIVE)

		with self.assertRaises(ValidationError):
			Driver.objects.create(
				first_name="Driver", 
				last_name="1",
				email=email,
				status = Driver.ACTIVE)

	def test_inactive_mentor_not_selectable(self):
		mentor = Driver.objects.create(
					first_name="Driver", 
					last_name="1",
					email="mentor@example.com",
					status = Driver.INACTIVE)

		with self.assertRaises(ValidationError):
			Driver.objects.create(
						first_name="Driver", 
						last_name="1",
						email="mentee@example.com",
						status = Driver.ACTIVE,
						mentor=mentor)
