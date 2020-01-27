let clicks = 0;
function changeH1(){
    let h1 = document.getElementById("h1Title");
    switch(clicks){
        case 0:
        h1.style.fontSize = "100px";
        h1.innerHTML = "KEEP CLICKING ON ME";
        clicks++;
        break;

        case 1:
        h1.style.backgroundColor = "red";
        clicks++;
        break;    

        case 2:
        h1.style.fontFamily = "Arial, Helvetica, sans-serif";
        clicks++;
        break;  
            
        case 3:
        h1.style.fontStyle = "bold";
        clicks++;
        break;
        
        case 4:
        h1.style.fontSize = "50px";
        clicks++;
        break; 

        case 5:
        h1.style.color = "blue";
        clicks++;
        break; 

        case 6:
        document.body.style.backgroundColor = "green";
        clicks++;
        break;
        
        case 7:
        h1.style.textAlign = "right";
        clicks++;
        break; 
    }
}