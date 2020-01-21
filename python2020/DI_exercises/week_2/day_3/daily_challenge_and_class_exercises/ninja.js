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

var building = {
    number_levels : 4,
    number_of_apt_by_level : {
        "1": 3,
        "2": 4,
        "3": 9,
        "4": 2,
    },
    name_of_tenants : ["Sarah", "Dan", "David"],
    number_of_rooms_and_rent:  {
        "Sarah": [3, 2000],
        "Dan":  [4, 1000],
        "David": [1, 10],
    },
}

//1)
console.log(Object.values(building.number_of_apt_by_level));

//2)
let sum = 0;
sum = building.number_of_apt_by_level.1;
console.log(sum);
sum = sum + building.number_of_apt_by_level.2;
console.log(sum);

