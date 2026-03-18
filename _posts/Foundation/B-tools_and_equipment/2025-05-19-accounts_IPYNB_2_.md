---
---

```python
---
toc: True
layout: post
data: tools
title: Account Creation
description: Learn how to create and manage course-required accounts, including a Portfolio Website, GitHub, Slack, and LinkedIn, while protecting your Personal Identifiable Information (PII).
categories: ['DevOps']
permalink: /tools/accounts
breadcrumb: True
---
```

## What Is PII?

**PII (Personal Identifiable Information)** is any detail that can identify you—like your name, address, or account info.

In this course, you may share or work with PII. Let’s make sure it’s handled wisely.

---

<div style="display: flex; align-items: flex-start; gap: 24px; margin-top: 20px;">

  <img src="{{site.baseurl}}/images/tools/accounts.png" alt="PII graphic" style="width:50%; max-width:400px; border-radius: 12px;"/>


<div id="pii-container"></div>

<script>
  const piiData = {
    Public: [
      "Name, Email, Photo",
      "Schools, City, Property",
      "Credit Reports, Router Info"
    ],
    Sensitive: [
      "Birthdate, Address, Phone",
      "Place of Birth, Maiden Names",
      "Driver’s License"
    ],
    Private: [
      "Social Security Number",
      "Login Credentials",
      "Two-Factor Sources"
    ]
  };

  const container = document.getElementById("pii-container");
  const heading = document.createElement("h3");
  heading.textContent = "Know Your PII";
  container.appendChild(heading);

  Object.entries(piiData).forEach(([category, items]) => {
    const button = document.createElement("button");
    button.textContent = `▶ ${category}`;
    button.style.margin = "10px 0";
    button.style.padding = "8px 14px";
    button.style.border = "none";
    button.style.borderRadius = "8px";
    button.style.backgroundColor = "#2c2a5d";  // dark blue/purple
    button.style.color = "white";
    button.style.fontSize = "16px";
    button.style.cursor = "pointer";
    button.style.transition = "background-color 0.3s";

    button.onmouseover = () => button.style.backgroundColor = "#3a3770";
    button.onmouseout = () => button.style.backgroundColor = "#2c2a5d";

    const list = document.createElement("ul");
    list.style.display = "none";
    list.style.margin = "8px 0 16px 20px";

    items.forEach(item => {
      const li = document.createElement("li");
      li.textContent = item;
      li.style.padding = "4px 0";
      list.appendChild(li);
    });

    button.addEventListener("click", () => {
      list.style.display = list.style.display === "none" ? "block" : "none";
    });

    container.appendChild(button);
    container.appendChild(list);
  });
</script>



</div>

<div style="display: flex; align-items: flex-start; gap: 24px; margin-top: 12px;">

  <img src="{{site.baseurl}}/images/tools/mfa.jpg" alt="Multi-Factor-Authentication" style="width:50%; min-width:120px; border-radius: 12px;" title='This is an Multi-Factor-Authentication'/>

  <div>
    <strong>Protect Your Information</strong>
    <ul>
      <li>Use <strong>Multi-Factor Authentication (MFA)</strong></li>
      <li>Create <strong>strong, unique passwords</strong></li>
      <li>Keep your <strong>software updated</strong></li>
      <li><strong>Encrypt</strong> data and backups</li>
      <li>Secure your <strong>Wi-Fi and router</strong></li>
      <li>Use <strong>biometrics</strong> where possible</li>
    </ul>
  </div>

</div>

---

### Online Risks

- **Phishing & malware** try to steal your data
- **Social engineering** tricks you into revealing info
- **Respond quickly** if compromised: update passwords and review your security

---



## PII Strategy on Account Creation

It is in your interest to establish and continually refine your PII (Personally Identifiable Information) strategy. You are likely already sharing some common PII, so consider for yourself what is OK to share. As you progress in the digital world, you will likely need to adapt.

### Key Points to Consider:

1. **Categorize Information**:  
   - 🟢 **Public Information**: Information you are comfortable sharing publicly, such as your name and general interests.
   - 🟡 **Sensitive Information**: Information that should be shared cautiously, such as your full birth date and phone number.
   - 🔴 **Highly Confidential Information**: Information that should be kept strictly private, like your social security number and internet access credentials.

2. **Use Different Email Accounts**:  
   - Maintain different email accounts for different purposes (e.g., junk email, common email, work/school email, important email). This helps manage the type and volume of information you receive and clarifies the importance of each account.

3. **Be Prepared for Security Incidents**:  
   - Anticipate that you may be hacked and be prepared to secure any vulnerabilities. Regularly update your passwords and use multi-factor authentication where possible.

4. **Adapt and Evolve**:  
   - As you gain more experience and your digital footprint grows, continually reassess and adapt your PII strategy to ensure it remains effective.

## Hacks

Create your course accounts.

As you create and manage your accounts, always be mindful of the information you are sharing. Protecting your PII is an ongoing process that requires vigilance and adaptability. By categorizing your information, using different email accounts, and preparing for potential security incidents, you can better safeguard your personal information.

<img src="{{site.baseurl}}/images/tools/13we.png" alt="Account Types" style="width:600px; border-radius: 12px;"/>

### Examples of Good User Names

Accoonts are public data.

Good:
- john-doe: Simple, professional, and easy to remember for you and to be recognized by others.
- johndev: Highlights your identity as a developer.
- jdoe123: A clean and professional option if your preferred username is already taken.

Bad:
- ilovecodinglol: Informal and not suitable for professional platforms. 
- coolguy123: Informal and makes it difficult for others to identify you as the source; such usernames can be seen as untrustworthy or even a potential threat.
- john.doe2005: Includes unnecessary personal information (e.g., birth year), which could compromise your privacy. The dot could be a problem on some platforms; stick to a dash.


### Examples of Good Passwords

Passwords are highly confidential information, but you need to remember them.  
A good password is long, unique, and not easily guessed. Use a mix of letters, numbers, and symbols. Consider using a passphrase—a sentence or a combination of random words that is easy for you to remember but hard for others to guess.

Good:
- **Blue!Tiger$Pizza2025** (a mix of words, symbols, and numbers)
- **Sunshine_4_RedBalloon!**
- **Giraffe2!TreeHouseRun**

Tips:
- Use at least 12 characters.
- Combine unrelated words or a phrase.
- Add numbers and special characters.
- Avoid using personal info (like your name or birthdate).
- Don’t reuse passwords across important accounts.
- Consider using a password manager to keep track of your passwords.

Bad:
- password123
- 123456
- qwerty
- yourname2025
- githubpassword

### Checklist for Account Creation

Use this checklist to track your progress as you create the required accounts:

* **Email Account**: Create or use a personal email account (e.g., Gmail) for development and accessibility.  
  * **Sign Up**: [Create a Gmail Account](https://accounts.google.com/signup)  
  * Many tools support logging in with Gmail, making it a convenient choice. Avoid using your school email for these accounts. Since your Gmail prefix is unique in the world, it may be a good choice for User ID on other setups on this page.

* **Slack Account**: Register for Slack using your personal email (e.g., Gmail).  
  * **Sign Up**: [Create a Slack Account](https://slack.com/get-started#/)

* **GitHub Account**: Create a GitHub account using the same personal email.  
  * **Sign Up**: [Create a GitHub Account](https://github.com/signup)  
  * This account will serve as your professional social media account as a coder. Avoid using your school email, as GitHub will be useful beyond your time in school.

* **GitHub Pages**: Publish a Student Portfolio using GitHub Pages.  
  * **Learn More**: [GitHub Pages Documentation](https://pages.github.com/)  
  * This will be a public website indexed by Google and Google Analytics.

* **Open Society Account**: Create an account on the course's Open Society platform  
  * **Sign Up**: [Open Coding Society](https://pages.opencodingsociety.com/)
  * Using your GitHub ID an account will be created to build course lists, provide compute services (e.g., AWS, KASM), and aggregate analytics for your instructor.
