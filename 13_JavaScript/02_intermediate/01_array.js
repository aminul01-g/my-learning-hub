const fruits = ['apple', 'banana', 'orange'];
console.log(fruits);

// print length of the array
console.log(fruits.length);

// Indexing arrays 
console.log(fruits[0]); // apple
console.log(fruits[1]); // banana
console.log(fruits[2]); // orange

// change an array element
fruits[1] = 'grape';
console.log(fruits); // ['apple', 'grape', 'orange']

// add an element to the array
fruits.push('kiwi');
console.log(fruits); // ['apple', 'grape', 'orange', 'kiwi']

// remove an element from the array
fruits.pop();
console.log(fruits); // ['apple', 'grape', 'orange']

// check the length of the array
console.log(fruits.length); // 3

// iterate over array elements (classic for-loop)
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// iterate over array elements (for...of)
for (const fruit of fruits) {
    console.log(fruit);
}

// iterate over array elements (forEach)
fruits.forEach((fruit) => {
    console.log(fruit);
});

// find index of an element
const index = fruits.indexOf('grape');
console.log(index); // 1

// check if array includes an element
const hasApple = fruits.includes('apple');
console.log(hasApple); // true

// remove a specific element from the array
const removedFruit = fruits.splice(index, 1);
console.log(removedFruit); // ['grape']
console.log(fruits); // ['apple', 'orange']

// sort array elements
fruits.sort();
console.log(fruits); // ['apple', 'orange']

// reverse array elements
fruits.reverse();
console.log(fruits); // ['orange', 'apple']

// concatenate arrays
const moreFruits = ['banana', 'kiwi'];
const allFruits = fruits.concat(moreFruits);
console.log(allFruits); // ['orange', 'apple', 'banana', 'kiwi']

// convert array elements to a string (with comma and space)
const fruitString = fruits.join(', ');
console.log(fruitString); // 'orange, apple'

// convert array elements to a string (without separator)
const fruitStringNoSeparator = fruits.join('');
console.log(fruitStringNoSeparator); // 'orangeapple'

// convert array elements to a string (with ' - ' separator)
const fruitStringWithSeparator = fruits.join(' - ');
console.log(fruitStringWithSeparator); // 'orange - apple'


// check if a variable is an array & convert a string to an array
console.log(Array.isArray(fruits)); // true
console.log(Array.isArray("Aminul")); // false
console.log(Array.from("Aminul")); // ['A', 'm', 'i', 'n', 'u', 'l']
console.log(Array.of(1, 2, 3)); // [1, 2, 3]


