function setfont(fontfamily){
    document.getElementById("fontfamily").value = fontfamily;
    if(fontfamily == "default"){
        document.getElementById("article").style.fontFamily=""
    }
    else{
        document.getElementById("article").style.fontFamily=fontfamily
    }
}