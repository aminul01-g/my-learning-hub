"use strict"; // Treat all JS code as newer version



// Data types in JavaScript
// 1. Primitive data types: string, number, boolean, null, undefined, symbol
// 2. Non-primitive data types: object (including arrays and functions)

// Primitive Data Types
// String data type
let name = "Aminul Islam"
console.table([name, typeof(name)])


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