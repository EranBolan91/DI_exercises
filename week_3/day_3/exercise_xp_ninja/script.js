let email = document.getElementById('email');
let btnRes = document.getElementById('check');
let results = document.getElementById('results');

btnRes.addEventListener('click',function(){
    let emailArr = email.value.split("");
    let indexAt = emailArr.indexOf("@");
    
        if(!(emailArr.includes("@"))){
            results.style.color =" red";
            results.innerHTML = "Incorrect mail address";

        }else if(!(emailArr.includes("."))){
            results.style.color =" red";
            results.innerHTML = "Incorrect mail address";

        }else if(emailArr[0] == "@"){
            results.style.color =" red";
            results.innerHTML = "Incorrect mail address";

        }else if (emailArr[emailArr.length -1] == "."){
            results.style.color =" red";
            results.innerHTML = "Incorrect mail address";

        }else if(emailArr[indexAt + 1] == "."){
            results.style.color =" red";
            results.innerHTML = "Incorrect mail address";
            
        }else{
            results.style.color =" green";
            results.innerHTML = "Mail address correct!";
        }
});