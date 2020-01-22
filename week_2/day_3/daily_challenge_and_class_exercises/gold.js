let arrGrades = [];
let arrCoefficient = [];

let getGrade = () =>{
    arrGrades.push(prompt("Please enter your grade"));
    return arrGrades;
}

let getCoefficient = () =>{
    arrCoefficient.push(prompt("Please enter your Coefficient"));
    return arrCoefficient;
}

let avg = () =>{
    let grade = [];
    let coefficient = [];
     grade = getGrade();
     coefficient = getCoefficient();
    console.log(grade + " " + coefficient);

    if(grade.length == 0){
        getGrade();
    }else if(coefficient.length == 0){
        getCoefficient();
    }else {
        console.log(grade/coefficient)/grade.length;
    }
}

avg();