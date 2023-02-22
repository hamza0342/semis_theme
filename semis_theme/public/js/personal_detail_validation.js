function cnic_validate(cnic) {
    var regex_cnic = /^([0-9]{5}[\-][0-9]{7}[\-][0-9]{1})$/;
    if (!(cnic.match(regex_cnic)) || cnic.length != 15) {
        //alert("In-valid Cnic");
        return false;
    } else {
        return true;
    }
}

function onlyalpha(e) {
	var regex = new RegExp("^[a-zA-Z. ]+$");
		var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
		if (regex.test(str)) {
			return true;
		}
		e.preventDefault();
		return false; 
}
// function currency_limit(e) {
// 	var regex = new RegExp("^\d{7}$");
// 		var str = String.fromCharCode(!e.charCode ? e.which : e.charCode);
// 		if (regex.test(str)) {
// 			return true;
// 		}
// 		e.preventDefault();
// 		return false; 
// }
function name_validate(name) {
    var is_text_valid = false;
    if (name.length >= 3) {
        var pattern = /^[a-zA-Z. ]+$/g;
        if(name.match(pattern) != null){
          is_text_valid = true;
        }
    }    
	  return is_text_valid; 
}

function email_validate(email) {
	var pattern = /^([a-zA-A0-9_.-])+@([a-zA-Z0-9_.-])+([a-zA-Z])+/;
	  var is_email_valid = false;
	  if(email.match(pattern) != null){
		is_email_valid = true;
	  }
	  return is_email_valid;
	  
    /* var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!(email.match(mailformat))) {
        //alert("In-valid email address!");
        return false;
    } else {
        return true;
    } */

}

function phone_validate(phone) {
    var regex_phone = /^(03[0-9]{2}[\-][0-9]{7})$/;
    console.log(phone);
    if (!(phone.match(regex_phone)) || phone.length != 12) {
        //alert("In-valid Phone Number");
        return false;
    } else {
        return true;
    }
}

function currency_format(value) {
    var currency_format = /^([0-9]{3}[\,][0-9]{3})$/;
    if (!(value.match(currency_format)) || value.length != 12) {
        return false;
    } else {
        return true;
    }
}
function account_no(account) {
    var accouunt_format = /^([0-9])+$/;
    if (!(account.match(accouunt_format)) || account.length > 20) {
        return false;
    } else {
        return true;
    }
}
function gr_no_format(account){
    const regex =/[\d]{1}/g;
    const doesItHaveNumber = regex.test(account);
    // if (!doesItHaveNumber) {
    //     console.log("Not Have Number");
    //     return false
    // }
    // else{
        console.log("Have Number",doesItHaveNumber);
        var gr_no_format =  /^([a-zA-Z0-9-_]{1,10})$/;
        if ((!doesItHaveNumber) || account.length > 10) {
            return false;
        } else{
            return true;
        }       
    // }
}
function all_validate(email, phone, name, cnic) {

    // if (name_validate(name) && email_validate(email) && phone_validate(phone) && cnic_validate(cnic)) {
    //     return true;
    // }
    // else return false;
}
