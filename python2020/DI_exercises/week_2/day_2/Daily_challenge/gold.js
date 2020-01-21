

let getNumber = () =>{
    return prompt("please enter a number");
}


let checkEvenOrOdd = () => {
    let number = getNumber();
    if(number % 2 == 0){
        console.log(number + " is an even number");
    }else{
        console.log(number + " is an odd number");
    }
}

checkEvenOrOdd();

var number1 = 5;
var number2 = 3;

let checkWhichBigger = (num1,num2) =>{
    if(num1 > num2){
        console.log(num1 + " is bigger");
    }else{
        console.log(num2 + " is bigger");
    }
}

checkWhichBigger(number1,number2);


let whcihLanguage = () =>{
    let language = prompt("Please enter your language");
    switch (language){
        case "french":
            console.log("Bonjour");
            break;
        case "english":
            console.log("Hello");
            break;
        case "hebrew":
            console.log("Shalom");
            break;
        default:
            console.log("😊");
    }
}

whcihLanguage();


let gradeChecker = () =>{
    let grade = prompt("Please enter your grade");
    if(grade > 90){
        console.log("A");
    }else if(grade < 90 && grade > 80){
        console.log("B");
    }else if(grade > 70 && grade < 80){
        console.log("C");
    }else if (grade < 70){
        console.log("D");
    }
}

gradeChecker();