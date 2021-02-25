from django.shortcuts import render

# Create your views here.
from .models import PollResult
"""
	On submit:
		Create a new poll_result object.
		Update its contents with information from the form.
		Save new poll_result object
		
		POLL will receive e.g 'question1': ['FE'], 'question2': ['1-2'], 'question3': ['12'], 'question4': ['OR']}
	
	args: request
	return: render(request, 'polls/results.html')
"""


def submit(request):
	poll_result = PollResult() # Make the object that will be saved to the database
	# Q1
	ans1 = request.POST['question1']
	if is_in_reflist(ans1, PollResult.STACK_CHOICES):
		poll_result.stack_choice = ans1
	else:
		return error_msg()
	# Q2
	ans2 = request.POST['question2']
	if is_in_reflist(ans2, PollResult.EXPERIENCE_CHOICES):
		poll_result.programming_languages = ans2
	else:
		return error_msg()
	# Q3
	ans3 = request.POST['question3']
	if is_sane_int(ans3):
		poll_result.programming_exp = int(ans3)
	else:
		return error_msg()
	# Q4
	ans4 = request.POST['question4']
	if is_in_reflist(ans4, PollResult.DATABASE_CHOICES):
		poll_result.database_exp = ans4
	else:
		return error_msg()
	poll_result.save()

	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
	return HttpResponseRedirect(reverse('results'))


"""
	is_in_reflist:
		Loops through a list of iterable (actual value, human readable name) to find if the given item is equal to the actual value
		args: 
			item: The item received from POST
			reflist: The list of iterable to check
		
		return: bool (True if item is in reflist iterable, False otherwise)
		
"""


def is_in_reflist(item, reflist):
	for index in range(len(reflist)):
		if item in reflist[index]:
			print("item is in reflist")
			return True
	return False


"""
	is_sane_int
		Checks if the given information is indeed an integer
		
		args: int_to_test, the string to check if it is a valid integer.
		
		return: bool (true if it is indeed an integer, false otherwise)
"""


def is_sane_int(int_to_test):
	try:
		tru_int = int(int_to_test)
		return True
	except ValueError:
		return False


"""
	error_msg
		A helper to standardize informing the user of an error

		args: msg: String to tell the user of what went wrong.
		
		return: null
"""


def error_msg(msg):
	return render(request, 'error', {
		'error_message': msg,
	})
