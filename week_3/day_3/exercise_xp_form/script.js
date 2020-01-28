//1)Show the value and the text of the selected option.
// let opt = document.getElementById("genres");

// console.log(opt.value);
// console.log(opt[1].text);



//Exercise 2
//1)Create a form with two inputs text : student_first_name and lstudent_last_name and a button.

let student_list = document.getElementById('student_list');
let buttonAdd = document.getElementById('add');
let calcButton = document.getElementById('calc');
let h4_first = document.createElement('h4');
let h4_last = document.createElement('h4');
let removeButton = document.createElement('button');
let students = 0;

h4_first.classList.add('title');
h4_last.classList.add('title');
student_list.classList.add('student_list');



buttonAdd.addEventListener('click',function(){
    let box = document.createElement('div');
    box.setAttribute('id',students);
    box.classList.add('box');

    let h4_first = document.createElement('h4');
    let h4_last = document.createElement('h4');
    
    removeButton.setAttribute('id','removeButton');
    removeButton.innerHTML = 'remove';

    h4_first.classList.add('title');
    h4_last.classList.add('title');
    box.appendChild(h4_first);
    box.appendChild(h4_last);
    box.appendChild(removeButton);
    
    let first_name_input = document.getElementById('first_name').value;
    let last_name_input = document.getElementById('last_name').value;
        h4_first.innerHTML = first_name_input;
        h4_last.innerHTML = last_name_input;

        student_list.appendChild(box);
        students++;
});

calcButton.addEventListener('click',function(){
    alert("There are " + students + " students in the class");
});


removeButton.addEventListener('click',function(value){
    console.log(value);
    //not sure how to delete -- need to ask
});