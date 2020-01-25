
const ROUNDS = 10;
let secretWord = "bolandian";
let splitArry = secretWord.split("");
let count = splitArry.length;

let initWord = (arr) =>{
   let split = arr.split("");
    for (let i = 1; i < count; i++) {
        if(i == count-1){

        }else{
            split.splice(i,1,"*");
        }   
    }
    return split;
}

let isWin = (word) =>{
    let counter = 0;
    for(value of word){
        if(value == "*"){
            counter = counter +1;
        }
    }
    if(counter > 0){
        return false;
    }else{
        return true;
    }
} 


let arrDisplay = initWord(secretWord);
let char;
let winFlag = false;
let secretWordSplit = secretWord.split("");
for(let i = 0;i < ROUNDS;i++){
    char = prompt("Please enter a character");
    if((isNaN(char)) && (char.length == 1)){
        for (let i = 1; i < secretWord.length; i++) {
                if(secretWordSplit[i] == char.toLocaleLowerCase()){
                    arrDisplay.splice(i,1,char);
                }
        }
        alert(arrDisplay.join(""));
    }else{
        alert("Please enter only 1 character and no numbers!");
        i--;
    }
    winFlag = isWin(arrDisplay);
    if(winFlag){
        alert("You have Won!");
        break;
    }
    if(i == ROUNDS - 1){
        alert("Too bad, you did not find the secret word. Maybe next time");
    }
    
}

