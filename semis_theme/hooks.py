from . import __version__ as app_version

app_name = "semis_theme"
app_title = "SEMIS Theme"
app_publisher = "Micromerger"
app_description = "SEMIS Theme for Frappe"
app_email = "m.haroon@pk.micromerger.com"
app_license = "MIT"

# Includes in <head>
# ------------------

app_include_css = ["/assets/semis_theme/css/xpert_theme.css",
                    "https://unpkg.com/leaflet@1.8.0/dist/leaflet.css",
                    "/assets/semis_theme/css/MarkerCluster.css",
                    "/assets/semis_theme/css/MarkerCluster.Default.css",
                    "/assets/semis_theme/css/xperterp.css",
                    "/assets/semis_theme/css/morris.css",
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"] 
                    
                    
app_include_js = ["https://unpkg.com/leaflet@1.8.0/dist/leaflet.js",
                   "https://cdnjs.cloudflare.com/ajax/libs/proj4js/2.3.6/proj4.js",
                   "https://code.highcharts.com/maps/highmaps.js",
                   "https://code.highcharts.com/stock/modules/data.js",
                   "https://code.highcharts.com/modules/marker-clusters.js",
                   "https://code.highcharts.com/modules/coloraxis.js",
                   "https://code.highcharts.com/modules/exporting.js",
                   "https://code.highcharts.com/modules/offline-exporting.js",
                   "https://code.highcharts.com/modules/export-data.js",
                   "/assets/semis_theme/js/leaflet.markercluster-src.js",
                   "/assets/semis_theme/js/webdata/webdatarocks.js",
                   "/assets/semis_theme/js/jquery.peity.js",
                   "/assets/semis_theme/js/jquery.table2excel.js",
                   "/assets/semis_theme/js/jquery.mask.js",
                   "/assets/semis_theme/js/raphael-min.js",
                   "/assets/semis_theme/js/morris.min.js",
                   "/assets/semis_theme/js/app.js" 
                #    "/assets/semis_theme/js/libs.min.js",
                #    "/assets/semis_theme/js/desk.min.js",
                #    "/assets/semis_theme/js/list.min.js",
                #    "/assets/semis_theme/js/form.min.js",
                #    "/assets/semis_theme/js/control.min.js",
                #    "/assets/semis_theme/js/report.min.js",
                   ] 
web_include_css = ["/assets/semis_theme/css/semis_theme.css"] 
web_include_js = ["/assets/semis_theme/js/loginapp.js"] 

# include js, css files in header of desk.html
# app_include_css = "/assets/semis_theme/css/semis_theme.css"
# app_include_js = "/assets/semis_theme/js/semis_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/semis_theme/css/semis_theme.css"
# web_include_js = "/assets/semis_theme/js/semis_theme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "semis_theme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "semis_theme.utils.jinja_methods",
#	"filters": "semis_theme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "semis_theme.install.before_install"
# after_install = "semis_theme.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "semis_theme.uninstall.before_uninstall"
# after_uninstall = "semis_theme.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "semis_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"semis_theme.tasks.all"
#	],
#	"daily": [
#		"semis_theme.tasks.daily"
#	],
#	"hourly": [
#		"semis_theme.tasks.hourly"
#	],
#	"weekly": [
#		"semis_theme.tasks.weekly"
#	],
#	"monthly": [
#		"semis_theme.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "semis_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "semis_theme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "semis_theme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"semis_theme.auth.validate"
# ]
