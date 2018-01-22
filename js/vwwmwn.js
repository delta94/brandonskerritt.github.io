;(function(){
	var twLink = document.createElement('a');
	twLink.setAttribute('href','https://codepen.io/triss90');
	twLink.setAttribute('class', 'tw-link')
	twLink.setAttribute('target','_blank');
	twLink.innerHTML = 'Discover more Pens by Tristan White';
	document.head.insertAdjacentHTML('beforeend','<style>.tw-link {font-family:Verdana, Geneva, sans-serif;position: fixed;bottom: 10px;right: 10px;background: #F71E35;color: #fff;text-decoration: none;padding: 10px 15px;-webkit-transition: all 0.3s ease;transition: all 0.3s ease;box-shadow: 0 0 5px rgba(0, 0, 0, 0.4);}.tw-link:hover {-webkit-transform: translateY(-3px);transform: translateY(-3px);box-shadow: 0 2px 5px rgba(0, 0, 0, 0.4);}</style>'); 
 	document.body.appendChild(twLink);
})();