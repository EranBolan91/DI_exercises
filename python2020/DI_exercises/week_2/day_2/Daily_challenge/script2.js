// change everything below to the newer Javascript!

// let + const
var a = 'test';
var b = true;
var c = 789;
a = 'test2';


// console log firstName lastName age eyeColor,num,city
var person = {
    firstName : "John",
    lastName  : "Doe",
    age       : 50,
    eyeColor  : "blue",
    id:{
      num:909090,
      add:{
        city:'tel aviv'
      }
    }
};

console.log(person.firstName + " " +
                    person.lastName + " "+
                    person.age + " " +
                    person.id.num + " " +
                    person.id.add.city);

// ada default arguments to the function
// set default age to 10;



function isValidAge(age) {
    return age = 10;
}
alert (isValidAge(14) );


// Chenge to Arrow functions
function whereAmI(username, location) {
    if (username && location) {
        return "I am not lost";
    } else {
        return "I am totally lost!";
    }
}

let whereAmI =(username,location) =>{
    if(username && location){
        return "I am not lost";
    }else{
        return "I am totally lost";
    }
}
