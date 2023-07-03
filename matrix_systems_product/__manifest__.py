{
    "name": "Matrix Systems Product",
    "summary": "Adds selection field 'Product Group' and modifies barcode on product.template and product.product to be 'FirstTwoDigitsofProductGroup.sequence'",
    "description": """
Matrix Systems Product
======================
This Module creates the selection field 'Product Group' and modifies the barcode field to be formed 
by the concatenation of the first two digits of the products's product group, a period, and the product's six digit sequence
    """,
    "version": "1.0.0",
    "category": "MatrixSystems/customizations",
    "license": "OPL-1",
    "depends": ["product"],
    "data": [
        "views/product_views.xml",
        "data/product_data.xml"
    ],
    "author": "Odoo Inc",
    "website": "www.matrixpci.com",
}