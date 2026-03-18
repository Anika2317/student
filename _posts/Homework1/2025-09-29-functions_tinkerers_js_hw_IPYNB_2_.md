---
layout: post
title: Functions Homework
description: Functions Homework
categories: ['Javascript', 'Homework']
permalink: /Functions
author: Tinkerers
---

<hr>

<style>
.glowing-text {
  color: #fff; /* Set the text color to white or a light color for better contrast */
  text-shadow: 0 0 10px #8a2be2, /* Purple glow */
               0 0 20px #8a2be2, /* Deeper purple glow */
               0 0 30px #4169e1, /* Blue glow */
               0 0 40px #4169e1; /* Deeper blue glow */

  font-weight: bold;
}
</style>

<h2 class="glowing-text">🍿 POPCORN HACK NO. 1 🍿</h2>

**NOTE: Do all this in the provided code cell below**

Oh no! Billy Bob Joe just went to Asia for vacation!  
However, he accidentally set the heating to 80 degrees Celsius, which is around 176 degrees Fahrenheight.

<img src="https://a.pinatafarm.com/1920x1076/2d3cc55d2a/sweating-jordan-peele.jpg" 
     style="width: 25%; height: auto;">

Help Billy Bob Joe by making a function to help with the conversion from F to C! (So that he doesn't spontaneously combust from setting his thermometer to 978 degrees Fahrenheight or something)

1. Define a function named toCelsius() that takes a parameter called "degrees_fh"
  
2. Write logic to make the function return the converted number of degrees in Celsius

Use this image to help you:

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwaeck7wnmhYfZGpg-SgoLywXhClBwDATR0g&s">

3. Call the function whenever the button is pressed with the values inputted by the user as input, and save the results to a variable.

4. `console.log()` the variable each time after calculating it, and append it to the end of the DOM.

Side note: `console.log()` is a function that comes predefined in JavaScript! You've almost definitely used functions before, even if you didn't know about them.

<hr>


```python
%%html

<p>Fahrenheit to Celsius Converter</p>

<input type="number" id="inputField" placeholder="Enter degrees (F)">
<button id="calculateButton">Calculate</button>

<div id="output1">Your results will appear here.</div>

<script>

  (() => {

    const button = document.getElementById("calculateButton");
    const input = document.getElementById("inputField");
    const output = document.getElementById("output1");

    // ^^ DO NOT MODIFY ANY ABOVE CODE ^^

    // 1. Define the function using c = (f - 32) / 1.8
    function toCelsius(degrees_fh) {
      return (degrees_fh - 32) / 1.8;
    }

    button.addEventListener("click", () => {

      // 2.user input and convert to number
      const fahrenheitValue = Number(input.value);

      // 3. Call the function
      const result = toCelsius(fahrenheitValue);

      // 4. Log result to console
      console.log(result);

      // 5. Add result to the DOM
      output.innerText += "\n" + fahrenheitValue + "°F = " + result.toFixed(2) + "°C";

    // vv DO NOT MODIFY ANY BELOW CODE vv
    });

  })();

</script>

```



<p>Fahrenheit to Celsius Converter</p>

<input type="number" id="inputField" placeholder="Enter degrees (F)">
<button id="calculateButton">Calculate</button>

<div id="output1">Your results will appear here.</div>

<script>

  (() => {

    const button = document.getElementById("calculateButton");
    const input = document.getElementById("inputField");
    const output = document.getElementById("output1");

    // ^^ DO NOT MODIFY ANY ABOVE CODE ^^

    // 1. Define the function using c = (f - 32) / 1.8
    function toCelsius(degrees_fh) {
      return (degrees_fh - 32) / 1.8;
    }

    button.addEventListener("click", () => {

      // 2. Get user input and convert to number
      const fahrenheitValue = Number(input.value);

      // 3. Call the function
      const result = toCelsius(fahrenheitValue);

      // 4. Log result to console
      console.log(result);

      // 5. Add result to the DOM
      output.innerText += "\n" + fahrenheitValue + "°F = " + result.toFixed(2) + "°C";

    // vv DO NOT MODIFY ANY BELOW CODE vv
    });

  })();

</script>




<style>
.glowing-text {
  color: #fff; /* Set the text color to white or a light color for better contrast */
  text-shadow: 0 0 10px #8a2be2, /* Purple glow */
               0 0 20px #8a2be2, /* Deeper purple glow */
               0 0 30px #4169e1, /* Blue glow */
               0 0 40px #4169e1; /* Deeper blue glow */

  font-weight: bold;
}
</style>

<h2 class="glowing-text">🍿 POPCORN HACK NO. 2 🍿</h2>

By the time we reach this lesson, we should have covered Loops/Iteration. Write a function called `findMax()` that does the following:

1. Takes one argument which is an array of integer numbers
2. Make the function loop through the array and return the largest element
3. Make the function write the results to DOM and to console:
  1. `console.log(_______)` writes to console
  2. `output.innerText += "\n" + ______` writes to DOM
4. Call the function three times with these arrays as input
   1. `[1, 2, 3, 4, 4, 4, 5, 6, 8, 4, 1, 7]`
   2. `[1]`
   3. `[97883, 981, 81283, 987213, 1, -391]`


```python
%%html


<div id="phack2">Your results will appear here:</div>

<script>

    (() => {

        const output = document.getElementById("phack2");
     
        // ^^ DO NOT MODIFY ABOVE CODE ^^
        
        // Write all of your code here!

    function findMax(arr) {
        let max = arr[0]; // start with the first element

        for (let i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        console.log("Max value:", max);
        output.innerText += "\nMax value: " + max;

        return max;
    }

    // Call the function three times with the given arrays
    findMax([1, 2, 3, 4, 4, 4, 5, 6, 8, 4, 1, 7]);
    findMax([1]);
    findMax([97883, 981, 81283, 987213, 1, -391]);

        // vv DO NOT MODIFY BELOW CODE vv
        
    })();

</script>
```




<div id="phack2">Your results will appear here:</div>

<script>

    (() => {

        const output = document.getElementById("phack2");

        // ^^ DO NOT MODIFY ABOVE CODE ^^

        // Write all of your code here!

    function findMax(arr) {
        let max = arr[0]; // start with the first element

        for (let i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }

        console.log("Max value:", max);
        output.innerText += "\nMax value: " + max;

        return max;
    }

    // Call the function three times with the given arrays
    findMax([1, 2, 3, 4, 4, 4, 5, 6, 8, 4, 1, 7]);
    findMax([1]);
    findMax([97883, 981, 81283, 987213, 1, -391]);

        // vv DO NOT MODIFY BELOW CODE vv

    })();

</script>




<style>
.glowing-text {
  color: #fff; /* Set the text color to white or a light color for better contrast */
  text-shadow: 0 0 10px #8a2be2, /* Purple glow */
               0 0 20px #8a2be2, /* Deeper purple glow */
               0 0 30px #4169e1, /* Blue glow */
               0 0 40px #4169e1; /* Deeper blue glow */

  font-weight: bold;
}
</style>

<h2 class="glowing-text">Homework</h2>


**Now that you have completed your function lesson, you will be doing some homework to apply the concepts you learned.**

<hr>

**Homework problem 1:**

Make a function that uses recursion to calculate the Nth Fibonacci number, given N as a parameter.

You just need to write the code in `fibonacci()`. The rest of the code to handle input/output is already written for you.



```python
%%html

<p>Fibonacci Number Calculator</p>

<input type="number" id="hw1input" placeholder="Enter the Nth number to find:">
<button id="hw1button">Calculate</button>
<div id="hw1output">Your results will appear here.</div>

<script>

(() => {

    const button = document.getElementById("hw1button");
    const input = document.getElementById("hw1input");
    const output = document.getElementById("hw1output");

    // ^^ DO NOT MODIFY ANY ABOVE CODE ^^

    // Recursive Fibonacci function
    function fibonacci(n) {
        if (n <= 0) return 0;   // Base case 0
        if (n === 1) return 1;  // Base case 1
        return fibonacci(n - 1) + fibonacci(n - 2); // Recursive step
    }

    // vv DO NOT MODIFY ANY BELOW CODE vv

    let result;
    let inpval;

    button.addEventListener("click", () => {

        inpval = Number(input.value);
        result = fibonacci(inpval);

        // Log the result to console
        console.log("Fibonacci Number #" + inpval + " is " + result);

        // Add the result to the end of DOM:
        output.innerText += "\n" + "Fibonacci Number #" + inpval + " is " + result;

    });

})();
</script>

```



<p>Fibonacci Number Calculator</p>

<input type="number" id="hw1input" placeholder="Enter the Nth number to find:">
<button id="hw1button">Calculate</button>
<div id="hw1output">Your results will appear here.</div>

<script>

(() => {

    const button = document.getElementById("hw1button");
    const input = document.getElementById("hw1input");
    const output = document.getElementById("hw1output");

    // ^^ DO NOT MODIFY ANY ABOVE CODE ^^

    // Recursive Fibonacci function
    function fibonacci(n) {
        if (n <= 0) return 0;   // Base case 0
        if (n === 1) return 1;  // Base case 1
        return fibonacci(n - 1) + fibonacci(n - 2); // Recursive step
    }

    // vv DO NOT MODIFY ANY BELOW CODE vv

    let result;
    let inpval;

    button.addEventListener("click", () => {

        inpval = Number(input.value);
        result = fibonacci(inpval);

        // Log the result to console
        console.log("Fibonacci Number #" + inpval + " is " + result);

        // Add the result to the end of DOM:
        output.innerText += "\n" + "Fibonacci Number #" + inpval + " is " + result;

    });

})();
</script>



**Homework problem 2:**

Make a function called `decribe()` that describes a person's attributes. It should take parameters `age`, `gender`, `job`, `height` and output something along the lines of "Hello! I am [age] years old and [gender]. My job is [job] and I'm [height] feet tall."

Y'know what? I don't feel like writing the code to handle output, so I'll leave that to you :). Take input from `ageInput.value`, e.g. `let x = ageInput.value`

After you're done, call the function with values of your choosing any and write its output to DOM and to the console.
Write to DOM using `output.innerText = _______` or `output.innerText += ____________`.




```python
%%html

<p>Person Describer</p>

<input type="number" id="hw2age" placeholder="Age">
<input type="text" id="hw2gender" placeholder="Gender">
<input type="text" id="hw2job" placeholder="Job">
<input type="number" id="hw2height" placeholder="Height (inches)">
<button id="hw2button">Describe Me!</button>

<div id="hw2output">Your results will appear here.</div>

<script>
(() => {
  const output = document.getElementById("hw2output");

  const ageInput = document.getElementById("hw2age");
  const genderInput = document.getElementById("hw2gender");
  const jobInput = document.getElementById("hw2job");
  const heightInput = document.getElementById("hw2height");
  const button = document.getElementById("hw2button");

  function describe(age, gender, job, height) {
    return `Hello! I am ${age} years old and ${gender}. My job is ${job} and I'm ${height} inches tall.`;
  }

  button.addEventListener("click", () => {
    const age = ageInput.value;
    const gender = genderInput.value;
    const job = jobInput.value;
    const height = heightInput.value;

    const message = describe(age, gender, job, height);

    console.log(message);
    output.innerHTML += "<br>" + message;
  });
})();
</script>

```



<p>Person Describer</p>

<input type="number" id="hw2age" placeholder="Age">
<input type="text" id="hw2gender" placeholder="Gender">
<input type="text" id="hw2job" placeholder="Job">
<input type="number" id="hw2height" placeholder="Height (inches)">
<button id="hw2button">Describe Me!</button>

<div id="hw2output">Your results will appear here.</div>

<script>
(() => {
  const output = document.getElementById("hw2output");

  const ageInput = document.getElementById("hw2age");
  const genderInput = document.getElementById("hw2gender");
  const jobInput = document.getElementById("hw2job");
  const heightInput = document.getElementById("hw2height");
  const button = document.getElementById("hw2button");

  function describe(age, gender, job, height) {
    return `Hello! I am ${age} years old and ${gender}. My job is ${job} and I'm ${height} inches tall.`;
  }

  button.addEventListener("click", () => {
    const age = ageInput.value;
    const gender = genderInput.value;
    const job = jobInput.value;
    const height = heightInput.value;

    const message = describe(age, gender, job, height);

    console.log(message);
    output.innerHTML += "<br>" + message;
  });
})();
</script>



## Submission

Submit the **deployed homework** on your site on the [master grading spreadsheet](https://docs.google.com/spreadsheets/d/1shZckk5fdkjfLZLazXcmydeHIgIjDCYEmR_SmBhWzJo/edit?gid=1726663250#gid=1726663250) next to your name.

E.g. If my name was "John Brown", I would navigate to the Functions tab, find the cell saying "John Brown", and put the link in the corresponding cell.


Requirements for homework:
1. Popcorn hacks: 0.2 points each, for a total of 0.4 points
2. Homework problems (1 and 2): 0.25 points each, for a total of 0.9 points
3. Up to 0.03 extra points will be given to code that demonstrates exceptional creativity and comprehension. If you really want to get these .03 points, add a new creative feature to either popcorn hack or either homework problem!
