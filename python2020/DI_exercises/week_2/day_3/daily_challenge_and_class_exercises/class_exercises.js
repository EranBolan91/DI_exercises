 let arr = [];
 for (let i = 0;i <=15; i++){
     arr[i] = i;
 }

 console.log(arr);

 let checkEvenOrOdd = (arr) =>{
     for(let i = 0;arr.length ; i++){
         if(arr[i] % 2 == 0){
             console.log(arr[i] + " is Even");
         }else{
             console.log(arr[i] + " is Odd");
         }
     }
 }
/** ------------------------------------------------ */

 let fizzBuzz = () =>{
     for(let i = 0;i <= 100;i++){
         if(i % 3 == 0){
             console.log("Fizz");
         }else if(i % 5 == 0){
             console.log("Buzz");
         }else if((i % 3) && (i % 5)){
             console.log("FizzBuzz");
         }else{
             console.log(i);
         }
     }
 }

 fizzBuzz();

 /** ------------------------------------------------ */
 var student = [['david',80],['Vinoth',77],['Divya',88],['Ishitha',95],['Thomas',68]];

 let avg = (students) =>{
     let avg,sum= 0;
     for(let i = 0;i < students.length;i++ ){
         sum = sum + students[i][1];
     }
     avg = sum/students.length;
     console.log(sum);
     switch(avg){
         case (100>avg && avg >=90):
             console.log("A");
             break;
         case (90>avg && avg >=80):
             console.log("B");
             break;
         case (80>avg && avg >=70):
             console.log("C");
             break;
         case (70>avg && ag >=60):
             console.log("D");
             break;
         case (60>avg):
             console.log("F");
             break;
             default:
                 console.log(avg);
     }
    
 }

 avg(student);

 /** ------------------------------------------------ */

 let drawingStars = () =>{
     for(let i = 0; i < 5 ;i++){
         console.log("\n");
         for(let j = 0;j < i+1;j++){
             console.log(" * ");
         }
     }
 }

 drawingStars();

 /** ------------------------------------------------ */

const array = [
    {
      username: "john!?",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky!",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy!",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    }
  ];

  let username = [];
   let username_question = [];
  
   let method = (array_username,array_question,array) =>{
     array.forEach(user =>{
         if(user.username.includes('!')){
             array_username.push(user);
         }
       });
       console.log(array_username);

       for(let i = 0;i < array.length;i++){
         if(array[i].username.includes('?')){
            array_question.push(array[i]);
        }   
      }
       console.log(array_question);
   } 


   let filter = (arr) =>{
       let filteredArray = [];
     for(i = 0;i < arr.length;i++){
         if(arr[i].team =="red"){
             filteredArray.push(arr[i]);
         }
     }
     return filteredArray;
   }


   let total = (arr) =>{
       let sum = 0;
       for(i = 0;i <arr.length;i++){
         sum = sum + arr[i].score;
       }
       console.log("Total users score " + sum);
   }


 let addToItems = (arr)=> {
     for(i = 0;i < arr.length;i++){
        let item = null;
        console.log("items length: " + arr[i].items.length);
         for(j = 0;j < arr[i].items.length;j++){
         item = arr[i].items[j].concat("!");
        arr[i].items[j] = item
      }
     }
     console.log(arr);
 }
  
  method(username,username_question,array);
  console.log(filter(array));
  total(array);
  addToItems(array);

  /** ------------------------------------------------ */

  let printStars = () =>{
    let space = 5;
    for(let i = 0;i < 5;i++){
          for(let j = 0;j <= space;j++){
            console.log(" ");
          }
          for(let k = 0;k <= i;k++){
            console.log(" * ");
          }
          space--;
    }

  }

printStars();  