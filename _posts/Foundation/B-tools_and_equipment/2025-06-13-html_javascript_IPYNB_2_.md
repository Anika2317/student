---
---

```python
---
layout: post
title: HTML and JavaScript Lesson
description: This page will teach you the basics of HTML and JavaScript.
categories: ['HTML', 'JavaScript']
permalink: /lessons/htmljs
---
```

## HTML Basics

HTML (HyperText Markup Language) gives structure to your content. It's the standard language used to create webpages.

> 💡 In Markdown (which you're using in `.md` files via fastpages), you can do many similar things with simpler syntax. Here's how HTML compares and expands on that.

### Headings, Paragraphs, and Emphasis

Markdown:

```markdown
# Welcome to My Web Page
This page uses **HTML** to display content and *JavaScript* to make it fun!
```

HTML:

```html
<h1>Welcome to My Web Page</h1>
<p>This page uses <b>HTML</b> to display content and <i>JavaScript</i> to make it fun!</p>
```

### Links and Lists

Markdown:

```markdown
[Visit MDN Web Docs](https://developer.mozilla.org)

- Learn HTML
- Practice JavaScript
- Have fun coding
```

HTML:

```html
<a href="https://developer.mozilla.org">Visit MDN Web Docs</a>

<ul>
  <li>Learn HTML</li>
  <li>Practice JavaScript</li>
  <li>Have fun coding</li>
</ul>
```

| Feature        | Markdown Syntax                            | HTML Syntax                                 |
| -------------- | ------------------------------------------ | ------------------------------------------- |
| Heading 1      | `# Heading`                                | `<h1>Heading</h1>`                          |
| Heading 2      | `## Subheading`                            | `<h2>Subheading</h2>`                       |
| Bold           | `**bold**` or `__bold__`                   | `<b>bold</b>` or `<strong>bold</strong>`    |
| Italic         | `*italic*` or `_italic_`                   | `<i>italic</i>` or `<em>italic</em>`        |
| Link           | `[OpenAI](https://openai.com)`             | `<a href="https://openai.com">OpenAI</a>`   |
| Image          | `![Alt](image.png)`                        | `<img src="image.png" alt="Alt">`           |
| Unordered List | `- Item` or `* Item`                       | `<ul><li>Item</li></ul>`                    |
| Ordered List   | `1. First`                                 | `<ol><li>First</li></ol>`                   |
| Paragraph      | *blank line between text*                  | `<p>Paragraph</p>`                          |
| Line Break     | `&nbsp;` or two spaces then Enter          | `<br>`                                      |
| Code (inline)  | `` `code` ``                               | `<code>code</code>`                         |
| Code Block     | <code>`js<br>console.log('hi')<br>`</code> | `<pre><code>console.log('hi')</code></pre>` |


---
