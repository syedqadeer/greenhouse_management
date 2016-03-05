# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "greenhouse"
app_title = "Greenhouse"
app_publisher = "Brandon Fox, Foxtrot"
app_description = "Custom app for managing the data entry, tracking and reporting for the Foxtrot Greenhouse. Will track greenhouse variables, water testing and nutrient/additive tracking."
app_icon = "mega-octicon octicon-bug"
app_color = "green"
app_email = "bfox@foxtrot.email"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/greenhouse/css/greenhouse.css"
# app_include_js = "/assets/greenhouse/js/greenhouse.js"

# include js, css files in header of web template
# web_include_css = "/assets/greenhouse/css/greenhouse.css"
# web_include_js = "/assets/greenhouse/js/greenhouse.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "greenhouse.install.before_install"
# after_install = "greenhouse.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "greenhouse.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"greenhouse.tasks.all"
# 	],
# 	"daily": [
# 		"greenhouse.tasks.daily"
# 	],
# 	"hourly": [
# 		"greenhouse.tasks.hourly"
# 	],
# 	"weekly": [
# 		"greenhouse.tasks.weekly"
# 	]
# 	"monthly": [
# 		"greenhouse.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "greenhouse.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "greenhouse.event.get_events"
# }

