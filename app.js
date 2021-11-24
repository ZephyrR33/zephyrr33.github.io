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
    }

    if (a == 2) {
        document.body.style.background = "url('/FonObloko.png') no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png



        document.body.style.margin = "0";
        document.body.style.padding = "0";

        document.body.style.backgroundPosition = "top";

        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
        document.body.style.backgroundColor = "#330000";
    }

    if (a == 3) {
        document.body.style.background = "url('/FonVan.png') center no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png
        document.body.style.margin = "0";
        document.body.style.padding = "0";

        document.body.style.backgroundPosition = "top";

        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
        document.body.style.backgroundColor = "#003300";
    }

    if (a == 4) {
        document.body.style.background = "url('/FonSaske.png') center no-repeat"; //Если файл в корне, если путь другой, укажите путь перед t.png
        document.body.style.margin = "0";
        document.body.style.backgroundColor = "#000033";
        document.body.style.padding = "0";
        document.body.style.backgroundPosition = "top";
        document.body.style.backgroundSize = "auto";
        document.body.style.backgroundAttachment = "fixed";
    }

}