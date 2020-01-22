const basket = ["apple","orange","grapes"];

//prints all the values in the array
for (i in basket){
    console.log(basket[i]);
}
//output: apple orange grapes


//prints all the values in the array
for(value of basket){
    console.log(value);
}
//output: apple orange grapes


//prints the values and the index of the array
basket.forEach( (value,index) => {
     console.log(value + " " + index);
   }
);
//output: apple 0 | orange 1 | grapes 2

console.log("----------------------------------");

const detailedBasket = {
    apples: 5,
    oranges: 10,
    grapes: 1000
  };

//prints the values of the object
  for (value in detailedBasket) {
     console.log(detailedBasket[value]);
 }
 //output: 5 10 1000


 Object.keys(obj); // prints the keys of the object (apples oranges grapes)
 Object.values(obj); // prints the values of the object (5 10 1000)
 Object.entries(obj); // prints the key and value (apples:5, oranges:10,grapes:1000)

//prints in loop the keys of the Object
Object.keys(detailedBasket).forEach( key  => {
    console.log( key );
  }
);
//output: apples oranges grapes

//prints in loop the values of the Object
Object.values(detailedBasket).forEach( value => {
    console.log(value);
});
//output: 5 10 1000

//prints in loop key and values of the Object
Object.entries(detailedBasket).forEach( ent => {
    console.log('enteries', ent);
  });
//output:apples 5  oranges 10 grapes 1000

  
  