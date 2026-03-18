---
layout: post
title: Array Homework
description: Array Homework
categories: ['Javascript', 'Homework']
permalink: /UnderstandArray
author: Coders
---

## Understanding Arrays

Arrays are those super useful containers that let programmers keep a bunch of related stuff together in one place. If variables are like single boxes, think of arrays as those shoe organizers where each slot holds something different.

### What's an Array?

At its core, an array is just:
- A collection of values (could be numbers, text, whatever)
- Organized in a sequence so you can find things easily
- Perfect when you need to work with multiple related items

Many beginners get confused about why arrays are even necessary. But try keeping track of 20 student scores with individual variables... yeah, not fun. Arrays make this kind of thing way easier.

### How Arrays Work

Arrays have a few key features that make them useful:

1. **Index numbers** - Each item has a position (starting at 0, which trips everyone up at first!)
2. **Order matters** - Items stay in the sequence you put them in
3. **Dynamic size** - Most languages let you add or remove items as needed
4. **Versatility** - Can hold pretty much any type of data

### Picturing an Array

Think of it like a row of mailboxes:

```
Index:   0      1      2       3        4
       ┌────┐ ┌────┐ ┌────┐ ┌────┐  ┌────┐
Array: │ 10 │ │ 20 │ │ 30 │ │ 40 │  │ 50 │
       └────┘ └────┘ └────┘ └────┘  └────┘
```

### Working With Arrays in JavaScript

#### Creating Arrays
```javascript
// Empty array - for when you want to fill it later
let emptyArray = [];

// Array with values ready to go
let numbers = [10, 20, 30, 40, 50];

// Mix and match different types (though usually better to keep similar types together)
let stuff = ["apple", 42, true, { name: "Alex" }];
```

#### Getting Items Out
```javascript
let fruits = ["apple", "banana", "cherry", "date"];

// Get the first fruit
console.log(fruits[0]); // "apple"

// Get the third fruit
console.log(fruits[2]); // "cherry"
```

#### Changing Things Around
```javascript
let colors = ["red", "green", "blue"];

// Change the middle color
colors[1] = "yellow";
console.log(colors); // ["red", "yellow", "blue"]

// Add a new color at the end
colors.push("purple");
console.log(colors); // ["red", "yellow", "blue", "purple"]

// Take away the last color
colors.pop();
console.log(colors); // ["red", "yellow", "blue"]
```

#### How Many Items?
```javascript
let team = ["Alice", "Bob", "Charlie", "David"];
console.log(team.length); // 4
```

#### Handy Array Methods

Here are some methods that are commonly used:

| Method | What it does | Example |
|--------|-------------|---------|
| push() | Adds to end | `array.push(item)` |
| pop() | Removes from end | `array.pop()` |
| unshift() | Adds to start | `array.unshift(item)` |
| shift() | Removes from start | `array.shift()` |
| slice() | Grabs a section | `array.slice(1,3)` |
| join() | Makes a string | `array.join(", ")` |

### Why Arrays Are Great

- **Saves time**: No need for 50 different variable names
- **Makes sense**: Keeps related data together where it belongs
- **Easy access**: Grab any item whenever you need it
- **Loops**: Perfect for doing the same operation on multiple items
- **Flexible**: Need to add more? No problem!

### Real Stuff You'd Store in Arrays

1. **Shopping list**: `["milk", "eggs", "bread", "coffee"]`
2. **Test scores**: `[95, 82, 78, 90, 88]`
3. **User info**: `["Sarah", 25, "Web Developer", true]`
4. **Game coordinates**: `[[2,3], [4,1], [7,5], [0,2]]`

Once programmers get comfortable with arrays, they use them everywhere!

## Time to Practice: Array Challenges!

Now it's time to put the concepts into practice! These challenges will help students get comfortable with arrays.

<div class="challenge-card">

### Hack #1: The Food Array

For this first challenge, students will work with something everyone enjoys - food! The task is to create a list of favorite foods and manipulate the array.

**What to do**:

1. **Make a food list**: 
   - Create a variable called `favoriteFoods`
   - Put 5 favorite foods in there as strings
   - For example: `let favoriteFoods = ["pizza", "ice cream", "sushi", "tacos", "pasta"];`

2. **Find a specific food**:
   - Get the first food from the list using its index
   - Print it out with console.log()
   - Remember that arrays start counting at 0, not 1

3. **Change something**:
   - Change the third food in the array
   - Replace it with something else using: `favoriteFoods[2] = "something else";`

4. **Add a dessert**:
   - Use push() to add one more food to the end
   - Example: `favoriteFoods.push("chocolate");`

5. **Count the foods**:
   - Check how many foods are now in the list
   - Use the length property and print it out

6. **See the results**:
   - Print out the whole array to see all the changes
   - Try: `console.log("My favorite foods are now: ", favoriteFoods);`

**Expected output**: The code should display the first food, then the new total number of foods (should be 6), and finally the complete updated food list.

</div>

This can be completed in the next code cell. Remember that making mistakes is part of the learning process!


```python
// Starting with a food list
let favoriteFoods = ["pasta", "pizza", "burgers", "salads", "tacos"];

console.log("First food:", favoriteFoods[0]);

favoriteFoods[2] = "sushi";

favoriteFoods.push("ice cream");

console.log("New length of list:", favoriteFoods.length);

console.log("All favorite foods:", favoriteFoods);

favoriteFoods.unshift("pancakes");
console.log("After adding one at the beginning:", favoriteFoods);
```

    First food: pasta
    New length of list: 6
    All favorite foods: ['pasta', 'pizza', 'sushi', 'salads', 'tacos', 'ice cream']
    After adding one at the beginning: ['pancakes', 'pasta', 'pizza', 'sushi', 'salads', 'tacos', 'ice cream']



```python

```

<div class="tip-box">

### Bonus Challenge Explained

The bonus challenge asks students to add a new food at the FRONT of the list instead of the end. This requires the `unshift()` method.

**How `unshift()` works**:
- It adds elements to the beginning of an array
- It's similar to cutting in line at a movie theater
- It returns how many items are now in the array

**How it differs from `push()`:**
- `push()` adds to the end (like joining the back of a line)
- `unshift()` adds to the beginning (like cutting to the front)

**Example code:**
```javascript
// Starting with a food list
console.log(favoriteFoods); // ["pizza", "ice cream", "burgers", "tacos", "pasta", "chocolate"]

// Adding "waffles" to the beginning
favoriteFoods.unshift("waffles");

// Result
console.log(favoriteFoods); // ["waffles", "pizza", "ice cream", "burgers", "tacos", "pasta", "chocolate"]
```

**What happens behind the scenes:**
When an element is added to the front, all existing elements shift right to make room:

**BEFORE:**

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
|-------|-------|----------|---------|--------|---------|----------|
| **Food** | pizza | ice cream | burgers | tacos | pasta | chocolate |

**AFTER:**

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|-------|--------|-------|----------|---------|--------|---------|----------|
| **Food** | waffles | pizza | ice cream | burgers | tacos | pasta | chocolate |
| **What happened** | NEW! | moved | moved | moved | moved | moved | moved |

Notice how everything shifts over by one position. This is why adding to the front can be slower than adding to the end when dealing with large arrays.

**Steps to complete:**
1. Use `unshift()` to add a breakfast food to the front
2. Print the list again to see the change
3. Check the length again (should be 7 if all previous steps were followed)

**Question to consider:** What happens to the indices of the existing elements after using `unshift()`?

</div>


```python
let favoriteFoods = ["pizza", "ice cream", "burgers", "tacos", "pasta", "chocolate"];
console.log("Before adding:", favoriteFoods);

// Add "waffles" to the beginning
favoriteFoods.unshift("waffles");

console.log("After adding:", favoriteFoods);
console.log("New length:", favoriteFoods.length);
```

    Before adding: ['pizza', 'ice cream', 'burgers', 'tacos', 'pasta', 'chocolate']
    After adding: ['waffles', 'pizza', 'ice cream', 'burgers', 'tacos', 'pasta', 'chocolate']
    New length: 7


<div class="challenge-card">

### Hack #2: The Temperature Array

For the second challenge, students will work with a set of temperature data. This involves tracking daily temperatures over a week.

**What to do**:

1. **Create a temperature array**:
   - Create a variable called `weekTemps`
   - Add 7 temperature values for a week (e.g., 72, 68, 74, 80, 76, 72, 67)

2. **Find specific days**:
   - Print out the temperature for Monday (index 0)
   - Print out the temperature for Friday (index 4)

3. **Find the weekly average**:
   - Calculate the average of all temperatures
   - Hint: Add them all up and divide by 7
   - You can do this with individual variables, a loop, or array methods

4. **Find the hottest day**:
   - Find the highest temperature in the array
   - Try using JavaScript's built-in `Math.max()` with the spread operator: `Math.max(...weekTemps)`
   - Print the result

5. **Temperature check**:
   - Use an if/else statement to check if any day was above 80 degrees
   - If yes, print "It was hot this week!"
   - If no, print "It was mild this week."

**Expected output**: The code should display the Monday and Friday temperatures, the average temperature (with one decimal place if needed), the highest temperature, and the temperature message.

This challenge introduces conditional logic along with array manipulation.

Remember that for the average temperature, you'll want to add all values and divide by the length of the array.

</div>


```python
// Hack #2: The Temperature Array

let weekTemps = [72, 68, 74, 80, 76, 72, 67];

// 2. Find specific days

console.log("Monday temperature:", weekTemps[0]);

console.log("Friday temperature:", weekTemps[4]);

// 3. Find the weekly average

let sum = weekTemps.reduce((a, b) => a + b, 0);

let averageTemp = sum / weekTemps.length;

console.log("Average temperature:", Math.round(averageTemp * 10) / 10);

// 4. Find the hottest day

let hottestTemp = Math.max(...weekTemps);

console.log("Hottest temperature:", hottestTemp);

// 5. Temperature check

let hasHotDay = weekTemps.some(temp => temp > 80);

if (hasHotDay) {

    console.log("It was hot this week!");

} else {

    console.log("It was mild this week.");

}
```

    Monday temperature: 72
    Friday temperature: 76
    Average temperature: 72.7
    Hottest temperature: 80
    It was mild this week.


<div class="tip-box">

### Need Help with Hack #2? Some Hints...

Instead of providing complete solutions (which wouldn't help with learning), here are some hints to guide thinking:

**Finding the average temperature**:
- The formula is: average = sum of all values ÷ number of values
- Begin with total = 0, then add each temperature one by one
- The number of values can be found with weekTemps.length
- The division should happen AFTER the loop (not inside it)

**Using Math.max() with an array**:
- Math.max() normally takes individual arguments like Math.max(1, 2, 3)
- The spread operator (...) expands an array into individual arguments
- For example: Math.max(...[1, 2, 3]) is the same as Math.max(1, 2, 3)
- This is an elegant way to find the highest value in an array

**Checking if any temperature was above 80**:
- You'll need to loop through the array
- Use a variable to track if you've found a hot day
- If you find any temperature > 80, set the variable to true
- After the loop, check the variable to determine which message to print

**Problem-Solving Strategy**:
When stuck on a programming problem, breaking it down often helps:
1. Identify what information is needed
2. Set up the necessary variables
3. Process each value systematically
4. Perform the required calculation or check
5. Display the result

Remember that learning to code takes time. Even experienced programmers frequently need to look things up and learn through trial and error.

</div>

<div class="recap-section">

## Well Done!

Completing these challenges is an accomplishment! Arrays might seem simple initially, but they're actually fundamental tools in programming. Nearly every application or website relies on arrays somewhere in its codebase.

### Quick Recap

- Arrays store multiple related values together
- Elements can be accessed using their position number (index)
- Arrays can grow or shrink as needed
- Loops can process each array element efficiently
- Common operations include adding, removing, and finding items

</div>

<div class="tip-box">

## Tips for Working Through These Challenges

Beginners shouldn't worry if these concepts seem challenging at first. Here are some suggested approaches:

### For Beginners

1. **Understand the code first:** Read through the provided code to understand what each line does. If something is confusing, looking it up or asking questions can help.
2. **Run the code and observe:** Seeing the output often helps clarify how things work.
3. **Make experimental changes:** Learning often happens through experimentation. Changing variable names or values and observing the effects can be highly educational.
4. **Progress gradually:** Master the basics before tackling bonus challenges.

</div>
