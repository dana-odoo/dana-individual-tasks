{
    "name": "LinkSource Sale",
    "summary": "Prevents the recomputation of unit price on an order line when a change in quantity is made",
    "description": """
LinkSource Sale
===============
This Module is used to allow a change in unit price of an order line to persist after a change in product quantity is made to that order line. This change persists until the 'recompute prices' button is clicked or when either product_id or product_uom are modified.
    """,
    "version": "1.0.0",
    "category": "LinkSource/customizations",
    "license": "OPL-1",
    "depends": ["sale"],
    "data": [
        "views/sale_order_views.xml"],
    "author": "Odoo Inc",
    "website": "linksourcesystems.com",
}
