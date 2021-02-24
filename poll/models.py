from django.db import models

# Create your models here.
""" PollResult needs:
		ID: Provided already when migrated to SQL
		choice of stack preference: frontend, backend, and both - Charfield
		Radio selection of how many programming languages you are experienced with: 0, 1-2, 3-4, 5-6, 7+ - Charfield (https://stackoverflow.com/questions/39566606/django-model-fields-radio-button)
		Integer of how long you have been programming for: presumably sanitized to between 0 and 99 - Intfield
		Radio selection of what database you have most experience with: PostgreSQL, MySQL, Oracle, SQL Server  - Charfield
"""


class PollResult(models.Model):
	FRONTEND = 'FE'
	BACKEND = 'BE'
	BOTH = 'BB'

	STACK_CHOICES = (
		(FRONTEND, 'Frontend'),
		(BACKEND, 'Backend'),
		(BOTH, 'Both')
	)

	EXPERIENCE_CHOICES = (
		('0', '0'),
		('1-2', '1-2'),
		('3-4', '3-4'),
		('5-6', '5-6'),
		('7+', '7+'),
	)

	POSTGRESQL = 'PG'
	MYSQL = 'MS'
	ORACLE = 'OR'
	SQL_SERVER = 'SS'

	DATABASE_CHOICES = (
		(POSTGRESQL, 'PostgreSQL'),
		(MYSQL, 'MySQL'),
		(ORACLE, 'Oracle'),
		(SQL_SERVER, 'SQL Server'),
	)

	stack_choice = models.CharField(
		max_length=2,
		choices=STACK_CHOICES
	)

	programming_languages = models.CharField(
		max_length=3,
		choices=EXPERIENCE_CHOICES
	)

	programming_exp = models.IntegerField(
		#validators=[MinValueValidator(0)]
	)

	database_exp = models.CharField(
		max_length=2,
		choices=DATABASE_CHOICES
	)
