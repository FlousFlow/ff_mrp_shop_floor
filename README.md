# Flous Flow Shop Floor

This is a standalone Shop Floor entry point for Odoo 19 Community.

It deliberately reuses the native `mrp.workorder` action, list/kanban/form
views and Play/Stop workflow. Employee session tracking and payroll costing
are provided by the separate `ff_mrp_employee_productivity` addon.

## Scope

This module provides a clean, separately installable Shop Floor menu. It does
not claim to replace Odoo Enterprise's proprietary OWL operator panel; the
Enterprise-only operator experience remains a separate implementation scope.
