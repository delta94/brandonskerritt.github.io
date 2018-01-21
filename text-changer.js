var words = ["👨‍💻Programmer", "✍️Blogger", "⛰️Hiker", "🥋Martial Artist", "&#x1F393;Student", "&#x1F4DA;Book Lover"];
var i = 0;
var text = "...";
function _getChangedText() {
  i = (i + 1) % words.length;
  return text.replace(/.../, words[i]);
}
function _changeText() {
  var txt = _getChangedText();
    var d = document.getElementById("changer")
    d.className = "fadeOut";
    setTimeout(function(){
     d.className = "";
    document.getElementById("changer").innerHTML = txt;
}, 1000);
}
setInterval("_changeText()", 1800);