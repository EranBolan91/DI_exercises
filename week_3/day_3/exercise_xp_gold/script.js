let totalTip = document.getElementById('totalTip');
totalTip.style.display = 'none';

calculateTip = () =>{
    let billAmt = document.getElementById('billamt').value;
    let serviceQual = document.getElementById('serviceQual').value;
    let numOfPeople = document.getElementById('peopleamt').value;
    
    let tip = document.getElementById('tip');
    let total;

    if(serviceQual == 0 || billAmt == 0){
        alert("Please fill the form");
        return;
    }

    if(numOfPeople == "" || numOfPeople < 1){
        numOfPeople = 1;
        let hideEachTag = document.getElementById('each');
        hideEachTag.style.display ='none';
    }
    
    total = ((billAmt * serviceQual)/numOfPeople).toFixed(2);
    totalTip.style.display = 'block';
    tip.innerHTML = total;
}

