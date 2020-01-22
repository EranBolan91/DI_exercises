// let family = {
//     Lastname:"Bolandian",
//     familyMembers: 5,
//     country:"Israel",
//     religion:"Jewish"
// }

// var keys = Object.keys(family);
// console.log(keys);
// console.log(Object.values(family));

/** ------------------------------- */

// var building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "one": 3,
//         "two": 4,
//         "three": 9,
//         "four": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 2000],
//         "Dan":  [4, 1000],
//         "David": [1, 10],
//     },
// }

//1)
//console.log(Object.values(building.number_of_apt_by_level));

//2)
// let sum = 0;
// sum = building.number_of_apt_by_level.one;
// sum = sum + building.number_of_apt_by_level.three;
// console.log(sum);

//3)

//console.log(building.name_of_tenants[1] + " " + building.number_of_rooms_and_rent.Dan[0]);

//4)

// let saraRent = building.number_of_rooms_and_rent.Sarah[1];
// let davidRent = building.number_of_rooms_and_rent.David[1];
// let danRent = building.number_of_rooms_and_rent.Dan[1];
// let sumRent = saraRent + davidRent;

// if(sumRent > danRent){
//     console.log("You have to inscrease to Dan his monthly rent");
//     building.number_of_rooms_and_rent.Dan[1] = 3000;
// }

// console.log(building);


/*-------------------------------------*/

let myGroceries = ["banana","orange","apple"];
var stock = { 
    "banana": 6, 
    "apple": 0, 
    "orange": 32 
}  

var prices = {    
     "banana": 4, 
    "apple": 2, 
    "orange": 1.5 
} 

let myBill = () =>{
    let sum = stock.banana * prices.banana + stock.orange * prices.orange;
    console.log(sum);
}
myBill();