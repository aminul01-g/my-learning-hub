//*************singleton object - only one instance exists

const john = new Object(); // creates an empty object

// Object.create() - creates a new object with the specified prototype
Object.create(null) // creates an empty object with no prototype 





//************ */ Object literals**************

const mysymbol = Symbol('mySymbol'); // unique symbol

// Object methods
const person = {
    name: 'Alice',
    [mysymbol]: 'This is a dynamic property',
    age: 25,
    greet() {
        console.log(`Hi, I'm ${this.name} and I'm ${this.age} years old.`);
    }
}

person.greet(); // Hi, I'm Alice and I'm 25 years old.

console.log("\n");

// Object.keys() - returns an array of the object's own property names
console.log(Object.keys(person)); // ['name', 'age', 'greet']

console.log("\n");


// Object.values() - returns an array of the object's own property values
console.log(Object.values(person)); // ['Alice', 25, [Function: greet]]

console.log("\n");


// Object.entries() - returns an array of the object's own key-value pairs
console.log(Object.entries(person)); // [['name', 'Alice'], ['age', 25], ['greet', [Function: greet]]]

console.log("\n");


// Accessing dynamic property using symbol
console.log(person[mysymbol]); // This is a dynamic property

console.log("\n");


// Object.assign() - copies properties from source objects to a target object
const target = {};
const source = { a: 1, b: 2 };
Object.assign(target, source);
console.log(target); // { a: 1, b: 2 }

console.log("\n");


// Object.hasOwnProperty() - checks if the object has a specific property as its own (not inherited)
console.log(person.hasOwnProperty('name')); // true
console.log(person.hasOwnProperty('toString')); // false (inherited from Object.prototype)

console.log("\n");


// Object.getOwnPropertyDescriptor() - returns a property descriptor for a specific property
const descriptor = Object.getOwnPropertyDescriptor(person, 'name');
console.log(descriptor); // { value: 'Alice', writable: true, enumerable: true, configurable: true }

console.log("\n");


// Object.defineProperty() - defines a new property or modifies an existing property on an object
Object.defineProperty(person, 'gender', {
    value: 'Female',
    writable: false,
    enumerable: true,
    configurable: true
});
console.log(person.gender); // Female

console.log("\n");

// ****************nested objects*****************
const company = {
    name: 'Tech Co.',
    employees: [
        { name: 'Alice', position: 'Developer' },
        { name: 'Bob', position: 'Designer' }
    ]
};

console.log(company.employees[0].name); // Alice
console.log(company.employees[1].name); // Bob

console.log("\n");

// *****************object merging*****************
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const merged = { ...obj1, ...obj2 };
const mergedObj = Object.assign({}, obj1, obj2);
console.log(merged); // { a: 1, b: 2, c: 3, d: 4 }
console.log(mergedObj); // { a: 1, b: 2, c: 3, d: 4 }

console.log("\n");

// *****************array of objects*****************
const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' }
];
console.log(users[0].name); // Alice
console.log(users[1].name); // Bob
console.log(users); // [ { id: 1, name: 'Alice' }, { id: 2, name: 'Bob' } ]


console.log("\n");

//*********** Object destructuring**************
const course = {
    title: 'JavaScript Basics',
    duration: '3 hours',
    courseinstructor: 'John Doe'
};

const { title, duration, courseinstructor: instructor } = course;
console.log(title); // JavaScript Basics
console.log(duration); // 3 hours
console.log(instructor); // John Doe


