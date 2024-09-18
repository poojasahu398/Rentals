import frappe
from frappe.model.document import Document
from frappe import _

@frappe.whitelist()
def get_doc():
    try:
        # Check if the document exists
        if not frappe.db.exists('Admission2', 'Aarti'):
            return {"error": _("Document not found")}
        
        # Fetch the document
        doc = frappe.get_doc('Admission2', 'Aarti')
        return doc.as_dict()

    except frappe.PermissionError:
        return {"error": _("You do not have permission to access this document")}
    
    except Exception as e:
        return {"error": str(e)}
