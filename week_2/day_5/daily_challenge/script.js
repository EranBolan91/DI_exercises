let getUserNumber = () =>{
    return prompt("Please enter your bottles number");
}

let bottlesCount = 1;
let bottlesNumber = getUserNumber();
// for(let i = bottlesNumber ;i != 0; i--){
//     console.log(i + " bottles of beer on the wall");
//     console.log(i + " bottles of beer");
//     if(bottlesCount == 1){
//         console.log("Take " + bottlesCount + " down,pass it around");
//     }else{
//     console.log("Take " + bottlesCount + " down,pass them around");
//     }
//     console.log(i - bottlesCount + " bottles of beer on the wall");
//     console.log(i - bottlesCount + " bottles of beer on the wall");
//     console.log(i - bottlesCount + " bottles of beer");
//     bottlesCount = bottlesCount + 1;
    
//     console.log("----------------------");
//     console.log("\n");
// }


while(bottlesNumber > 0){
    console.log(bottlesNumber + " bottles of beer on the wall");
    console.log(bottlesNumber + " bottles of beer");
    if(bottlesCount == 1){
        console.log("Take " + bottlesCount + " down,pass it around");
    }else{
    console.log("Take " + bottlesCount + " down,pass them around");
    }
    console.log(bottlesNumber - bottlesCount + " bottles of beer on the wall");
    console.log(bottlesNumber - bottlesCount + " bottles of beer on the wall");
    console.log(bottlesNumber - bottlesCount + " bottles of beer");
    bottlesNumber = bottlesNumber - bottlesCount;
    bottlesCount = bottlesCount + 1;

    console.log("----------------------");
    console.log("\n");
    
}