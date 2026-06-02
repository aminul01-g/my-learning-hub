"use strict"; // Treat all JS code as newer version



// Data types in JavaScript
// 1. Primitive data types: string, number, boolean, null, undefined, symbol
// 2. Non-primitive data types: object (including arrays and functions)

// Primitive Data Types
// String data type
let name = "Aminul Islam"
console.table([name, typeof(name)])
console.log(`Hello my name is ${name}`);

let gameName = new String(' Clash of Clan');
console.log(gameName); // simply pring the game name
console.log(gameName.__proto__); //  
console.log(gameName.toLocaleLowerCase()); // convert into Lowercase
console.log(gameName.toUpperCase()); // convert into Uppercase
console.log(gameName.charAt(3)); // find char in index 3
console.log(gameName.indexOf('a')); // find the index of a char
console.log(gameName.substring(3,6)); // print a substring
console.log(gameName.slice(-12, 4)); // 
console.log(gameName.trim()); // remove the extra space
console.log(gameName.replace('n', 'N')); // replace one to another
console.log(gameName.includes('i')); // is there or not



// Number data type -> 2^53
let age = 20
console.table([age, typeof(age)])


// BigInt data type -> 2^53 + 1
let a = 9007199254740991n
console.table([a, typeof(a)])


// Boolean data type
let isStudent = true
console.table([isStudent, typeof(isStudent)])


// Null data type
let address = null
console.table([address, typeof(address)])


// Undefined data type
let phoneNumber;
console.table([phoneNumber, typeof(phoneNumber)])



// Symbol data type
let uniqueId = Symbol("id")
console.table([uniqueId, typeof(uniqueId)])


//-----------------------------------------------------------
//****************** Non-Primitive Data Types ********************
// Array, Objects, Functions

let numbers = [1, 2, 3, 4, 5] // Array
console.log(numbers)


// Object data type
let person = {
    name: "Aminul Islam",
    age: 30,
    isStudent: true,
    address: null,
    phoneNumber: undefined,
    uniqueId: Symbol("id")
}
console.table([person, typeof(person)])     

let func = function(){
    console.log("Hello World");
} // Function

console.log(func)