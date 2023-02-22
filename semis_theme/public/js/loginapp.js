document.getElementById ('login_email').placeholder='administrator@semis.rsu-sindh.gov.pk';

if (navigator.doNotTrack != 1 && !window.is_404) {
	frappe.ready(() => {
		console.log('AAA');
		/* let browser = frappe.utils.get_browser();
		frappe.call("frappe.website.doctype.web_page_view.web_page_view.make_view_log", {
			path: location.pathname,
			referrer: document.referrer,
			browser: browser.name,
			version: browser.version,
			url: location.origin,
			user_tz: Intl.DateTimeFormat().resolvedOptions().timeZone
		}) */
	})
}