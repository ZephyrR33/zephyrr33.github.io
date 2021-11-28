function changeColorRed() {
    //document.body.style.background = colorArray[i];
    localStorage.setItem("anumber", "4");
}


function changeColorPink() {
    localStorage.setItem("anumber", "1");



}

function changeColorGreen() {
    //document.body.style.background = colorArray[i];
    localStorage.setItem("anumber", "3");


}

function changeColorBlue() {
    localStorage.setItem("anumber", "2");
}


function changeColor() {
    let r = document.getElementById("r");
    let t = document.getElementById("t");
    let p = document.getElementById("p");
    let inp = document.getElementById("inp");
    let int = document.getElementById("int");
    var a = parseInt(localStorage.getItem("anumber"));
    if (a == 1) {
        //document.body.style.background = colorArray[i];
        document.body.style.background = "url('/FonDark.png') center  no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png




        document.body.style.margin = "0";
        document.body.style.padding = "0";

        document.body.style.backgroundPosition = "top";

        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
        document.body.style.backgroundColor = "#000000";
        r.style.border= "5px solid rgba(255, 255, 255, 1)";
        t.style.border= "5px solid rgba(255, 255, 255, 1)";
        p.style.border= "5px solid rgba(255, 255, 255, 1)";
        int.style.backgroundColor = "rgba(255, 255, 255, 1)";
        inp.style.backgroundColor = "rgba(255, 255, 255, 1)";
    }

    if (a == 2) {
        document.body.style.background = "url('/FonObloko.png') no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png



        document.body.style.margin = "0";
        document.body.style.padding = "0";

        document.body.style.backgroundPosition = "top";

        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
        document.body.style.backgroundColor = "#330000";
        r.style.border= "5px solid rgba(120, 39, 62, 1)";
        t.style.border= "5px solid rgba(120, 39, 62, 1)";
        p.style.border= "5px solid rgba(120, 39, 62, 1)";
        int.style.backgroundColor = "rgba(120, 39, 62, 1)";
        inp.style.backgroundColor = "rgba(120, 39, 62, 1)";
    }

    if (a == 3) {
        document.body.style.background = "url('/FonVan.png') center no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png
        document.body.style.margin = "0";
        document.body.style.padding = "0";

        document.body.style.backgroundPosition = "top";

        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
        document.body.style.backgroundColor = "#003300";
        r.style.border= "5px solid rgba(93, 239, 151, 1)";
        t.style.border= "5px solid rgba(93, 239, 151, 1)";
        p.style.border= "5px solid rgba(93, 239, 151, 1)";
        int.style.backgroundColor = "rgba(93, 239, 151, 1)";
        inp.style.backgroundColor = "rgba(93, 239, 151, 1)";
    }

    if (a == 4) {
        document.body.style.background = "url('/FonSaske.png') center no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png
        document.body.style.margin = "0";
        document.body.style.margin = "0";
        document.body.style.backgroundColor = "rgba(12, 16, 34, 1)";
        document.body.style.padding = "0";
        document.body.style.backgroundPosition = "top";
        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
        r.style.border= "5px solid rgba(93, 95, 239, 1)";
        t.style.border= "5px solid rgba(93, 95, 239, 1)";
        p.style.border= "5px solid rgba(93, 95, 239, 1)";
        int.style.backgroundColor = "rgba(93, 95, 239, 1)";
        inp.style.backgroundColor = "rgba(93, 95, 239, 1)";
    }

}