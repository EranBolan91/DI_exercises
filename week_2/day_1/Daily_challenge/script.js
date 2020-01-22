let number1;
let number2;
let sign;

function my_f(num){
 
    if(num != "+" && num != "-" && num != "/"){
        if(isNaN(number1)){
            number1 = num;
        }else{
            number2 = num;
        }
    }else{
        switch(num){
            case "+":
            sign = num;
            console.log(sign);
            break;
    
            case "-":
            sign = num;
            break;
            
            case "/":
            sign = num;
            break;
        default:
        
        }
    }

    console.log(number1 + " " + number2);
    console.log(sign);
}

function calc(){
    console.log(sign);
    let ans;
    switch(sign){
        case "+":
        ans = number1 + number2;
        console.log(ans);
        break;
        case "-":
        ans = number1 - number2;
        console.log(ans);  
        break;
        case "/":
        ans = number1/number2;    
        console.log(ans);
        break;
    }
    alert("Your answer is " + ans);
}