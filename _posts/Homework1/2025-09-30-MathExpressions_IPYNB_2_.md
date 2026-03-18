---
layout: post
title: Math Expressions
description: Math Expressions Homework
categories: ['Javascript', 'Homework']
permalink: /Math
author: Penguins
---

# Penguins JS Lessons

<a href="https://github.com/Comp-Sci-Team/js-lesson_pages/blob/main/_notebooks/CSSE/JavaScriptLessons/Mathematic_Expressions/2025-09-30-penguins-math-exp-hw.ipynb" download><b>Download Homework</b></a> <br/>
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfwgZR0QYAg_uYuZ7XqqEm-xlU0-gZFE2dtgnKEe5kH7Yp0Vg/viewform?usp=dialog"><b>Submission Google Form for Homework</b></a>

## **Mathematical Expressions Homework**
In order to learn this subject of programming well, you have to practice:

> Popcorn hack 1: operations with variables

> Popcorn hack 2: Make 2 variables `x`, and `y`. Compute 3 different operations and log it into the console with console.log();

> Final Task: Build a system of functions that represent different mathematical expressions. Each of these functions will perform a different mathematical operation(ex: add, subtract). Make at least 5 of these different functions. 

---

## <b>Popcorn Hack 1 (Progress Check)</b>

<b>Part 1:</b><br/>
In the javascript node below, make 2 variables, `num1` set to 6 and `num2` set to 3, then write the equation `(num1 * num2) + (num1 / 2)`.

The output should be 21.<br/>
<br/>
<b>Part 2:</b><br/>
Next, keeping the same variables, add a new variable called `total` that is equal to the equation `num1 / num2 + 2 ** 3`, and this time make the equation<br/><br/> `(total + 15) - numb1 ** 2 / 4` <br/><br/>

Write this code below:


```python
num1 = 6
num2 = 3

part1_result = (num1 * num2) + (num1 / 2)
print("Part 1 Answer:", part1_result)  # Output: 21.0

total = (num1 / num2) + 2 ** 3  # 6 / 3 + 8 = 2 + 8 = 10

part2_result = (total + 15) - (num1 ** 2 / 4)  # (10 + 15) - (36 / 4) = 16
print("Part 2 Answer:", part2_result)  # Output: 16.0

```

    Part 1 Answer: 21.0
    Part 2 Answer: 16.0


---

## Popcorn Hack 2 (Progress check):

Create 2 variables `x` and `y`. With the output area below, provide 3 different operators used with the 2 variables<br/>(`ex: let sum = x + y;`)<br/> and fill in the output with a sentence that provides all three operators and their respective answer.


```python
%%html

<h3>Popcorn hack 2 output</h3>
<div id="homework1"></div>
<script>    
(() => {
    // Your variables go here
    let x = 23
    let y = 17

	// put your operations here:
	// feel free to do any operation and change the names of the variables
	let operation1 = x + y
	let operation2 = x * y
	let operation3 = x - y

    // Put the answer for the 3 operators in this DOM element
    document.getElementById("homework1").innerText = operation1 + operation2+ operation3
})();
</script>
```



<h3>Popcorn hack 2 output</h3>
<div id="homework1"></div>
<script>    
(() => {
    // Your variables go here
    let x = 23
    let y = 17

	// put your operations here:
	// feel free to do any operation and change the names of the variables
	let operation1 = x + y
	let operation2 = x * y
	let operation3 = x - y

    // Put the answer for the 3 operators in this DOM element
    document.getElementById("homework1").innerText = operation1 + operation2+ operation3
})();
</script>



---

## Final Task:

1. Make 5 different functions, each with different operators/expressions:

- Addition
- Subtraction
- Multiplication
- Exponential
- Modulus

2. Be able to use the functions as well as <code>document.getElementById</code> to make the buttons output the result.

3. Have fun! Mess around with different variables with different values, and maybe see if you can make any complex equations like the ones you're learning in your math class. The end objective is for you to be able to use and understand math expressions.


### Example function:

```
function add(a, b)
{
	return a + b;
}
```

### Some ideas you can use:
- Multiply Function
- Square root function
- Cube root function

---


Now that you have seen the example, you will start writing your custom functions in the html code block below: <br>
<u> Make sure to follow each comment on where to write your code, don't modify any existing code. </u>
<br><br>


```python
%%html

<h2>Function outputs:</h2>

<!-- Buttons and output divs -->
<button type="button" onclick="Add(4,5)">Function Output 1</button>
<div id="functionOutput1"></div>
<br>

<button type="button" onclick="Expression()">Function Output 2</button>
<div id="functionOutput2"></div>
<br>

<button type="button" onclick="Multiply(3,7)">Function Output 3</button>
<div id="functionOutput3"></div>
<br>

<button type="button" onclick="Subtract(10,6)">Function Output 4</button>
<div id="functionOutput4"></div>
<br>

<button type="button" onclick="Divide(8,12)">Function Output 5</button>
<div id="functionOutput5"></div>
<br>

<script>
	// Function 1: Add two numbers
	function Add(a, b) {
		let result = a + b;
		document.getElementById("functionOutput1").innerText = result;
	}

	// Function 2: Expression example
	function Expression() {
		let result = (5 * 3) + 2; // Example calculation
		document.getElementById("functionOutput2").innerText = result;
	}

	// Function 3: Multiply two numbers
	function Multiply(a, b) {
		let result = a * b;
		document.getElementById("functionOutput3").innerText = result;
	}

	// Function 4: Subtract two numbers
	function Subtract(a, b) {
		let result = a - b;
		document.getElementById("functionOutput4").innerText = result;
	}

	// Function 5: Divide two numbers
	function Divide(a, b) {
		let result = a / b;
		document.getElementById("functionOutput5").innerText = result;
	}
</script>

```



<h2>Function outputs:</h2>

<!-- Buttons and output divs -->
<button type="button" onclick="Add(4,5)">Function Output 1</button>
<div id="functionOutput1"></div>
<br>

<button type="button" onclick="Expression()">Function Output 2</button>
<div id="functionOutput2"></div>
<br>

<button type="button" onclick="Multiply(3,7)">Function Output 3</button>
<div id="functionOutput3"></div>
<br>

<button type="button" onclick="Subtract(10,6)">Function Output 4</button>
<div id="functionOutput4"></div>
<br>

<button type="button" onclick="Divide(8,12)">Function Output 5</button>
<div id="functionOutput5"></div>
<br>

<script>
	// Function 1: Add two numbers
	function Add(a, b) {
		let result = a + b;
		document.getElementById("functionOutput1").innerText = result;
	}

	// Function 2: Expression example
	function Expression() {
		let result = (5 * 3) + 2; // Example calculation
		document.getElementById("functionOutput2").innerText = result;
	}

	// Function 3: Multiply two numbers
	function Multiply(a, b) {
		let result = a * b;
		document.getElementById("functionOutput3").innerText = result;
	}

	// Function 4: Subtract two numbers
	function Subtract(a, b) {
		let result = a - b;
		document.getElementById("functionOutput4").innerText = result;
	}

	// Function 5: Divide two numbers
	function Divide(a, b) {
		let result = a / b;
		document.getElementById("functionOutput5").innerText = result;
	}
</script>



---

<b>Grading</b>

Popcorn Hack 1: Completion gives 0.2 points.<br/><br/>
Popcorn Hack 2: Completion gives 0.3 points.<br/><br/>

Final Task: Completion gives 0.5 points. Max of 0.02 extra points from extra work relevant to the subject or finishing assignment in a way that shows exceptional comprehension of the lesson.

<br>
<b><u>Make sure to submit your homework deployed link onto the global homework submission google sheet</u><b>

<a href="https://docs.google.com/forms/d/e/1FAIpQLSfwgZR0QYAg_uYuZ7XqqEm-xlU0-gZFE2dtgnKEe5kH7Yp0Vg/viewform?usp=dialog"><b>Submission Google Form for Homework</b></a>
