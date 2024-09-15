document.getElementById("submit").addEventListener("click", myFunction);
document.getElementById("sub").addEventListener("click", myFunction);
function myFunction() {
  window.location.href = "#resultbody1";
}
function showValue() {
  var range = document.getElementById("rangeurl");
  var rangeValue = document.getElementById("rangeValue");
  rangeValue.innerHTML = range.value;
}
function showValue1() {
  var range = document.getElementById("rangetext");
  var rangeValue = document.getElementById("rangeValue1");
  rangeValue.innerHTML = range.value;
}
function showValue2() {
  var range = document.getElementById("rangepdf");
  var rangeValue = document.getElementById("rangeValue2");
  rangeValue.innerHTML = range.value;
}

function countWord() {
  var words = document.getElementById("textforsummer").value;
  var count = 0;
  var split = words.split(" ");
  for (var i = 0; i < split.length; i++) {
    if (split[i] != "") {
      count += 1;
    }
  }
  document.getElementById("show").innerHTML = count;
}
function countWord1() {
  var words = document.getElementById("result1").textContent;
  var count = 0;
  var split = words.split(" ");
  for (var i = 0; i < split.length; i++) {
    if (split[i] != "") {
      count += 1;
    }
  }
  document.getElementById("showres").innerHTML = count;
}
function countWord2() {
  var words = document.getElementById("result2").textContent;
  var count = 0;
  var split = words.split(" ");
  for (var i = 0; i < split.length; i++) {
    if (split[i] != "") {
      count += 1;
    }
  }
  document.getElementById("showres2").innerHTML = count;
}
function countWordsInElement(elementId, countId) {
  var words = document.getElementById(elementId).textContent;
  var count = countWords(words);
  document.getElementById(countId).innerHTML = count;
}

function countWords(text) {
  var count = 0;
  var split = text.split(" ");
  for (var i = 0; i < split.length; i++) {
    if (split[i] != "") {
      count += 1;
    }
  }
  return count;
}

function countWord3() {
  var words = document.getElementById("result3").textContent;
  var count = 0;
  var split = words.split(" ");
  for (var i = 0; i < split.length; i++) {
    if (split[i] != "") {
      count += 1;
    }
  }
  document.getElementById("showres3").innerHTML = count;
}
// function mycopy() {
// var copyText = document.getElementById("result1").innerText;
// copyText.select();
// navigator.clipboard.writeText(copyText.textContent);
// }
function copyElementText() {
  var text = document.getElementById("result1").innerText;
  var elem = document.createElement("textarea");
  document.body.appendChild(elem);
  elem.value = text;
  elem.select();
  document.execCommand("copy");
  document.body.removeChild(elem);
}
function mycopy1() {
  var text = document.getElementById("result2").innerText;
  var elem = document.createElement("textarea");
  document.body.appendChild(elem);
  elem.value = text;
  elem.select();
  document.execCommand("copy");
  document.body.removeChild(elem);
}
function mycopy2() {
  var text = document.getElementById("result3").innerText;
  var elem = document.createElement("textarea");
  document.body.appendChild(elem);
  elem.value = text;
  elem.select();
  document.execCommand("copy");
  document.body.removeChild(elem);
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    /* Toggle between adding and removing the "active" class,
        to highlight the button that controls the panel */
    this.classList.toggle("active");

    /* Toggle between hiding and showing the active panel */
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
    } else {
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}

// drag and drop
// function drag(ev) {
// ev.dataTransfer.setData("src", ev.target.id);
//   }
//
//   function drop(ev) {
// ev.preventDefault();
// var data = ev.dataTransfer.getData("src");
//   }
//   function allowDrop(ev) {
// ev.preventDefault();
//   }
