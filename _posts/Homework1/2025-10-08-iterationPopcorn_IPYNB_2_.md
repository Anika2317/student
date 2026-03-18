---
layout: post
title: Iteration Homework
description: Iteration Homework
categories: ['Javascript', 'Homework']
permalink: /Iteration
author: Inventors
---

### Hack 1: The "Counting Stars" Hack (The while Loop) 

Instruction: To run this hack, call the countStars() function with a number to set the limit for the star count.



```javascript
%%javascript

function countStars(limit) {
  // 1. Initialize a counter variable. We'll start our count at 1.
  let count = 1;


  // 2. Start the `while` loop. The code inside this loop will run
  // as long as the condition `count <= limit` is true.
  while (count <= limit) {
    // 3. This is the code that runs in each iteration.
    console.log(`Star #${count} shining bright!`);


    // 4. This is the increment step. It's crucial! If we don't
    // increase the `count`, the loop will run forever (an infinite loop).
    count++;
  }


  // 5. This message is displayed once the loop condition is no longer true
  // and the loop has finished.
  console.log("All the stars have been counted.");
}

```


    <IPython.core.display.Javascript object>


### Hack 2: The "Playlist Shuffle" Hack (The For Loop) 🎵
Instruction: To run this hack, define an array of strings called mySongs and pass that array into the playlistShuffle() function.


```javascript
%%javascript
function playlistShuffle(playlist) {
  // 1. Start the `for...of` loop. This loop is perfect for iterating
  // over the items of an array.
  // The variable `song` will hold the value of each item in the `playlist` array, one by one.
  for (const song of playlist) {
    // 2. Action performed for each song in the array.
    console.log(`Now playing: "${song}"`);
  }


  // 3. This message is displayed once the loop has processed every item in the array.
  console.log("All of the songs have been played");
}


// Example of how to define the array:
const mySongs = ["Roslyn", "Honeybee", "Bowery", "forever"]; 
// Then, call the function: playlistShuffle(mySongs);
playlistShuffle(mySongs);


```


    <IPython.core.display.Javascript object>


# Submission

You will submit the link to your homework on a web page in the below form.  
If you are unable to get your homework accessible from the website, you can upload this Jupyter notebook to the form.

**IMPORTANT: If uploading, please name this Jupyter notebook in this format: [FirstName][LastName]_iterations_hw.ipynb**


https://forms.gle/yaiYRXDq341kb2538

