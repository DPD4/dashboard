# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _

def after_install():
    """تشغيل بعد تثبيت التطبيق"""
    try:
        create_workspaces()
        create_advanced_analytics_workspace()
        setup_permissions()
        frappe.db.commit()
        print("✅ تم تثبيت Financial Dashboard بنجاح!")
    except Exception as e:
        frappe.log_error(f"خطأ في تثبيت Financial Dashboard: {str(e)}")
        print(f"❌ خطأ في التثبيت: {str(e)}")

def create_workspaces():
    """إنشاء الـ workspaces"""
    workspaces = [
        {
            "name": "Financial Overview",
            "title": "نظرة عامة مالية",
            "icon": "accounting",
            "category": "Modules",
            "public": 1,
            "module": "Financial Dashboard Final",
            "links": [
                {
                    "label": "لوحة التحكم المالية",
                    "type": "Link",
                    "link_type": "Page",
                    "link_to": "financial-overview-dashboard",
                    "onboard": 0,
                    "hidden": 0
                }
            ],
            "shortcuts": [
                {
                    "label": "فاتورة مبيعات",
                    "type": "DocType",
                    "link_to": "Sales Invoice",
                    "color": "Red",
                    "stats_filter": '{"docstatus": 1}',
                    "format": "{} فاتورة"
                },
                {
                    "label": "قيد يومية",
                    "type": "DocType", 
                    "link_to": "Journal Entry",
                    "color": "Blue",
                    "stats_filter": '{"docstatus": 1}',
                    "format": "{} قيد"
                }
            ],
            "number_cards": [
                {
                    "label": "الرصيد الحالي",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_current_balance",
                    "color": "#FF4444",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "المبيعات",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_monthly_sales",
                    "color": "#44FF44",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "الحسابات المدينة",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_accounts_receivable",
                    "color": "#4444FF",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "صافي الربح",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_net_profit",
                    "color": "#FF8800",
                    "stats_time_interval": "Daily"
                }
            ]
        },
        {
            "name": "Sales Analytics",
            "title": "تحليلات المبيعات",
            "icon": "selling",
            "category": "Modules",
            "public": 1,
            "module": "Financial Dashboard Final",
            "links": [
                {
                    "label": "لوحة تحليلات المبيعات",
                    "type": "Link",
                    "link_type": "Page",
                    "link_to": "sales-analytics-dashboard",
                    "onboard": 0,
                    "hidden": 0
                }
            ],
            "shortcuts": [
                {
                    "label": "العملاء",
                    "type": "DocType",
                    "link_to": "Customer",
                    "color": "Green",
                    "stats_filter": '{}',
                    "format": "{} عميل"
                },
                {
                    "label": "الأصناف",
                    "type": "DocType",
                    "link_to": "Item",
                    "color": "Orange",
                    "stats_filter": '{}',
                    "format": "{} صنف"
                }
            ],
            "number_cards": [
                {
                    "label": "إجمالي المبيعات",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_total_sales",
                    "color": "#FF4444",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "عدد الفواتير",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_invoice_count",
                    "color": "#44FF44",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "متوسط قيمة الفاتورة",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_avg_invoice_value",
                    "color": "#4444FF",
                    "stats_time_interval": "Daily"
                }
            ]
        },
        {
            "name": "Inventory Management",
            "title": "إدارة المخزون",
            "icon": "stock",
            "category": "Modules",
            "public": 1,
            "module": "Financial Dashboard Final",
            "links": [
                {
                    "label": "لوحة إدارة المخزون",
                    "type": "Link",
                    "link_type": "Page",
                    "link_to": "inventory-management-dashboard",
                    "onboard": 0,
                    "hidden": 0
                }
            ],
            "shortcuts": [
                {
                    "label": "المستودعات",
                    "type": "DocType",
                    "link_to": "Warehouse",
                    "color": "Purple",
                    "stats_filter": '{}',
                    "format": "{} مستودع"
                },
                {
                    "label": "حركات المخزون",
                    "type": "DocType",
                    "link_to": "Stock Entry",
                    "color": "Teal",
                    "stats_filter": '{"docstatus": 1}',
                    "format": "{} حركة"
                }
            ],
            "number_cards": [
                {
                    "label": "قيمة المخزون",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_inventory_value",
                    "color": "#FF4444",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "عدد الأصناف",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_items_count",
                    "color": "#44FF44",
                    "stats_time_interval": "Daily"
                },
                {
                    "label": "أصناف منخفضة المخزون",
                    "method": "financial_dashboard_final.financial_dashboard_final.api.get_low_stock_items",
                    "color": "#4444FF",
                    "stats_time_interval": "Daily"
                }
            ]
        }
    ]
    
    for workspace_data in workspaces:
        if not frappe.db.exists("Workspace", workspace_data["name"]):
            workspace = frappe.new_doc("Workspace")
            workspace.update(workspace_data)
            workspace.insert(ignore_permissions=True)
            print(f"✅ تم إنشاء workspace: {workspace_data['title']}")

def setup_permissions():
    """إعداد الصلاحيات"""
    try:
        # إعطاء صلاحيات للأدوار المختلفة
        roles = ["System Manager", "Accounts Manager", "Accounts User"]
        
        for role in roles:
            if frappe.db.exists("Role", role):
                # إعطاء صلاحية الوصول للـ workspaces
                for workspace in ["Financial Overview", "Sales Analytics", "Inventory Management"]:
                    if not frappe.db.exists("Has Role", {"parent": workspace, "role": role}):
                        workspace_doc = frappe.get_doc("Workspace", workspace)
                        workspace_doc.append("roles", {"role": role})
                        workspace_doc.save(ignore_permissions=True)
        
        print("✅ تم إعداد الصلاحيات بنجاح")
    except Exception as e:
        print(f"⚠️ تحذير في إعداد الصلاحيات: {str(e)}")

def create_custom_fields():
    """إنشاء حقول مخصصة إذا لزم الأمر"""
    pass

def create_advanced_analytics_workspace():
    """إنشاء workspace التحليلات المتقدمة"""
    workspace_data = {
        "name": "Advanced Analytics",
        "title": "التحليلات المتقدمة",
        "icon": "reports",
        "category": "Modules",
        "public": 1,
        "module": "Financial Dashboard Final",
        "links": [
            {
                "label": "لوحة التحليلات المتقدمة",
                "type": "Link",
                "link_type": "Page",
                "link_to": "advanced-analytics-dashboard",
                "onboard": 0,
                "hidden": 0
            }
        ],
        "shortcuts": [
            {
                "label": "التقارير المالية",
                "type": "DocType",
                "link_to": "Account",
                "color": "Orange",
                "stats_filter": '{}',
                "format": "{} تقرير"
            },
            {
                "label": "تحليل الربحية",
                "type": "DocType",
                "link_to": "Cost Center",
                "color": "Purple",
                "stats_filter": '{}',
                "format": "{} تحليل"
            }
        ],
        "number_cards": [
            {
                "label": "إجمالي الإيرادات",
                "method": "financial_dashboard_final.financial_dashboard_final.api.get_total_revenue",
                "color": "#FD7E14",
                "stats_time_interval": "Daily"
            },
            {
                "label": "معدل النمو",
                "method": "financial_dashboard_final.financial_dashboard_final.api.get_growth_rate",
                "color": "#28A745",
                "stats_time_interval": "Daily"
            },
            {
                "label": "كفاءة العمليات",
                "method": "financial_dashboard_final.financial_dashboard_final.api.get_operational_efficiency",
                "color": "#DC3545",
                "stats_time_interval": "Daily"
            }
        ]
    }
    
    if not frappe.db.exists("Workspace", workspace_data["name"]):
        workspace = frappe.new_doc("Workspace")
        workspace.update(workspace_data)
        workspace.insert(ignore_permissions=True)
        print(f"✅ تم إنشاء workspace: {workspace_data['title']}")