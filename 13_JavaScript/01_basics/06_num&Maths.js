const blance = new Number(100);
console.log(blance);
console.log(typeof blance);

const num1 = 10;
const num2 = 20;
const num3 = 30;
const num4 = 40.8911;

// *************************Numbers*****************************
console.log("*************************Numbers*****************************");


console.log(num1 + num2);
console.log(num1 - num2);
console.log(num1 * num2);
console.log(num1 / num2);
console.log(num1 % num2);

console.assert(num1 < num2, "num1 should be less than num2");
console.assert(num1 > num2, "num1 should be greater than num2"); // This will trigger an assertion error

console.log(num4.toFixed(2)); // Rounds to 2 decimal places
console.log(num4.toPrecision(3)); // Rounds to 3 significant digits

console.log(Number.isInteger(num1)); // true
console.log(Number.isInteger(num4)); // false

console.log(Number.isNaN(NaN)); // true
console.log(Number.isNaN(123)); // false

console.log(Number.isFinite(123)); // true
console.log(Number.isFinite(Infinity)); // false

const strNum = "123";
console.log(Number(strNum)); // Converts string to number
console.log(parseInt(strNum)); // Parses string to integer
console.log(parseFloat("123.45")); // Parses string to float

console.log(num1.toString()); // Converts number to string
console.log(num1.toExponential(2)); // Converts to exponential notation with 2 decimal places




//********************************Maths******************* */

console.log("************************Maths*********************");

console.log(Math.max(num1, num2, num3)); // Maximum value
console.log(Math.min(num1, num2, num3)); // Minimum value

console.log(Math.abs(-5)); // Absolute value

console.log(Math.PI); // Pi constant
console.log(Math.E); // Euler's number

console.log(Math.round(4.7)); // Round to the nearest integer
console.log(Math.round(4.4)); // Round to the nearest integer

console.log(Math.ceil(4.4)); // Ceil rounds up to the nearest integer
console.log(Math.ceil(4.7)); // Ceil rounds up to the nearest integer

console.log(Math.floor(4.7)); // Floor rounds down to the nearest integer
console.log(Math.floor(4.4)); // Floor rounds down to the nearest integer

console.log(Math.sqrt(16)); // Square root
console.log(Math.pow(2, 4)); // 2 raised to the power of 4

console.log(Math.random()); // Random number between 0 and 1
console.log(Math.floor(Math.random() * 10) + 1); // Random number between 1 and 10

console.log(Math.sign(-5)); // -1 (negative number)
console.log(Math.sign(0)); // 0 (zero)
console.log(Math.sign(5)); // 1 (positive number)

console.log(Math.trunc(4.7)); // Truncates the decimal part
console.log(Math.trunc(-4.7)); // Truncates the decimal part
