let sentence = ['bolandian','eraneranRan','saying','shalom'];
let spaceArr = [];

let checkLengthWord = (sentenceString) =>{
    let word,wordLength = 0,tempIndex;
    sentenceString.forEach((value,index) => {
        word = value.length;
        if(wordLength < word){
            wordLength = word;
            tempIndex = index;
        }
    });
    sentenceString.forEach((value,index)=>{
        word = value.length;
        spaceArr.push(wordLength - word);
    });
    console.log("Space arry " + spaceArr);
    return wordLength;
}

// let frame = (sentenceString) =>{
//     let length = checkLengthWord(sentenceString);
//     let heightFrame = sentenceString.length;
//     let printFrame = "";
//     let index = 0;
//     for (let i = 0; i < heightFrame+1; i++) {
//         let spacer = spaceArr[i];
//         for(let j = 0; j < length+2;j++){
//                 //print the first row stars
//                 if(i == 0){  
//                     printFrame = printFrame + "*";
//                     //console.log("*");
//                     //console.log("first line " + j);
//                 }else if(j == length+1){ //print the last star in each line
//                     printFrame = printFrame + "*";
//                     //console.log("*");
//                     //console.log("\n");
//                 }else if((j == 1) && !(i == 0)){ //print the first star and the sentence
//                     printFrame = printFrame + "*";
//                     printFrame = printFrame + sentence[index];
//                     //console.log("*");
//                     //console.log(sentence[index]);
//                     index++;
//                 }else if(i == heightFrame){
//                     printFrame = printFrame + "*";
//                     //console.log("*"); //prints the end row
//                 }else {
//                     printFrame = printFrame + " ";
//                     //console.log(" "); //print spaces
//                 }
//         }
//         console.log(printFrame);
//         console.log("\n");
//         printFrame = "";
//     }
//     //console.log(printFrame);
// }

// frame(sentence);

// let str;
//   for (let index = 0; index < 10; index++) {
//       str = str + "*";
//   }
// console.log(str);


// let frame = (sentenceString) =>{
//     let length = checkLengthWord(sentenceString);
//     let heightFrame = sentenceString.length;
//     let printFrame = "";
//     let index = 0;
//     for (let i = 0; i < heightFrame+1; i++) {
//         let spacer = spaceArr[i];
//         console.log(spacer);
//         for(let j = 0; j < length+2;j++){
//                 //print the first row stars
//                 if(i == 0){  
//                     printFrame = printFrame + "*";
//                 }else if(j == 0 && (i != 0)){
//                     console.log("inside the j == 1");
//                     printFrame = printFrame + "*";
//                     printFrame = printFrame + sentence[index];
//                 }else if(spacer > 0 && j == 1){ // this if adds the spaces after the word and put star in the end
//                     for(i = 0;i <= spacer;i++){
//                         if(i == spacer){ //checks if the is end, otherwise keep add space
//                             printFrame = printFrame + "*";
//                         }else{
//                             printFrame = printFrame + " ";
//                         }
//                     }
//                 }else if(i == heightFrame+1){
//                     printFrame = printFrame + "*";
//                 }
//         }
//         console.log(printFrame);
//         console.log("\n");
//         printFrame = "";
//     }
//     //console.log(printFrame);
// }


let frame = (sentenceString) =>{
    let length = checkLengthWord(sentenceString);
    let heightFrame = sentenceString.length;
    console.log("height frame: " + heightFrame);
    let printFrame = "";
    let index = 0;
    for (let i = 0; i < heightFrame; i++) {
        let spacer = spaceArr[i-1];
        let count = 0;
        if(i == 0){
            for(i = 0;i < length;i++){
                printFrame = printFrame + "*";
            }
            index++;
            console.log("Spacer: " + spacer);
            console.log("index: " +index);
            console.log(printFrame);
            console.log("\n");
            printFrame = "";
        }else if(i == heightFrame-1){
            console.log("IF end");
            for(i = 0;i < length;i++){
                printFrame = printFrame + "*";
            }
            index++;
            console.log(printFrame);
            console.log("\n");
            printFrame = "";
        }else{
            console.log("The else");
            printFrame = printFrame +"*"+sentence[index];
            while(count < spacer){
             printFrame = printFrame + " ";
             count++;   
             console.log("Count: " + count + "Spacer: " +spacer)
            }
             index++;
             printFrame = printFrame + "*";
             console.log(printFrame);
             console.log("\n");
             printFrame = "";
        }
        
    }
    //console.log(printFrame);
}

frame(sentence);
