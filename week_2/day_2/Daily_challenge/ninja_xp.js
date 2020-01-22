var me = [];

me.push("my","favorite","color","is","blue");

var str1 = "mix";
var str2 = "pod";
var x = str1.substr(2);
var d = str2.substr(2);
var newWord = str1.replace("x",d) + " " + str2.replace("d",x);
console.log(newWord); 

console.log("-----------");

var str = "swim";

function wordadd(str)

let word = "welcome";
let check = (str) => {
    if(str.length >= 3){
       var lastwords = str.substring(str.length -3 ,str.length);
       if(lastwords == "ing"){
         return str.concat("ly");
       }else{
         return str.concat("ing");
       }  
    }else{
        return str;
    }
}

console.log(check(word));

var not = "not";
var bad = "bad";
var line ="This dinner is not that bad!";
var line2 = "‘This movie is not so bad!";
var line3 = "This dinner is bad!";

let checkLine = (stringLine) =>{
    if(stringLine.includes(not)){
        var indexBad = stringLine.indexOf(bad);
        var indexNot = stringLine.indexOf(not);
        if(indexBad > indexNot){
          var newline = stringLine.substr(0,indexNot) + "good!" + stringLine.substr(indexNot+stringLine.length); 
            console.log(newline);
        }
    }else{
        console.log(stringLine);
    }
}

checkLine(line3);