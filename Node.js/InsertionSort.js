const insert = (array, rightIndex, value) => {
    let j;
    for (j = rightIndex; j >= 0 && array[j] > value; j--) {
        array[j+1] = array[j];
    }
    array[j+1] = value;    
}

const insertSort = array => {
    const opLimit = 7;
    console.log(array);
    for (let i=1; i < array.length; i++) {
        insert(array, i-1, array[i]);
        console.log(array);
        if (i > opLimit ) {
            console.log('Breaking beacause something is clearing wrong');
            break;
        }
    }
}

const array = [22, 11, 99, 88, 9, 7, 42];
insertSort(array);
console.log("Array after sorting", array);