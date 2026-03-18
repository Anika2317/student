---
layout: post
title: Strings Homework
description: Strings Homework
categories: ['Javascript', 'Homework']
permalink: /strings-homework
author: Makers
---

<hr>

# JavaScript Strings Popcorn Hacks & Homework

## Popcorn Hack #1 - Secret Password

### Instructions:

1.	Create three string variables named secretBase, codeWord, and symbol.
	•	Each should contain text inside quotes (" " or ' ').
2.	Find the number of characters in the secretBase string.
	•	Use the .length property to count how many characters are in the string.
	•	Store this value in a new variable called baseLength.
3.	Change all the letters in the codeWord string to uppercase.
	•	Use the .toUpperCase() method and store the result in a variable named fullCode.
4.	Combine all the strings together to reveal the full secret message.
	•	Use the + operator to concatenate secretBase, fullCode, and symbol.
	•	Save it to a variable named fullSecret.
5.	Print your results using console.log().
	•	Display both the string length and the full secret message in the console.


```javascript
%%javascript

// Popcorn Hack #1 - Secret Password

// Task 1: Create your variables
let secretBase = "anikasHQ";
let codeWord = "amazingness";
let symbol = "#007";

// Task 2: Find the number of characters in the first string.
let baseLength = secretBase.length;

// Task 3: Standardize the second string to all uppercase letters.
let fullCode = codeWord.toUpperCase();

// Task 4: Combine everything to reveal the full secret.
let fullSecret = secretBase + fullCode + symbol;

// Task 5: Print the results.
console.log("Base Length:");
console.log(baseLength);

console.log("Full Code:");
console.log(fullCode);

console.log("Full Secret:");
console.log(fullSecret);

```


    <IPython.core.display.Javascript object>


<hr>

## Popcorn Hack #2 - Grocery Store

### Instructions:

1.	Define your variables and string values
	•	Each should contain text inside quotes (" " or ' ').
    •	Your variables should include: `ingredient`, `price`, and `store`.
2.	Write a message using template liberals.
	•	Using mlti-line strings and interpolation, create a complex sentence writing an automated message advertising a discounted item.
	•	Use backticks!!
3.	Use interpolation to check the amount of characters in the lesson!
	•	Use `${}` and `.length` to help.
4.	Print your results using console.log().
	•	Display both the string length and the full secret message in the console.


```javascript
%%javascript

// Popcorn Hack #2 - Grocery Store

// Task 1: Define your variables and strings
let ingredient = "amazing apples"; 
let price = "$17.23/ounce";
let store = "store of food";

// Task 2: Write the complex sentence using a template literal (backticks).
const snackMessage = `
🍎 Special Deal Alert! 🍎

There is a store called ${store}, come and get ${ingredient}, but it's ${price}!
Don’t miss out on this amazing deal.
`;

// Task 3. Check the length of the full message and print it to the console.
console.log(`The full message is ${snackMessage.length} characters long.`);
console.log(snackMessage);

```


    <IPython.core.display.Javascript object>


<hr>

# Homework

Objective: Apply string concepts (const, quotes, .length, .toUpperCase(), and template literals) to format game data.

## 🏷️ Part A - String Variables & Quotes
Create a constant variable named `UPGRADE_NAME` and assign it the string value `"Lucky Seven"`. Print this variable to the console.

Create a variable named `cost` and assign it the number value 7777. Print this number to the console.

Create a variable named `EMOJI` and assign it the emoji string value "🍀". 

Create a variable named `BUTTON_CLASS` and assign it the string value: bg-green-500 hover:bg-green-600 text-white. 

## 📏 Part B – Length and Modification
Using the `UPGRADE_NAME` variable from above, create a new constant variable named `DISPLAY_NAME` that converts the name to all uppercase letters. Print `DISPLAY_NAME`.

Create a constant variable named `NAME_LENGTH` that stores the total number of characters (including spaces) in the original `UPGRADE_NAME`. Print the length to the console with a label like: "Name Character Count: [Count]".

Create a variable named message that stores the exact string below. 

"Insufficient Cookies"

## ✨ Part C – Template Literal Interpolation
Use string concatenation (the + sign) to combine the EMOJI, UPGRADE_NAME, and cost variables into the following exact output. Print the result.
Challenge (extra credit): Use String Interpolation 

🍀 Lucky Seven (7777 Cookies)
Now, rewrite the entire message from problem 8 using a template literal (backticks `) and interpolation (${}). Store the result in a new variable called shopButtonText. Print shopButtonText.

The Final Message: Create a constant variable named errorDisplay that uses a template literal to combine the following three variables into one clean message: EMOJI, UPGRADE_NAME, and message.

Error: 🍀 Lucky Seven purchase failed: "Insufficient Cookies"
Hint: The quote marks around Insufficient Cookies must be part of the final output string.


🌟 Extra Credit Challenge (Optional)
Create a variable named `HINT_TEXT` that stores the following exact quote:
The "Lucky Seven" upgrade multiplies your clicks by 7.



```javascript
%%javascript

// --- JavaScript Homework (All in One Cell) ---

//  Part A - String Variables & Quotes
const UPGRADE_NAME = "Lucky Seven";
console.log("UPGRADE_NAME:", UPGRADE_NAME);

let cost = 7777;
console.log("Cost:", cost);

let EMOJI = "🍀";
let BUTTON_CLASS = "bg-green-500 hover:bg-green-600 text-white";
console.log("BUTTON_CLASS:", BUTTON_CLASS);

//  Part B – Length and Modification
const DISPLAY_NAME = UPGRADE_NAME.toUpperCase();
console.log("DISPLAY_NAME:", DISPLAY_NAME);

const NAME_LENGTH = UPGRADE_NAME.length;
console.log("Name Character Count:", NAME_LENGTH);

let message = "Insufficient Cookies";
console.log("Message:", message);

//  Part C – Template Literal Interpolation
// 1. Using string concatenation
let legacyOutput = EMOJI + " " + UPGRADE_NAME + " (" + cost + " Cookies)";
console.log("Legacy Output:", legacyOutput);

// 2. Using template literal
let shopButtonText = `{EMOJI} {UPGRADE_NAME} ({cost} Cookies)`;
console.log("Shop Button Text:", shopButtonText);

// 3. Final error message with quote marks included
const errorDisplay = `Error: {EMOJI} {UPGRADE_NAME} purchase failed: "{message}"`;
console.log("Error Display:", errorDisplay);

//  Extra Credit Challenge
let HINT_TEXT = 'The "Lucky Seven" upgrade multiplies your clicks by 7.';
console.log("Hint Text:", HINT_TEXT);

```


    <IPython.core.display.Javascript object>

