---
---

```python
---
title: Math 1B Chapter 7 
comments: true
layout: post
description: Math 1B Chapter 7 equation of a line problems
author: John Mortensen
permalink: /tools/kernels/math
categories: [Math]
---
```

## Problem:
Write the equation of the line with x-intercept (-4, 0) and y-intercept (0, 9).

## Solution:
Calculate the slope (m) using the formula:
m = (y2 - y1) / (x2 - x1)
where (x1, y1) = (-4, 0) and (x2, y2) = (0, 9).

Use the slope-intercept form of the equation of a line:
y = mx + b
where b is the y-intercept.

## Steps in Python:
1. Calculate the slope.
2. Write the equation of the line.
3. Plot the line.


```python
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image, display

"""Function to dynamically format a number based on its precision"""
def dynamic_format(value):
    """Dynamically format a number based on its precision."""
    if abs(value - round(value)) < 0.001:  # Close enough to a whole number
        return f"{int(round(value))}"
    elif abs(value * 10 - round(value * 10)) < 0.001:  # Close enough to one decimal place
        return f"{value:.1f}"
    else:  # Two decimal places
        return f"{value:.2f}"
    
"""Construct the equation of the line given two points"""
# Given points
x1, y1 = 1, 9
x2, y2 = -4, 2

# Ensure x1 < x2, on the left by swapping points if necessary
if x1 > x2:
    x1, x2 = x2, x1
    y1, y2 = y2, y1

# Calculate the slope (m)
m_numerator = y2 - y1
m_denominator = x2 - x1
m = m_numerator / m_denominator

# Calculate the y-intercept (b)
b = y1 - m * x1

# Calculate the x-intercept
x_intercept = -b / m

# Print the equation of the line: y = mx + b
print(f"The equation of the line is: y = ({m_numerator}/{m_denominator})x + {dynamic_format(b)}")

"""Build the points of the line using Numpy"""
x = np.linspace(x_intercept - 1, b + 1, 100)  # -1 and +1 to extend the line beyond the intercepts, 100 points
y = m * x + b  # Calculate y values using the equation of the line

"""Print data in NumPy arrays (optional)"""
formatted_points_start = [(dynamic_format(x_val), dynamic_format(y_val)) for x_val, y_val in zip(x[:5], y[:5])]
formatted_points_end = [(dynamic_format(x_val), dynamic_format(y_val)) for x_val, y_val in zip(x[-5:], y[-5:])]
print(f"Formatted First 5 points of the line: {formatted_points_start}")
print(f"Formatted Last 5 points of the line: {formatted_points_end}")

"""Use Matplotlib to plot the line"""
# Set up labels for plt
plt.title(f'Line with x-intercept ({dynamic_format(x_intercept)}, {0}) and y-intercept ({0}, {dynamic_format(b)})')
plt.xlabel('x')
plt.ylabel('y')
# Add grid and axis lines
plt.grid(color='gray', linestyle='--', linewidth=0.5)  # Add grid
plt.axhline(0, color='black', linewidth=0.5)  # Highlight x-axis
plt.axvline(0, color='black', linewidth=0.5)  # Highlight y-axis
# Plot using the equation of the line, including label of equation in the legend
plt.plot(x, y, label=f'y = ({m_numerator}/{m_denominator})x + {dynamic_format(b)}')

# Scatter the original points
plt.scatter([x1, x2], [y1, y2], color='blue', label='Original Points')  # Original points
plt.text(x1, y1, f'({dynamic_format(x1)}, {dynamic_format(y1)})', fontsize=12, ha='right', color='blue')
plt.text(x2, y2, f'({dynamic_format(x2)}, {dynamic_format(y2)})', fontsize=12, ha='right', color='blue')

# Scatter the x and y intercepts
plt.scatter([x_intercept, 0], [0, b], color='red', label='Intercepts')  # Intercepts
plt.text(0, b, f'({0}, {dynamic_format(b)})', fontsize=12, ha='right', color='red')
plt.text(x_intercept, 0, f'({dynamic_format(x_intercept)}, {0})', fontsize=12, ha='left', color='red')

# Save the plot to a file
output = './matlib/IM_ch7_equation_from_2_points.png'
plt.legend()
plt.savefig(output)
plt.close()
# Display the saved plot using IPython.display
display(Image(filename=output))
```

    The equation of the line is: y = (7/5)x + 7.6
    Formatted First 5 points of the line: [('-6.43', '-1.4'), ('-6.28', '-1.19'), ('-6.12', '-0.97'), ('-5.97', '-0.76'), ('-5.82', '-0.55')]
    Formatted Last 5 points of the line: [('7.99', '18.79'), ('8.14', '19.00'), ('8.30', '19.21'), ('8.45', '19.43'), ('8.6', '19.64')]



    
![png](output_2_1.png)
    


## Hack
MatPlot images don't get published to GitHub pages automatically.   IPRNB conversion does not plan for 

### Step 1: Save the Plot as an Image
Comment out the show() code to save the plot as an image file. You can use the savefig function from matplotlib to save the plot.  This still shows in VSCode output.

```js
lt.legend()
plt.savefig(output)
#plt.show()
```

### Step 2: Reference the Image in Your Markdown or HTML
After saving the plot as an image file, you can reference this image in your Markdown or HTML files. Make sure to place the image file in a location that is accessible by your GitHub Pages site, such as the assets or images directory.

Example in Markdown:

```markdown
![Line Plot](output)
```

Example in HTML:

```html
<img src="output" alt="Line Plot">
```

### Step 3: Automating the Process for GitHub Pages
You can automate the process of saving plots and converting notebooks to Markdown using Jupyter Notebook extensions or custom scripts, for instance the nbconvert.sh. 

You can then manually move the images to the appropriate directory so the MatPlot is visible in location `./matlib'.

By following these steps, you can include the generated plots from your Jupyter notebook in your GitHub Pages site, making them accessible on the deployed server.


