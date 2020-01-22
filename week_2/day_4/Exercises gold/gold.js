let times = 0;

let playTheGame = () =>{
    let newGame;
    let flag = 0;
  do{
      let numbers = confirm();
      console.log("PlayTheGame - check what the output " + numbers);
      if(numbers != false){
          newGame = test(numbers[0],numbers[1]);
          if(newGame == true){
              alert("To play again, please refresh the page");
              newGame = false;
              flag = 1;
          }
      }else{
          newGame = false;
      }
    } while(newGame) 
    if(flag == 1){
        alert("To play again, please refresh the page");
    }else{
        alert("You couldn't guess the computer number, you might succeed next time");
    }
}

let exit = true;
let confirm = () => {
    let arrNumbers = [];
    do{
        let number = prompt("Please enter a number between 0 - 10");
        if(isNaN(number)){
            alert("Sorry Not a number, Goodbye");
            exit = true;
        }else if(number > 10 || number < 0){
            alert("Sorry the number is not in the range 0 - 10");
            exit = true;
        }else if(number == "no"){
            exit = false;
            alert("Thanks for playing - Goodbye");
        }else{
            exit = false;
            let computerNumber = Math.floor(Math.random()*11);
            arrNumbers.push(number);
            arrNumbers.push(computerNumber);
            console.log(computerNumber);
        }
    }while(exit)

    return arrNumbers;
}

let test = (userNumber,computerNumber) => {
    while(times < 2){
        if(userNumber == computerNumber){
            alert("You have won the computer!");
            return true;
        }else if(userNumber > computerNumber){
            alert("Your number is bigger then the computer's number, try again");
            times = times + 1;
            console.log(times);
            confirm();
        }else if(userNumber < computerNumber){
            alert("Your number is lower then the computer's number,try again");
            console.log(times);
            times++;
            confirm();
        }
    }
    console.log("---------------------");
    return false;
}

playTheGame();