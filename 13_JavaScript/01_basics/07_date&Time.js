//*************Date****************** */
console.log("************************Date*********************");

// Date is a built-in object in JavaScript that allows you to work with dates and times. It provides various methods to create, manipulate, and format dates. Here are some examples of how to use the Date object:

// Create a new Date object representing the current date and time
const now = new Date();
console.log(now);
console.log(typeof now); // "object"

// Create a Date object for a specific date and time
const specificDate = new Date('2022-01-01T12:00:00');
console.log(specificDate);

// Get the current year, month, day, hours, minutes, and seconds
console.log('Year:', now.getFullYear());
console.log('Month:', now.getMonth() + 1); // Months are zero-indexed
console.log('Day:', now.getDate());
console.log('Hours:', now.getHours());
console.log('Minutes:', now.getMinutes());
console.log('Seconds:', now.getSeconds());

// Format a date as a string
const formattedDate = now.toLocaleDateString();
console.log('Formatted Date:', formattedDate);

// Calculate the difference between two dates
const date1 = new Date('2022-01-01');
const date2 = new Date('2022-01-10');
const timeDifference = date2 - date1; // Difference in milliseconds
const dayDifference = timeDifference / (1000 * 60 * 60 * 24); // Convert to days
console.log('Difference in days:', dayDifference);

// Add days to a date
const futureDate = new Date();
futureDate.setDate(futureDate.getDate() + 7); // Add 7 days
console.log('Future Date:', futureDate);

// Get the current timestamp (milliseconds since January 1, 1970)
const timestamp = Date.now();
console.log('Current Timestamp:', timestamp);




//**********************Time*************************/
console.log("************************Time*********************");


// Time is often represented as a part of the Date object in JavaScript. You can manipulate time using the Date object methods. Here are some examples:

// Get the current time
const currentTime = new Date();
console.log('Current Time:', currentTime.toLocaleTimeString());

// Set a specific time
const specificTime = new Date();
specificTime.setHours(15);
specificTime.setMinutes(30);
specificTime.setSeconds(0);
console.log('Specific Time:', specificTime.toLocaleTimeString());

// Calculate the difference between two times
const time1 = new Date('2022-01-01T10:00:00');
const time2 = new Date('2022-01-01T12:30:00');
const timeDifferenceInMs = time2 - time1; // Difference in milliseconds
const timeDifferenceInHours = timeDifferenceInMs / (1000 * 60 * 60); // Convert to hours
console.log('Difference in hours:', timeDifferenceInHours);

// Add hours to a time
const futureTime = new Date();
futureTime.setHours(futureTime.getHours() + 3); // Add 3 hours
console.log('Future Time:', futureTime.toLocaleTimeString());

// Get the current date and time in ISO format
const isoString = new Date().toISOString();
console.log('Current Date and Time in ISO format:', isoString);

// Get the current date and time in UTC
const utcString = new Date().toUTCString();
console.log('Current Date and Time in UTC:', utcString);

// Get the current date and time in a specific locale
const localeString = new Date().toLocaleString('en-US');
console.log('Current Date and Time in en-US locale:', localeString);

// Get the current date and time in a different time zone
const timeZoneString = new Date().toLocaleString('en-US', { timeZone: 'America/New_York' });
console.log('Current Date and Time in New York:', timeZoneString);