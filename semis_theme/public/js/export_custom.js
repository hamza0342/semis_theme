function downloadtable(div_name, file_name) {
	$(div_name).table2excel({
		exclude: ".noExl",
		name: file_name,
		exclude_img: true,
		exclude_links: true,
		exclude_inputs: true,
		preserveColors: true,
		filename: file_name
	});
}