var words = ["👨‍💻Programmer", "✍️Blogger", "⛰️Hiker", "🥋Martial Artist", "&#x1F393;Student", "&#x1F4DA;Book Lover"];
// So this is the list of words to rotate through
var i = 0;
// This appears to be a counter
var text = "...";
// This is the text it'll start with
function _getChangedText() {
  // so this function replaces all items with "..." with the word[i]
  i = (i + 1) % words.length;
  // universal variable to constantly allow text change
  return text.replace(/.../, words[i]);
}
function _changeText() {
  var txt = _getChangedText();
  // so this gets the changed text
    var d = document.getElementById("changer")
    // gets the element by ID "changer"
    d.className = "fadeOut";
    // uses CSS fadeOut class
    setTimeout(function(){
     d.className = "";
    
    document.getElementById("changer").innerHTML = txt;
}, 1000); // So basically this part actually changes the text
}

var showText = function (target, message, index, interval) {   
  if (index < message.length) {
    $(target).append(message[index++]);
    setTimeout(function () { showText(target, message, index, interval); }, interval);
  }
}

setInterval("_changeText()", 1000);
