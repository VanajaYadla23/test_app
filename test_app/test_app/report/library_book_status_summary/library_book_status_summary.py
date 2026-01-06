# Copyright (c) 2026, Vanaja and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	data = frappe.db.sql("""select status,COUNT(*) AS total_books FROM `tabLibrary Book`GROUP BY status""",as_dict=True)
	columns = [
		{
		"label":"Status",
		"fieldname":"status",
		"fieldtype":"Select",
		"width":100
		},
		{
		"label":"Total Books",
		"fieldname":"total_books",
		"fieldtype":"Data",
		"width":100
		},
	]
	return columns, data
