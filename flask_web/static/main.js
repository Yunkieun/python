let pic = document.getElementById('pic')
pic.onmouseover = changePic;
pic.onmouseout = originPic;

function changePic(){
     pic.src = "../static/cup-5.jpg";
}

        function originPic(){
            pic.src = "../static/cup-4.jpg";
        }