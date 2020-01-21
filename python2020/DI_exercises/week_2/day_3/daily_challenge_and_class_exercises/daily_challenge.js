const arr = [5,0,9,1,7,4,2,6,3,8];

let sorting = (array) =>{
    let temp = 0;
    for(let i = 0;i < array.length;i++){
        for(let j = i+1;j < array.length;j++){
                if(array[i] > array[j]){
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp; 
                }
        }
    }
    console.log(array);
}

sorting(arr);