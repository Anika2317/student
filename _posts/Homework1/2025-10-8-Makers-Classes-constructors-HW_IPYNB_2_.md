---
layout: post
title: Classes and Constructors Homework
description: Classes and Constructors Homework
categories: ['Javascript', 'Homework']
permalink: /classes-constructors-HW
author: Makers
---

## <u>JavaScript Classes and Constructors Homework<u>
By now you should have a decent grasp of classes and constructors, and how to make and build one. The following exercises should help you solidify your understanding of classes and constructors in JavaScript.

## Popcorn Hack 1
1. The class TennisPlayer has been defined for you. Create a constructor with the arguements name, rank, and rankPoints.
2. Call the class with the arguments Novak Djokovic, 1, 16000. 
3. Add one or more of the following arguments to the initial constructor: age, tournamentsPlayed, titlesWon. Add this as part of the profile output.


```javascript
%%javascript

class TennisPlayer {
    constructor(name, rank, rankPoints) {
        this.name = name;
        this.rank = rank;
        this.rankPoints = rankPoints;
    }

    profile() {
        console.log("Hi my name is " + this.name + ", my rank is " + this.rank + " and I have " + this.rankPoints + " ranking points.");
    }
}

// Create an instance of the class
const player1 = new TennisPlayer('Anika', 23, 2400);

// Call the method
player1.profile();

```


    <IPython.core.display.Javascript object>


## Popcorn Hack 2

1. Create a class called library
2. Within library create a class called book with a constructors that allows the two methods - add book and remove book
3. Add another inner class called computers - and have it output the number of computers on

Below is the starter code to get you started


```javascript
%%javascript

// Step 1: Create the main class called Library
class Library {
    constructor(name) {
        this.name = name;
        console.log(`Welcome to the {this.name} Library!`);
    }
}

// Step 2: Create the inner "Book" class (as a static class)
Library.Book = class {
    constructor() {
        this.books = [];
    }

    addBook(title) {
        this.books.push(title);
        console.log(`Added "{title}" to the library.`);
    }

    removeBook(title) {
        const index = this.books.indexOf(title);
        if (index > -1) {
            this.books.splice(index, 1);
            console.log(`Removed "{title}" from the library.`);
        } else {
            console.log(`"{title}" not found in the library.`);
        }
    }
};

// Step 3: Create another inner class called "Computers"
Library.Computers = class {
    constructor(computersOn) {
        this.computersOn = computersOn;
    }

    showComputersOn() {
        console.log(`There are currently {this.computersOn} computers on.`);
    }
};

// --- Example Usage ---
const myLibrary = new Library("Dead Poets Society");
const bookManager = new Library.Book();
const techRoom = new Library.Computers(8);

bookManager.addBook("All The Light We Cannot See");
bookManager.addBook("Paper Towns");
bookManager.removeBook("All The Light We Cannot See");
techRoom.showComputersOn();

```


    <IPython.core.display.Javascript object>


## Homework
Create and expand the Cookie Clicker project:
1. Fill out the cookies and cookiesPerClick variables.
2. Define what should happen upon clicking the cookie.
3. Create an `Upgrade` class that multiplies cookies per click, and expand the original cookieclicker class to integrate upgardes.
5. Print how each upgrade changes the total cookie output.
6. Add a cookie type variable which sets the specific type of cookie (ex: Chocolate chip, Oatmeal, etc.)
The following code is to help you get started.

#### Extra credit: Up to 0.03 points
- Create a new cell, apply the ALL of the above changes to a blank cookie clicker project, and submit that code for the cookie clicker project.


```javascript
%%javascript

// Main CookieClicker class
class CookieClicker {
  constructor(cookies, cookiesPerClick, cookieType) {
    this.cookies = cookies; // start value
    this.cookiesPerClick = cookiesPerClick;
    this.cookieType = cookieType;
  }

  click() {
    this.cookies += this.cookiesPerClick;
    console.log(`You have {this.cookies} {this.cookieType} cookies.`);
  }

  // Method to apply an upgrade
  applyUpgrade(upgrade) {
    this.cookiesPerClick *= upgrade.multiplier;
    console.log(
      `Upgrade applied: {upgrade.name}! Cookies per click is now {this.cookiesPerClick}.`
    );
  }
}

// Upgrade class
class Upgrade {
  constructor(name, multiplier) {
    this.name = name;
    this.multiplier = multiplier;
  }
}

// --- Example Usage ---

// Create a cookie clicker
const myClicker = new CookieClicker(0, 1, "Chocolate Chip");

// Click a few times
myClicker.click();
myClicker.click();

// Create upgrades
const goldenOven = new Upgrade("Golden Oven", 2);
const magicMilk = new Upgrade("Magic Milk", 3);

// Apply upgrades
myClicker.applyUpgrade(goldenOven);
myClicker.click(); // should earn double now

myClicker.applyUpgrade(magicMilk);
myClicker.click(); // earns 6x now (2×3=6)

```


    <IPython.core.display.Javascript object>


This is where you will find homework: [Github Homework Link](https://github.com/Open-Coding-Society/pages/tree/main/_notebooks/CSSE/JavaScriptLessons/Classes_and_Methods)
