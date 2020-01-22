var array = ["Banana","Apples","Oranges","Blueberries"];

array.shift();
array.sort();
array.push("Kiwi");
array.splice(1,1);
array.reverse();

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(array2[1][1][0]);

console.log(array);
console.log("-------------------");

var obj = {
    username:"Eran",
    password:"ohhyeah"
};

var database = [obj];

var obj1 = { username:"May",timeline:"15/10/2020"};
var obj2 = { username:"Shiran",timeline:"01/03/2020"};
var obj3 = { username:"Keren",timeline:"29/08/2020"};

var newFeeds = [obj1,obj2,obj3];

console.log(newFeeds);