# Copyright 2022 Joan Segui <joan.segui@qubiq.es>
# Copyright 2022 Albert Gonzalez <albert.gonzalez@qubiq.es>
# Copyright 2022 Pol Reig <pol.reig@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Igualia custom developments",
    "summary": "Module to implement Igualia custom developments",
    "version": "13.0.1.0.0",
    "category": "Base",
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "contacts",
        "website",
        "extra_features_gruposgp",
    ],
    "data": [
        "views/res_partner.xml",
    ],
}
