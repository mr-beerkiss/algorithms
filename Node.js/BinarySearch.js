const primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 
    103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163 ,167, 173, 179, 181, 191, 193, 197, 199, 
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283
];

function binarySearch(arr, target) {
    let min = 0;
    let max = arr.length - 1;
    //let mid = Math.floor(max / 2);

    const bailLimit = 10;
    let count = 0;
    while (max >= min) {
        // console.log(`
        // Min: ${min} 
        // Max: ${max},
        // Mid: ${mid}`);
        // if (++count >= bailLimit) {
        //     console.log('bailing');
        //     return -1;
        // }

        // // if (min === max && arr[min] !== target) {
        // if (min > max) {
        //     console.log('not found');
        //     return -1;
        // }

        // if (arr[mid] === target) {
        //     console.log(`found result in ${count} steps`);
        //     return mid;
        // } else if (arr[mid] < target) {            
        //     min = mid;
        //     mid = Math.floor(min + (max - min)/2);
        // } else {
        //     max = mid;
        //     mid = Math.floor(max / 2);
        // }
        if (++count >= bailLimit) return -101;
        const guess = min + Math.floor((max-min)/2);
        //  console.log(`
        // Min: ${min} 
        // Max: ${max},
        // Guess: ${guess}`);
        if (arr[guess] === target) {
            console.log(`found result in ${count} steps`);
            return guess;
        } else if ( arr[guess] < target ) {
            min = guess + 1;
        } else {
            max = guess - 1;
        }

        
    }

    return -1;
}

function assert(a, b) {
    if (a !== b) throw Error(`Assertion failed, ${a} !== ${b}`);
    return "Works";
}

console.log(assert(binarySearch(primes, 67), 18));
console.log(assert(binarySearch(primes, 3), 1));
console.log(assert(binarySearch(primes, 13), 5));
console.log(assert(binarySearch(primes, 97), 24));
console.log(assert(binarySearch(primes, 2), 0));
console.log(assert(binarySearch(primes, 277), primes.indexOf(277)));
console.log(assert(binarySearch(primes, 139), primes.indexOf(139)));
console.log(assert(binarySearch(primes, 8), -1));