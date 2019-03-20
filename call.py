from db import Db

from auth import Auth

class Call:
	def __init__(self, first_name, last_name, phone, email,
			 address1, address2, postal_code, city, country,
			 customer_id=None, added_by=None):
		self.first_name = first_name
		self.last_name = last_name
		self.phone = phone
		self.email = email
		self.address1 = address1
		self.address2 = address2
		self.postal_code = postal_code
		self.city = city
		self.country = country
		self.customer_id = customer_id
		self.added_by = added_by

	def save(self):
		'''If self has been populated by database data - UPDATE.
		Otherwise - INSERT a new record.'''
		pass

	def build_from_row(row):
		if row is None:
			return None
		call = Call(row[0], row[1], row[2], row[3], row[4])
		return call

	# Note: this is a CLASS function (no self!)
	def get_for_customer(customer_id, include_user=False):
		'''Return a list of Call objects for the given customer.
		(Bonus: if include_user is True, add a 'user' attribute/property
		to each Call object, containing all the info about the user who
		created the Call object.)'''
		pass

	def get(call_id):
		'''Get a single Call object that corresponds to the call id.
		If none found, return None.'''
		pass

	# Note: this is a CLASS function (no self!)
	def get_all():
		'''Get a list of Call objects - one for each row in the 
		relevant table in the database.'''
		pass
