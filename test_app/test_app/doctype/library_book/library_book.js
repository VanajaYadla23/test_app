// Copyright (c) 2026, Vanaja and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Book", {
    refresh(frm){
        frm.add_custom_button("Book",function(){
            // frappe.msgprint("heyyy hiiii")
            frappe.call({
                method: "test_app.api.get_user_name",
                args:{user: frappe.session.user},
                callback:function(r){
                    if(r.message){
                        // frappe.msgprint(`heyyy hiiii ${r.message}`)
                        frappe.msgprint({
                            title:("Error"),
                            message:`heyyy hiiii ${r.message}`,
                            indicator: "red"
                        })
                    }
                }
            })
        })
        status_change(frm);
    },
    status(frm){
        status_change(frm);
    },
    // validate(frm){
    //     if(frm.doc.status && frm.doc.status=="Issued" && !frm.doc.published_date){
    //         frappe.throw("Published Date is mandatory when the book is issued")
    //     }
    // }
});

function status_change(frm){
    if(frm.doc.status=="Issued"){
        frm.set_df_property("price","read_only",true)
        frappe.msgprint("This book is currently issued")
    // }else if(frm.doc.status=="Lost"){
    //     frm.set_value("price",0)
    //     frm.set_df_property("price","read_only",false)
    }else{
        frm.set_df_property("price","read_only",false)
    }
}