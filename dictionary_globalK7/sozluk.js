function ara (arama) {
	$.getJSON("https://sozluk.gov.tr/gts?ara="+arama,function(data){
		for (var i = data[0]["anlamlarListe"].length - 1; i >= 0; i--) {
			var current = data[0]["anlamlarListe"][i];
			console.log(current);
		};
	})
}
function searchDOM(){
	var inputthing = document.getElementById("search").value;
	$.getJSON("https://sozluk.gov.tr/gts?ara="+inputthing.replace(" ","+"),function(data){
		document.getElementById("results").innerHTML = "";
		for (var i = data[0]["anlamlarListe"].length - 1; i >= 0; i--) {
			var current = data[0]["anlamlarListe"][i];
			document.getElementById("results").innerHTML = document.getElementById("results").innerHTML+"<li>"+data[0]["anlamlarListe"][i].anlam+"</li>";
		};
	})
}