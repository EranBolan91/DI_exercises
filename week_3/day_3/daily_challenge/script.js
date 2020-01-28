let sentences = [
    "What came first,the chichken or the NOUN .",
    "Be careful not to vacuum the NOUN when you clean under your bed.",
    "BBQ at my house! Everyones invited, and its bring your own NOUN ",
    "One that ADJECTIVE music comes on,its time to shut down your acceptance speech!",
    "Dear NAME you are NOUN ",
    "Please excuse NAME who is far too ADJECTIVE to attend NOUN class",
    "I cant start my day without NOUN"
]

let nounInput = document.getElementById("noun");
let adjectiveInput = document.getElementById("adjective");
let personInput = document.getElementById("person");

let count = 0;
var libButton = document.getElementById('lib-button');
    var libIt = function() {

        let sente = sentences[count];
        var storyDiv = document.getElementById("story");

        if(adjectiveInput.value != ""){
            storyDiv.innerHTML = sente.replace("ADJECTIVE",adjectiveInput.value); 
            console.log(adjectiveInput.value);   
        }
        if(nounInput.value != ""){
            storyDiv.innerHTML = sente.replace("NOUN",nounInput.value);
            console.log(nounInput.value);
            
        }
        if(personInput.value != ""){
            storyDiv.innerHTML = sente.replace("NAME",personInput.value);
            console.log(personInput.value);
        }
        count++;
    };
    libButton.addEventListener('click', libIt);

    /**Need to check why it doesn't replace ADJECTIVE and NOUN but NAME it does replace */