---
layout: post
title: array Homework
description: Array Homework
categories: ['Javascript', 'Homework']
permalink: /Arrays
author: The Coders
---

## Homework

Arrays are like containers! They group multiple elements under one variable. You can see this by observing the code and the output. (run it)




```python
%%html


  <h2>Output</h2>
  <div id="output"></div>

  <script>
    document.getElementById("output").innerText = ""; // Clear output
    (() => {

        let numbers = [1, 2, 3, 4];
        console.log(numbers);
        document.getElementById("output").innerText += numbers;


    })();
  </script>
```



<html>

<body>
  <h2>Output</h2>
  <div id="output"></div>

  <script>
    document.getElementById("output").innerText = ""; // Clear output
    (() => {

        let numbers = [1, 2, 3, 4];
        console.log(numbers);
        document.getElementById("output").innerText += numbers;


    })();
  </script>
</body>
</html>



You can see that you only had to type one variable instead of multiple to get the group of numbers. Try it out yourself to get the concept

### Part A of the homework (Graded for completion)

- Think of 3 things you like to do on the weekend.
- Come up with a name for this list of 3 things
- In the code cell below, look for "titleofthings" and the 3 THINGS.
- Replace all of the "titleofthings" with the name you came up with.
- Replace THING 1, 2, and 3 with the 3 things you you like to do. (make sure not to delete the quotation marks)
- run the code


```python
%%html

  <h2>Output 2</h2>
  <div id="outputpls"></div>

  <script>
    document.getElementById("outputpls").innerText = ""; // Clear output
    (() => {

        let titleofthings = ["Listen to music", " play guitar", " & relax", ];
        const sentence = "I like to: " + titleofthings;
        console.log(sentence);
        document.getElementById("outputpls").innerText += sentence;


    })();
  </script>

```



<h2>Output 2</h2>
<div id="outputpls"></div>

<script>
  document.getElementById("outputpls").innerText = ""; // Clear output
  (() => {

      let titleofthings = ["Listen to music", " play guitar", " & relax", ];
      const sentence = "I like to: " + titleofthings;
      console.log(sentence);
      document.getElementById("outputpls").innerText += sentence;


  })();
</script>




```python

```

Once you have ran the code, see how your list is generated without you having to type each individual word into the DOM. This concept applies to all other situations where you would want to reference your list.

### Part B (Graded for completion)

- Let's say you want to write a few sentences about the things you do after school, but you don't want to have to type out the list every time you want to reference it.
- Create an array to make writing this more efficient.
- Come up with a unique title for the list and replace NAME with your title.
- Replace LIST with your list. Make sure to remember the quotation marks and commas.


```python
%%html

  <h2>Output</h2>
  <div id="output3"></div>

  <script>
    document.getElementById("output3").innerText = ""; // Clear output
    (() => {

      
      let activity = ["Listen to music", " play guitar", " & relax", ];
      // Replace the blanks, that look like this _____, below! HINT: the line above
      const smallParagraph = "After school, I like to " + activity + ". This is because " + activity + " is really fun to me. I think you should try " + activity + "."; 
      console.log(smallParagraph);
      document.getElementById("output3").innerText += smallParagraph;


    })();
  </script>
```



<h2>Output</h2>
<div id="output3"></div>

<script>
  document.getElementById("output3").innerText = ""; // Clear output
  (() => {


    let activity = ["Listen to music", " play guitar", " & relax", ];
    // Replace the blanks, that look like this _____, below! HINT: the line above
    const smallParagraph = "After school, I like to " + activity + ". This is because " + activity + " is really fun to me. I think you should try " + activity + "."; 
    console.log(smallParagraph);
    document.getElementById("output3").innerText += smallParagraph;


  })();
</script>



If you did that correctly, you'll realize that you would've spent a LOT more time on that if you decided to type out your list every time it occured in those sentences instead of just using an array. When people use arrays, they have the goal of efficiency, and also organization. Arrays can help code from getting too lengthy, especially if the list if quite long and is referenced quite a lot.

### Part C (Graded on whether it worked or not)

Try it out yourself!

- Suppose you have a group of friends: Bob, Tom, and Steve. You are talking about them to a robot, and you are getting tired of saying each of their names over and over because this robot does not understand the concept of pronouns. How can you fix this?
    - In the code cell below, make an array to solve your problem. Write three sentences, each including the array. Use the console log and DOM to print the output. (if you don't know how to do this, you can reference the formats from the previous code cells and figure out what you should type. Make sure to note the subtle differences though, or else it won't work)


```python
%%html

<html>

<body>
  <h2>Output</h2>
  <div id="output4"></div>

  <script>
    document.getElementById("output4").innerText = ""; // Clear output
    (() => {
        let friends = [" Bob is cool", " Tom is not", " and Steve is just there"];
        const smallparagraph = "my friends are very interesting, because:" +friends
        console.log(smallparagraph);
        document.getElementById("output4").innerText += smallparagraph;


    })();
  </script>
</body>
</html>
```



<html>

<body>
  <h2>Output</h2>
  <div id="output4"></div>

  <script>
    document.getElementById("output4").innerText = ""; // Clear output
    (() => {
        let friends = [" Bob is cool", " Tom is not", " and Steve is just there"];
        const smallparagraph = "my friends are very interesting, because:" +friends
        console.log(smallparagraph);
        document.getElementById("output4").innerText += smallparagraph;


    })();
  </script>
</body>
</html>



## Submit here
https://docs.google.com/forms/d/e/1FAIpQLSfqHrQwvgNYvxxUxMD5mIfSgfZGkiDu6uPV0I_GMG8wqSQzpw/viewform?usp=header
