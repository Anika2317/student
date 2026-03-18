---
layout: post
title: Variables Homework
description: Variables Homework
categories: ['Javascript', 'Homework']
permalink: /variables
author: Tinkerers
---

<style>
.glowing-text {
  color: #fff; /* Set the text color to white or a light color for better contrast */
  text-shadow: 0 0 10px #8a2be2, /* Purple glow */
               0 0 20px #8a2be2, /* Deeper purple glow */
               0 0 30px #4169e1, /* Blue glow */
               0 0 40px #4169e1; /* Deeper blue glow */

  font-weight: bold;
  margin-top: 0;
}
</style>

Presented by the
<h4 class="glowing-text">TINKERERS</h4>

<hr>

# <div style="font-weight:bold; text-decoration:underline;">Popcorn Hack 1 🍿😈</div>

Let's start diving into some of the questions. 

## Instructions

Below instructions refer to this code cell:


```python
%%html

<html>
<body>
  <h2>Popcorn Hack 1 Output</h2>
  <div id="output1"></div>

  <script>
  (() => {

    let name = "Anika and Sophie";
    const age = 23;

    // In practice, you shouldn't use var. This is just for the purposes of teaching :)
    var city = "New York"; 

    // Change vars here
    name = "Anika";
    //age = 2;   // What happens if you uncomment this line ???
    city = "Comp Sci";

    document.getElementById("output1").innerText = name + " is " + age + " years old and resides in " + city + ".";
    console.log(name + " is " + age + " years old and is currently in " + city + ".")

  })();
  </script>
</body>
</html>

```



<html>
<body>
  <h2>Popcorn Hack 1 Output</h2>
  <div id="output1"></div>

  <script>
  (() => {

    let name = "Anika and Sophie";
    const age = 23;

    // In practice, you shouldn't use var. This is just for the purposes of teaching :)
    var city = "New York"; 

    // Change vars here
    name = "Anika";
    //age = 2;   // What happens if you uncomment this line ???
    city = "Comp Sci";

    document.getElementById("output1").innerText = name + " is " + age + " years old and resides in " + city + ".";
    console.log(name + " is " + age + " years old and is currently in " + city + ".")

  })();
  </script>
</body>
</html>



Now, do the below with this code.

1. Adjust var declarations, names, values, etc. Mess around with it and observe any changes/errors. 
2. Think and/or discuss with your table: what changes did you notice?

Now let's make some changes :)

3. Uncomment the line saying `age = 2;` and look at your console. What do you notice?

4. Add a new variable called `hobby` with the value of "painting" and update the DOM output and console output to say:  
   "[NAME] is [AGE] years old, lives in [CITY], and loves [HOBBY]"

5. There's a keyword called `typeof` in JavaScript. Use this keyword to also display the data types of the variables.
   Example: `typeof "John"` gives `"string"` and `typeof 3.14` gives `"number"`

<hr>

# <div style="font-weight:bold; text-decoration:underline;">Popcorn Hack 2 🍿😈</div>

Follow the below instructions.

1. Go to the code cell below this text.
2. Using the correct JS variable naming convention, declare a Magic Number variable with the value returned by `input.value` to get a user response.
3. Convert it to a Number data type using Number(). Example: `let x = Number(x);` turns x into a Number. This is because prompt() always returns Strings.
4. Create variables `doubled`, `squared`, and `tripled` that contain the doubled, squared, and tripled values of the magic number.
5. Display the results in DOM and the console by changing output.innerText and using console.log().


```python
%%html

<p>Click the button after entering your magic number!</p>

<input type="number" id="magicInput" placeholder="Enter magic number">
<button onclick="calculateMagic()">Calculate</button>

<div id="output2">Your results will appear here.</div>

<script>
  function calculateMagic() {
    let input = document.getElementById("magicInput");
    let output = document.getElementById("output2");

    let magicNumber = Number(input.value);

    if (isNaN(magicNumber)) {
      output.innerText = "Please enter a valid number.";
      return;
    }

    let doubled = magicNumber * 2;
    let squared = magicNumber ** 2;
    let half = magicNumber / 2;

    output.innerText = `Doubled: ${doubled}, Squared: ${squared}, Half: ${half}`;
  }
</script>

```



<p>Click the button after entering your magic number!</p>

<input type="number" id="magicInput" placeholder="Enter magic number">
<button onclick="calculateMagic()">Calculate</button>

<div id="output2">Your results will appear here.</div>

<script>
  function calculateMagic() {
    let input = document.getElementById("magicInput");
    let output = document.getElementById("output2");

    let magicNumber = Number(input.value);

    if (isNaN(magicNumber)) {
      output.innerText = "Please enter a valid number.";
      return;
    }

    let doubled = magicNumber * 2;
    let squared = magicNumber ** 2;
    let half = magicNumber / 2;

    output.innerText = `Doubled: ${doubled}, Squared: ${squared}, Half: ${half}`;
  }
</script>




```python

```




<hr>

# Variables Homework (Show what you know!)

### Homework Problems: Understanding JavaScript Variables 

There is a code block below the image saying "Have Fun!" Write your code in there.

### <span style="color: white; text-shadow: 2px 2px 5px white;"> Part A - Creating Variables</span>

1. Create a variable called `name` and store your first name in it. Print it in the console and to DOM.


2. Create two variables `age` and `city`. Print them in a single sentence like:
        - "I am 15 years old and I live in New York."


3. Create a variable `isStudent` (true/false). Print it.

### <span style="color: white; text-shadow: 2px 2px 5px white;"> Part B – Numbers & Strings</span>


4. Create two number variables num1 = 10 and num2 = 5. Print their sum, difference, product, and quotient.


1. Make a variable `favoriteFood` and print:
    My favorite food is ____."

### <span style="color: white; text-shadow: 2px 2px 5px white;">Part C – Practice Problems</span>


6. Swap the values of two variables: x = 7 and y = 3.


7. Create a variable `fullName` by joining two strings: "FirstName" and "LastName".


8. Convert temperature C = 25 into Fahrenheit using F = (C * 9/5) + 32.


9. Create a variable score = 85.
    - Print "Pass" if score >= 50, else "Fail".



10. Write a program that asks for your name and age (use prompt)
     and prints: "Hello <name>, you are <age> years old."

11. Make a project that uses 5 variables to run. It can do anything yuou want, have fun and good luck!

Extra credit (optional): 
    Instead of hard coding the variable for number 9 to 85, make the variable a random number from 1-100.

![An image of have fun](https://as2.ftcdn.net/jpg/05/52/30/29/1000_F_552302940_Nct9zn3a6us0igBJqlkDQzQnbM4LLvmS.jpg "An image of have fun")



```python
%%html
<html>
<body>
 <h2>Homework Output</h2>
 <div id="output"></div>


 <script>
   document.getElementById("output").innerText = ""; // Clear output
   (() => {


     // Part A - Creating Variables
     let name = "Anika";
     const age = 14;
     let city = "San Diego";


     // Part B - Build sentences
     let line1 = "My name is " + name;
     let line2 = "I am " + age + " years old and I live in " + city;


     // Part A - number 3
     let isStudent = true; // or false if you’re not a student
     // Print to console
     console.log("Am I a student? " + isStudent);
     // Add it to the page output
     document.getElementById("output").innerText += "\nAm I a student? " + isStudent;




     // Print both lines to output box
     document.getElementById("output").innerText = line1 + "\n" + line2;


     document.getElementById("output").innerText = line1 + "\n" + line2;
document.getElementById("output").innerText += "\nAm I a student? " + isStudent;


// Part B - Numbers & Strings
let num1 = 10;
let num2 = 5;


// Calculate sum, difference, product, quotient
let sum = num1 + num2;
let difference = num1 - num2;
let product = num1 * num2;
let quotient = num1 / num2;


// Print to console
console.log("Sum:", sum);
console.log("Difference:", difference);
console.log("Product:", product);
console.log("Quotient:", quotient);


// Print to page output
document.getElementById("output").innerText +=
   `\n\nSum: ${sum}` +
   `\nDifference: ${difference}` +
   `\nProduct: ${product}` +
   `\nQuotient: ${quotient}`;


// Favorite food
let favoriteFood = "pizza";
console.log("My favorite food is " + favoriteFood);
document.getElementById("output").innerText += `\nMy favorite food is ${favoriteFood}.`;


// Part C - Practice Problems


// 6. Swap variables
let x = 7;
let y = 3;
console.log("Before swap: x =", x, "y =", y);
[x, y] = [y, x]; // swap using array destructuring
console.log("After swap: x =", x, "y =", y);
document.getElementById("output").innerText += `\n\nBefore swap: x=${7}, y=${3}\nAfter swap: x=${x}, y=${y}`;


// 7. Join strings to make fullName
let firstName = "Anika";
let lastName = "Seksaria";
let fullName = firstName + " " + lastName;
console.log("Full name:", fullName);
document.getElementById("output").innerText += `\nFull name: ${fullName}`;


// 8. Convert Celsius to Fahrenheit
let C = 25;
let F = (C * 9/5) + 32;
console.log(C + "°C is " + F + "°F");
document.getElementById("output").innerText += `\n${C}°C is ${F}°F`;


// 9. Pass/Fail based on score
let score = 85;
let result = score >= 50 ? "Pass" : "Fail";
console.log("Score:", score, "Result:", result);
document.getElementById("output").innerText += `\nScore: ${score}, Result: ${result}`;


// 10. Prompt for name and age
let userName = "Anika";
let userAge = "14";
console.log(`Hello ${userName}, you are ${userAge} years old.`);
document.getElementById("output").innerText += `\nHello ${userName}, you are ${userAge} years old.`;


// 11. Using 5 variables for a fun message
let name11 = "Anika";
let age11 = 15;
let day11 = "birthday";
let comingDays11 = 123;
let compliment11 = "congrats";


let message11 = `Hello ${name11}, your ${day11} is in ${comingDays11} days! You will then be ${age11} years old, ${compliment11}!`;


// Print to console
console.log(message11);


// Print to page output
document.getElementById("output").innerText += `\n${message11}`;




   })();
 </script>
</body>
</html>




```


<html>
<body>
 <h2>Homework Output</h2>
 <div id="output"></div>


 <script>
   document.getElementById("output").innerText = ""; // Clear output
   (() => {


     // Part A - Creating Variables
     let name = "Anika";
     const age = 14;
     let city = "San Diego";


     // Part B - Build sentences
     let line1 = "My name is " + name;
     let line2 = "I am " + age + " years old and I live in " + city;


     // Part A - number 3
     let isStudent = true; // or false if you’re not a student
     // Print to console
     console.log("Am I a student? " + isStudent);
     // Add it to the page output
     document.getElementById("output").innerText += "\nAm I a student? " + isStudent;




     // Print both lines to output box
     document.getElementById("output").innerText = line1 + "\n" + line2;


     document.getElementById("output").innerText = line1 + "\n" + line2;
document.getElementById("output").innerText += "\nAm I a student? " + isStudent;


// Part B - Numbers & Strings
let num1 = 10;
let num2 = 5;


// Calculate sum, difference, product, quotient
let sum = num1 + num2;
let difference = num1 - num2;
let product = num1 * num2;
let quotient = num1 / num2;


// Print to console
console.log("Sum:", sum);
console.log("Difference:", difference);
console.log("Product:", product);
console.log("Quotient:", quotient);


// Print to page output
document.getElementById("output").innerText +=
   `\n\nSum: ${sum}` +
   `\nDifference: ${difference}` +
   `\nProduct: ${product}` +
   `\nQuotient: ${quotient}`;


// Favorite food
let favoriteFood = "pizza";
console.log("My favorite food is " + favoriteFood);
document.getElementById("output").innerText += `\nMy favorite food is ${favoriteFood}.`;


// Part C - Practice Problems


// 6. Swap variables
let x = 7;
let y = 3;
console.log("Before swap: x =", x, "y =", y);
[x, y] = [y, x]; // swap using array destructuring
console.log("After swap: x =", x, "y =", y);
document.getElementById("output").innerText += `\n\nBefore swap: x=${7}, y=${3}\nAfter swap: x=${x}, y=${y}`;


// 7. Join strings to make fullName
let firstName = "Anika";
let lastName = "Seksaria";
let fullName = firstName + " " + lastName;
console.log("Full name:", fullName);
document.getElementById("output").innerText += `\nFull name: ${fullName}`;


// 8. Convert Celsius to Fahrenheit
let C = 25;
let F = (C * 9/5) + 32;
console.log(C + "°C is " + F + "°F");
document.getElementById("output").innerText += `\n${C}°C is ${F}°F`;


// 9. Pass/Fail based on score
let score = 85;
let result = score >= 50 ? "Pass" : "Fail";
console.log("Score:", score, "Result:", result);
document.getElementById("output").innerText += `\nScore: ${score}, Result: ${result}`;


// 10. Prompt for name and age
let userName = "Anika";
let userAge = "14";
console.log(`Hello ${userName}, you are ${userAge} years old.`);
document.getElementById("output").innerText += `\nHello ${userName}, you are ${userAge} years old.`;


// 11. Using 5 variables for a fun message
let name11 = "Anika";
let age11 = 15;
let day11 = "birthday";
let comingDays11 = 123;
let compliment11 = "congrats";


let message11 = `Hello ${name11}, your ${day11} is in ${comingDays11} days! You will then be ${age11} years old, ${compliment11}!`;


// Print to console
console.log(message11);


// Print to page output
document.getElementById("output").innerText += `\n${message11}`;




   })();
 </script>
</body>
</html>






# Submission

You will submit the link to your homework on a web page in the below form.  
If you are unable to get your homework accessible from the website, you can upload this Jupyter notebook to the form.

**IMPORTANT: If uploading, please name this Jupyter notebook in this format: [FirstName][LastName]_vars_hw.ipynb**
Example: SamarthHande_hw.ipynb

<https://forms.gle/UBDFErZpKpTApWap8>

Requirements for homework:
1. Parts A, B, and C should be completed. You will get .3 points for each question completed.
2. Up to 0.03 extra points will be given to code that demonstrates exceptional creativity and comprehension.
