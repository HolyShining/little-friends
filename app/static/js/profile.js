// function show_div() {var d = document;
// d.querySelector('.hide_div').addEventListener('click', function(){
//     var div3 = d.createElement('div');
//     div3.className = 'new_pet';
//     div3.innerHTML = '<a href=""><img class="avatar"src="../templates/img/1.jpg"></img></a><p>newpet</p>';
//     d.querySelector('.petlist').appendChild(div3);
// }, false);}

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


// function add_newpet(){
//   var d = document;
//   d.querySelector('.add_pet').addEventListener('mouseover', function(){
//     var p = d.getElementsByClassName('p_hidden');
//     var actualDisplay = window.getComputedStyle(p).display;
//     if (actualDisplay == 'none'){
//       added_item_button.style.display = 'inline';
//     }
//   },false);
// }s
