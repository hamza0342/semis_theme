let sidebar_categories=[
			"Modules",
			"Domains",
			"Places",
			"Administration"
		];
let workspaces= new Array();
let workspaceitems= new Array();
let index=0;
$(document).ready(function(){
		$("#body").before('<nav class="navbar navbar-expand-lg headermenu"><div class="container sidebar"> <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="navbarSupportedContent"><ul class="navbar-nav desksidebar"></ul></div></div></nav>');
		
		
		console.log('app.js',frappe.boot.allowed_workspaces);
		
		workspaces = new Array();
		 
		for (let page of frappe.boot.allowed_workspaces) { 
			workspaces.push(page);
		}   
		
		make_menu_sidebar();
		  
});		
async function make_menu_sidebar() {  
	var sidebar_section='';
	index=0;
	workspaces.forEach(async (category) => {  
			frappe.call({
				method: "frappe.desk.desktop.get_desktop_page", 
				args: {
					page: JSON.stringify(category) 
				  },	
				callback: function (r) { 
					workspaces[index]['shortcuts']=r.message.shortcuts;  
					let $item = get_sidebar_item_menu(workspaces[index]);
					$item.appendTo('.sidebar .desksidebar',); 
					index++;
				}
			}); 
	});  
} 
  
function get_sidebar_item_menu(item){
			let keys = Object.keys(item); 
			if (item.shortcuts.items.length > 0){
				var shortcuts='';
				 item.shortcuts.items.forEach(function(items) { 
						let route = frappe.utils.generate_route({ 
							name: items.link_to,
							type: items.type, 
							doc_view: items.doc_view
						});
 
						
					 shortcuts +=`<li><a class="dropdown-item" href="${route}">${items.label || items.name}</a></li>`;
				 })
				
				return $(`
					 <li class="nav-item  dropdown"><a
						href="/app/${frappe.router.slug(item.name)}"
						class="nav-link dropdown-toggle desk-sidebar-item standard-sidebar-item ${item.selected ? "selected" : ""}"
					>
						<span>${frappe.utils.icon(item.icon || "folder-normal", "md")}</span>
						<span class="sidebar-item-label">${item.label || item.name}<span>
					</a>
					<ul class="dropdown-menu" aria-labelledby="navbarDropdown">
					${shortcuts}
					<ul></li> 	
				`);
			}else{ 
				return $(`
					<li class="nav-item  dropdown"><a
						href="/app/${frappe.router.slug(item.name)}"
						class="nav-link desk-sidebar-item standard-sidebar-item ${item.selected ? "selected" : ""}"
					>
						<span>${frappe.utils.icon(item.icon || "folder-normal", "md")}</span>
						<span class="sidebar-item-label">${item.label || item.name}<span>
					</a></li>
				`);
			}  
	
}