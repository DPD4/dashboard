# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "financial_dashboard_final"
app_title = "Financial Dashboard"
app_publisher = "Your Company"
app_description = "Arabic Financial Dashboard for ERPNext"
app_icon = "octicon octicon-dashboard"
app_color = "red"
app_email = "admin@yourcompany.com"
app_license = "MIT"
app_version = app_version

# Website Route Rules
website_route_rules = [
    {"from_route": "/dashboard", "to_route": "financial-dashboard"},
    {"from_route": "/financial-overview", "to_route": "financial-overview-dashboard"},
    {"from_route": "/sales-analytics", "to_route": "sales-analytics-dashboard"},
    {"from_route": "/inventory-management", "to_route": "inventory-management-dashboard"},
    {"from_route": "/advanced-analytics", "to_route": "advanced-analytics-dashboard"},
]

# Workspaces
fixtures = [
    {
        "doctype": "Workspace",
        "filters": [
            ["name", "in", ["Financial Overview", "Sales Analytics", "Inventory Management", "Advanced Analytics"]]
        ]
    }
]

# Installation
after_install = "financial_dashboard_final.install.after_install"