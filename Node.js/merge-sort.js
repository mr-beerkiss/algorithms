const arrayEquals = require('./utils').arrayEquals;

const mergeSort = alist => {
  if ( alist.length > 1) {
    const mid = Math.floor(alist.length/2);
    
    const leftHalf = alist.slice(0, mid);
    const rightHalf = alist.slice(mid);

    mergeSort(leftHalf);
    mergeSort(rightHalf);

    let [i, j, k] = [0, 0, 0];

    while (i < leftHalf.length && j < rightHalf.length) {
      if (leftHalf[i] < rightHalf[j]) {
        alist[k++] = leftHalf[i++] 
      } else {
        alist[k++] = rightHalf[j++] 
      }
    }

    while (i < leftHalf.length) alist[k++] = leftHalf[i++]

    while (j < rightHalf.length) alist[k++] = rightHalf[j++]
  }
}

const testProgram = () => {
  const in_arr1 = [54, 26, 93, 17, 77, 31, 44, 55, 20];
  const ex_arr1 = [17, 20, 26, 31, 44, 54, 55, 77, 93];

  mergeSort(in_arr1);

  console.assert(arrayEquals(ex_arr1, in_arr1), 'Expected %o but got %o', ex_arr1, in_arr1);

  const in_arr2 = [7, 1, -2, -5, 0, 6, 3, 15];
  const ex_arr2 = [-5, -2, 0, 1, 3, 6, 7, 15];

  mergeSort(in_arr2);

  console.assert(arrayEquals(ex_arr2, in_arr2), 'Expected %o but got %o', ex_arr2, in_arr2);

  console.log('All tests have passed');
} 

testProgram();
