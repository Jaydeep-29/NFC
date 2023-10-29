function getBoolVal(lb_val) {
  if (lb_val == "TRUE") {
    return 1;
  }

  if (lb_val == "FALSE") {
    return 0;
  }
}

function getLevel(ls_val) {
  if (ls_val.length > 0) {
    var ls_data = ls_val.trim();
    return ls_data.substring(6, ls_data.length).trim();
  }
}

function getLevelDropDown(no_of_level){
  var ls_dropdown_val = "";
  for (var i = 0 ;i<=no_of_level;i++){
    if (ls_dropdown_val == ""){
      ls_dropdown_val = "<option val="+i+">Select User Level</option>"
    } else {
      ls_dropdown_val = ls_dropdown_val + "<option val="+i+">Level "+i+"</option>"
    }
  }
  return ls_dropdown_val;
}



$(document).keydown(function (event) {

  //     $("body").on("contextmenu", function(e) {
  //         return false;
  //     // });

  //     // if (event.keyCode == 123) { // Prevent F12
  //     //     return false;
  //     // } else if (event.ctrlKey && event.shiftKey && event.keyCode == 73) { // Prevent Ctrl+Shift+I        
  //     //     return false;
  //     // } else if (event.ctrlKey && event.shiftKey && event.keyCode == 74) { // Prevent Ctrl+Shift+J        
  //     //     return false;    
  //     // }
  //     //  else if (event.ctrlKey && event.keyCode == 85) { // Prevent Ctrl+U        
  //     //     return false;
  //     // }
  
  //cont_usr();

});