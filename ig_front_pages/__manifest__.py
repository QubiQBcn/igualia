# Copyright 2022 Joan Segui <joan.segui@qubiq.es>
# Copyright 2022 Albert Gonzalez <albert.gonzalez@qubiq.es>
# Copyright 2022 Pol Reig <pol.reig@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Custom pages reports",
    "summary": "Module to implement costom pages reports",
    "version": "13.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "sale",
        "sale_management",
    ],
    "data": [
        "views/sale_order_template_views.xml",
        "reports/ig_front_pages.xml",
    ],
}
