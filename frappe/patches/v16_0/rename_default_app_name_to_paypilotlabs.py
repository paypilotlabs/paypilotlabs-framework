import frappe


def execute():
	# Only replace the stock default; a name the site owner chose stays.
	for doctype in ("Website Settings", "System Settings"):
		if frappe.db.get_single_value(doctype, "app_name") in ("Frappe", "Frappe Framework"):
			frappe.db.set_single_value(doctype, "app_name", "PayPilotLabs")
