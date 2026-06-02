// Convertions

// String to Number
let score1 = "33"
console.log(typeof(score1))

let convertedScore = Number(score1)
console.log(typeof(convertedScore))

// Number to String
let score2 = 44
console.log(typeof(score2))

let convertedScore2 = String(score2)
console.log(typeof(convertedScore2))

// Type coercion
let score3 = "55"
let score4 = 66

let totalScore = score3 + score4
console.log(totalScore) // "5566" (string concatenation)

totalScore = Number(score3) + score4
console.log(totalScore) // 121 (number addition)



// -------------------------------------------------------------------
// ***********************Operations*********************************
let x = 10
let y = 5

console.log(x + y) // 15 (addition)
console.log(x - y) // 5 (subtraction)
console.log(x * y) // 50 (multiplication)
console.log(x / y) // 2 (division)
console.log(x % y) // 0 (modulus/reminder)
console.log(x ** y) // 100000 (exponentiation)
console.log(++x) // 11 (increment)
console.log(--x) // 10 (decrement)
console.log(-x) // -10 (negative value)
console.log("1" + 2 + 2) // "122" (string conversion)
console.log(1 + 2 + "2") // "32" (number(1 + 2), String(2))


