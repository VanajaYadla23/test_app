import frappe

@frappe.whitelist()
def get_user_name(user):
    user_name = frappe.db.get_value("User",user,"full_name")
    return user_name