// Copyright (c) 2023, Magnificats and contributors
// For license information, please see license.txt

// frappe.ui.form.on("EMS Code", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('EMS Code',  {
    validate: function(frm) {
        frm.doc.code = frm.doc.breed_code + " " + frm.doc.colour_code + " - " + frm.doc.breed_name + " " + frm.doc.colour_name;
    }
});
