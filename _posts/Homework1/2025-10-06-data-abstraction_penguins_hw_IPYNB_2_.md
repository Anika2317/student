---
layout: post
title: Data Abstraction Homework
description: Data Abstraction Homework
categories: ['Javascript', 'Homework']
permalink: /Penguins-homework
author: Penguins
---

# Penguins JS Lessons

<a href="https://github.com/Open-Coding-Society/pages/blob/main/_notebooks/CSSE/JavaScriptLessons/Data_Abstractions/2025-10-06-data-abstraction_penguins_hw.ipynb" download><b>Download Homework</b></a> <br/>
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfwgZR0QYAg_uYuZ7XqqEm-xlU0-gZFE2dtgnKEe5kH7Yp0Vg/viewform?usp=sharing&ouid=105179298243342263196"><b>Submission Google Form for Homework</b></a>

## **Data Abstraction Homework**
In order to learn this subject of programming well, you have to practice:

> Popcorn hack 1: Data Abstraction with functions

> Popcorn hack 2: Data abstraction with classes

> Final Task: Building a player system using classes and functions

---

## <b>Popcorn Hack 1 (Progress Check)</b>

Data abstraction with functions:

**Part 1:** Edit the `Account()` function to print out the username and password to the console using console.log().

**Part 2:** Edit the `ChangeUsername()` function to accept a `newUsername` parameter, then set the `username` variable to the `newUsername` parameter.

**Part 3:** Edit the `ChangePassword()` function to accept a `newPassword` parameter, then set the `password` variable to the `newPassword` parameter.

**Part 4:** Make the `Login()` function check if the parameters `_username` and `_password` are equal to the `username` and `password` variables, then print out if the login succeeded or failed using console.log().


```javascript
%%javascript

// Initial username and password
let username = "Giuseppe";
let password = "giuseppe_very_awesome_password";

// --- Part 1: Print username and password ---
function Account() { 
    console.log("Your username: " + username);
    console.log("Your password: " + password);
}

// --- Part 2: Change the username ---
function ChangeUsername(newUsername) {
    username = newUsername;
    console.log("Username changed to: " + username);
}

// --- Part 3: Change the password ---
function ChangePassword(newPassword) {
    password = newPassword;
    console.log("Password changed.");
}

// --- Part 4: Login check ---
function Login(_username, _password) {
    if (_username === username && _password === password) {
        console.log("Login successful!");
        return true;
    } else {
        console.log("Login failed!");
        return false;
    }
}

// --- Example Usage ---
Account(); // print initial username & password

ChangeUsername("Giuseppe123");
ChangePassword("new_super_secret");

Login("Giuseppe123", "wrong_password"); // should fail
Login("Giuseppe123", "new_super_secret"); // should succeed

```


    <IPython.core.display.Javascript object>


---

## <b>Popcorn Hack 2 (Progress Check)</b>

Use the examples provided in the lesson if you're stuck.

**Part 1:** Make a class named `House`

**Part 2:** Make a constructor for the `House` class with the parameters cost, age, and size

**Part 3:** Make an instance of the House class with the name myHouse and fill the parameters with any numbers you want.

Write your code down here:


```javascript
%%javascript

// --- Part 1 & 2: House class ---
class House {
    constructor(cost, age, size) {
        this.cost = cost;
        this.age = age;
        this.size = size;
    }
}

// --- Part 3: Create an instance ---
const myHouse = new House(250000, 10, 2000); // cost: 250k, age: 10 years, size: 2000 sqft

console.log("My house details:");
console.log("Cost: " + myHouse.cost);
console.log("Age: " + myHouse.age + " years");
console.log("Size: " + myHouse.size + " sqft");

```


    <IPython.core.display.Javascript object>


---

## <b>Final task</b>

**Part 1:** Create 2 variables in the constructor like this: this.variableName = something. 
These variables will be called: `this.positionX`, `this.velocityX`.

**Part 2:** Create 2 methods called `MoveLeft()` and `MoveRight()`, <br>
inside MoveLeft() set 'this.velocityX' to -200. <br>
inside MoveRight() set 'this.velocityX' to 200.

**Part 3:** Create a function called `UpdatePosition()`. Inside this function, add 'this.velocityX' to 'this.positionX'

**Part 4:** Call each method (MoveLeft(), MoveRight(), UpdatePosition() ), on the player object.


```javascript
%%javascript

// --- Part 1, 2, 3: Define the Player class ---
class Player {
    // Part 1: constructor with positionX and velocityX
    constructor() {
        this.positionX = 0;  // starting position
        this.velocityX = 0;  // starting velocity
    }

    // Part 2: MoveLeft and MoveRight methods
    MoveLeft() {
        this.velocityX = -200;
        console.log("Moving left, velocityX =", this.velocityX);
    }

    MoveRight() {
        this.velocityX = 200;
        console.log("Moving right, velocityX =", this.velocityX);
    }

    // Part 3: UpdatePosition method
    UpdatePosition() {
        this.positionX += this.velocityX;
        console.log("Updated positionX =", this.positionX);
    }
}

// --- Part 4: Create player instance and call methods ---
let player = new Player();

player.MoveRight();      // set velocity to 200
player.UpdatePosition(); // add velocity to position

player.MoveLeft();       // set velocity to -200
player.UpdatePosition(); // add velocity to position

```


    <IPython.core.display.Javascript object>


---

<b>Grading</b>

Popcorn Hack 1: Completion gives 0.2 points.<br/><br/>
Popcorn Hack 2: Completion gives 0.3 points.<br/><br/>

Final Task: Completion gives 0.5 points. Max of 0.02 extra points from extra work relevant to the subject or finishing assignment in a way that shows exceptional comprehension of the lesson.

<br>
<b><u>Make sure to submit your homework deployed link onto the global homework submission google sheet</u><b>

<a href="https://docs.google.com/forms/d/e/1FAIpQLSfwgZR0QYAg_uYuZ7XqqEm-xlU0-gZFE2dtgnKEe5kH7Yp0Vg/viewform?usp=sharing&ouid=105179298243342263196"><b>Submission Google Form for Homework</b></a>
