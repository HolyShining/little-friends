function show_addpet() {
  if (document.getElementById("p1_hidden").style.visibility == "visible"){
    document.getElementById("p1_hidden").style.visibility = "hidden";
  }
  else {
    document.getElementById("p1_hidden").style.visibility = "visible";
  };
}

function show_editinf() {
  if (document.getElementById("p2_hidden").style.visibility == "visible") {
    document.getElementById("p2_hidden").style.visibility = "hidden";
  }
  else {
    document.getElementById("p2_hidden").style.visibility = "visible";
  };
}

function show_del() {
  if (document.getElementById("p3_hidden").style.visibility == "visible") {
    document.getElementById("p3_hidden").style.visibility = "hidden";
  }
  else {
    document.getElementById("p3_hidden").style.visibility = "visible";
  };
}
