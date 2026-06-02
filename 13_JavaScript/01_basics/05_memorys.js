// Stack(Primitives) and Heap(Objects, Array, Functions)
let name = "Aminul Islam" // Stack
let person = { // Heap
    name: "Aminul Islam",
    age: 30,
    isStudent: true,
    address: null,
    phoneNumber: undefined,
    uniqueId: Symbol("id")
}

console.log(name) // "Aminul Islam"
console.log(person) // {name: "Aminul Islam", age: 30, isStudent: true, address: null, phoneNumber: undefined, uniqueId: Symbol(id)}

// When we assign a primitive value to a variable, it is stored in the stack. When we assign an object to a variable, it is stored in the heap.
// The variable holds a reference to the location of the object in the heap. When we access the variable, it retrieves the value from the stack or the reference from the heap, depending on the type of data. 


