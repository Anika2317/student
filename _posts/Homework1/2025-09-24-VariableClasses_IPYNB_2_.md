---
layout: post
title: Classes and variables Homework
description: Classes and Variables Homework
categories: ['Javascript', 'Homework']
permalink: /classes-Variables-HW
author: Inventors
---

## POPCORN HACK 1 A short program about variables



```javascript
%%javascript

let name = "Anika";
let age = 14;

// Step 2: Print a message
console.log("Hi, my name is", name);
console.log("I am", age, "years old.");


// Step 3: Unfinished part
// TODO: Make a new variable called "nextYearAge"
// that is the age plus 1
let NextYearAge = age + 1;

// let nextYearAge = age + 1   // <-- finish this line!

// TODO: Print out the result
// Example: "Next year I will be 11 years old."
console.log("Next year, Ill be" + NextYearAge + "years old!" )   // <-- finish this line!


```


    <IPython.core.display.Javascript object>


## POPCORN HACK 2 A short program about classes



```javascript
%%javascript

// Step 1: Define the Animal class
class Animal {
  constructor(name, sound, kind) {
    this.name = name;
    this.sound = sound;
    this.kind = kind;
  }

  // Make the animal speak
  speak() {
    console.log(this.name + " the " + this.kind + " says " + this.sound + " !");
  }

  // Bonus method: describe the animal
  describe() {
    console.log(this.name + " is a " + this.kind + " and is not very nice!");
  }
}

// Step 2: Create a list to hold all the animals in the zoo
let zoo = [];

// Step 3: Add animals to the zoo
zoo.push(new Animal("Buddy", "Woof", "Dog"));
zoo.push(new Animal("Mittens", "Meow", "Cat"));
zoo.push(new Animal("Polly", "Squawk", "Parrot"));
zoo.push(new Animal("Pete", "moo", "cow"));



// Step 4: Loop through all animals and make them speak
zoo.forEach(animal => {
  animal.speak();
  animal.describe();
});

```


    <IPython.core.display.Javascript object>


## Homework


```javascript
%%javascript

## Step 1: Make a list of choices
const_choices = ["rock", "paper", "scissors"];

## Step 2: Ask the user for their choice (browser version with prompt)
let_userChoice = prompt("Choose rock, paper, or scissors:").toLowerCase();

## Step 3: Computer picks a random choice
const_computerChoice = choices[Math.floor(Math.random() * choices.length)];
console.log("Computer chose:", computerChoice);

## Step 4: Compare userChoice and computerChoice
if (userChoice == computerChoice) {
  console.log("It's a tie!");
} else if (userChoice === "rock" && computerChoice === "scissors") {
  console.log("You win!");
} else if (userChoice === "scissors" && computerChoice === "paper") {
  console.log("You win!");
} else if (userChoice === "paper" && computerChoice === "rock") {
  console.log("You win!");
} else {
  console.log("You lose!");
}

## Bonus
/*
while (true) {
  let userChoice = prompt("Choose rock, paper, or scissors”)
}
```


    <IPython.core.display.Javascript object>


## Sumbmission!
