# imports - standard imports
import unittest

# imports - module imports
import frappe

# imports - frappe module imports
from frappe.chat.doctype.chat_message import chat_message
from frappe.chat.util import create_test_user

session   = frappe.session
test_user = create_test_user(__name__)

class TestChatMessage(unittest.TestCase):
	def test_send(self):
		# TODO - Write the case once you're done with Chat Room
		# user = test_user
		# chat_message.send(user, room, 'foobar')
		pass
