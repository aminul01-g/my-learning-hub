const accountId = 1234567890

// "let" and "var" are used to declare variables in JavaScript.
//  The main difference between them is that "let" has block scope, while "var" has function scope.
//  This means that variables declared with "let" are only accessible within the block they are defined in, while variables declared with "var" are accessible throughout the entire function they are defined in.
let accountEmail = "aminul@gmail.com"
var accountPassword = "12345678"
accountCity = "Dhaka"
let accountState; // undefined


/* Prefer not to use "var" to declare variables in JavaScript, as it can lead to unexpected behavior due to its function scope.
 Instead, it's recommended to use "let" or "const" for variable declarations, as they provide block scope and help prevent accidental variable reassignments. */ 

console.log(accountId)

console.table([accountEmail, accountPassword, accountCity, accountState])


