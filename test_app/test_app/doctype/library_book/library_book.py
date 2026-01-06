# Copyright (c) 2026, Vanaja and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now
from frappe.model.document import Document


class LibraryBook(Document):
	# def validate(self):
	# 	if self.price is not None and self.price<=0:
	# 		frappe.throw("Price must be greater than 0")
	# 	if frappe.db.exists("Library Book",{"isbn":self.isbn,"name":["!=",self.name]}):
	# 		frappe.throw("ISBN must be unique")
	def before_save(self):
		if self.status=="Issued":
			if self.published_date is None:
				frappe.throw("Published Date is mandatory when the book is issued")
		elif self.status=="Lost":
			self.price=0
		doc = self.get_doc_before_save()
		if doc and doc.status and doc.status!=self.status:
			new_doc = frappe.new_doc("Library Status Log")
			new_doc.library_book = self.name
			new_doc.old_status = doc.status
			new_doc.new_status = self.status
			new_doc.changed_on = now()
			new_doc.changed_by = frappe.session.user
			new_doc.insert()