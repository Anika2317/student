---
layout: post
title: GitHub Pages
description: This page will teach you how to set up GitHub Pages using the VSCode online editor.
categories: ['DevOps']
permalink: /tools/github_pages
---

<style>
details {
  border: 2px sopd #003366;
  border-radius: 12px;
  padding: 10px;
  margin-bottom: 16px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
  background: white;
  transition: background 0.2s;
}
details[open] {
  background: #f0f6ff;
}
summary {
  font-weight: bold;
  cursor: pointer;
  font-size: 1.1em;
  outpne: none;
}
details > div {
  margin-top: 10px;
}
@media (prefers-color-scheme: dark) {
  details {
    background: #181a20;
    color: #e0e6ef;
    border-color: #375a7f;
  }
  details[open] {
    background: #23263a;
  }
}
</style>

<style>
details {
  border: 2px solid #003366;
  border-radius: 12px;
  padding: 10px;
  margin-bottom: 16px;
  box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
  background: white;
  transition: background 0.2s;
}
details[open] {
  background: #f0f6ff;
}
summary {
  font-weight: bold;
  cursor: pointer;
  font-size: 1.1em;
  outline: none;
}
details > div {
  margin-top: 10px;
}

/* Progress Bar Styles */
.progress-tracker {
  background: #f8f9fa;
  border: 2px solid #003366;
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  text-align: center;
}

.progress-bar {
  width: 100%;
  height: 10px;
  background: #e9ecef;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 15px;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #003366, #0066cc);
  width: 0%;
  transition: width 0.8s ease;
  border-radius: 10px;
}

.progress-text {
  color: #003366;
  font-weight: 600;
  font-size: 1.1em;
}

/* Validator Styles */
.validator {
  background: #f8f9fa;
  border: 2px solid #dee2e6;
  border-radius: 8px;
  padding: 15px;
  margin-top: 15px;
}

.validator input {
  width: 70%;
  padding: 8px 12px;
  border: 2px solid #dee2e6;
  border-radius: 6px;
  margin-right: 10px;
  font-size: 14px;
}

.validator button {
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.validate-btn {
  background: #003366;
  color: white;
}

.validate-btn:hover {
  background: #0066cc;
}

.validate-btn:disabled {
  background: #6c757d;
  cursor: not-allowed;
}

.confirm-btn {
  background: #17a2b8;
  color: white;
  width: 100%;
}

.confirm-btn:hover {
  background: #138496;
}

.status {
  margin-top: 10px;
  padding: 8px 12px;
  border-radius: 6px;
  font-weight: 600;
}

.status.loading {
  background: #fff3cd;
  color: #856404;
  border: 1px solid #ffeaa7;
}

.status.success {
  background: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.status.error {
  background: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.step-complete {
  border-color: #28a745 !important;
  background: #d4edda !important;
}

@media (prefers-color-scheme: dark) {
  details {
    background: #181a20;
    color: #e0e6ef;
    border-color: #375a7f;
  }
  details[open] {
    background: #23263a;
  }
  .progress-tracker {
    background: #181a20;
    color: #e0e6ef;
    border-color: #375a7f;
  }
  .progress-bar {
    background: #374151;
  }
  .progress-text {
    color: #e0e6ef;
  }
  .validator {
    background: #2d3748;
    border-color: #4a5568;
    color: #e0e6ef;
  }
  .validator input {
    background: #374151;
    border-color: #4a5568;
    color: #e0e6ef;
  }
  .step-complete {
    background: #1a2f1a !important;
    border-color: #28a745 !important;
  }
}
</style>

<div class="progress-tracker">
  <div class="progress-bar">
    <div class="progress-fill" id="progressBar"></div>
  </div>
  <div class="progress-text">Progress: <span id="progressText">0%</span></div>
</div>

<details>
  <summary>What is GitHub Pages?</summary>
  <div>
    <p><strong>GitHub Pages</strong> is a free service provided by GitHub that allows you to host <em>static websites</em> directly from a GitHub repository. It's perfect for project documentation, portfolios, and personal websites. Once your site is published, it can be accessed through a unique GitHub URL — no extra hosting setup required!</p>
    <img src="{{site.baseurl}}/images/tools/github-pages.jpg" alt="GitHub Pages" style="width:50%; border-radius: 12px;"/>
  </div>
</details>

<details>
  <summary>What is Visual Studio Code?</summary>
  <div>
    <p><strong>Visual Studio Code (VSCode)</strong> is a free, open-source code editor developed by Microsoft. It's lightweight, highly customizable, and supports many programming languages. It includes powerful features like syntax highlighting, debugging tools, Git integration, and extensions.</p>
    <p>Even better: you can use VSCode <strong>in your browser</strong> by visiting <code>vscode.dev</code> — no installation required!</p>
    <img src="{{site.baseurl}}/images/tools/vscode.png" alt="VSCode" style="width:20%; border-radius: 12px;"/>
  </div>
</details>

<details id="step1">
  <summary>First Steps: Start Your Own Site</summary>
  <div>
    <p>1. Click the link below to open the starter repository:  
      🔗 <a href="https://github.com/Open-Coding-Society/student.git" target="_blank">Open Coding Society Student Repository</a>
    </p>
    <p>2. On the GitHub page, click the green <strong>"Use this template"</strong> button.</p>
    <img src="{{site.baseurl}}/images/tools/use-this-template.png" alt="Use Template Button" style="width:50%; border-radius: 12px;"/>
    <br>
    <p>3. Select <strong>"Create a new repository"</strong>.</p>
    <p>4. Follow onscreen instruction. Name it <strong>student</strong> .</p>
    <img src="{{site.baseurl}}/images/tools/createafork.png" alt="New Repo Page" style="width:50%; border-radius: 12px;"/>
    
    <div class="validator">
      <h4>✅ Validate Step 1</h4>
      <p>Enter your GitHub username to check if you created the repository:</p>
      <input type="text" id="githubUsername" placeholder="Your GitHub username" />
      <button class="validate-btn" onclick="validateStep1()">Check Repository</button>
      <div id="step1Status" class="status" style="display: none;"></div>
    </div>
  </div>
</details>

<details id="step2">
  <summary>Next Steps: Edit Your Site in the online VSCode editor.</summary>
  <div>
    <p>Now that you've created your own copy of the site:</p>
    <li>Open a new browser tab.</li>
    <li>Type the following URL, <strong>and please remember to replace the placeholders:</strong></li>
    <p>1. YOUR_GITHUB_USERNAME</p>
    <p>2. YOUR_REPOSITORY_USERNAME</p>
    <pre><code>vscode.dev/github/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME</code></pre>
    <p>You can write and edit your HTML, CSS, and JavaScript files directly in your browser.</p>
    <p>For example, to edit the main page, open <code>index.md</code> in the file explorer on the left side.</p>
    <p>3. Click on the file to open it.</p>
    <p>4. Make changes to the content. For example, you can change the text in the file near the top to be your first name.</p>
    <p>Try replacing [Your full name] with your name.</p>
    <img src="{{site.baseurl}}/images/tools/vscodedev.png" alt="vscode.dev Website" style="width:50%; border-radius: 12px;"/>
        <h4>Now you need to edit config.yml</h4>
    <p>1. Open <code>_config.yml</code></p>
    <p>2. Change <code>owner_name</code> to your full name</p>
    <p>3. Change <code>github_username</code> to your github username</p>
    <img src="{{site.baseurl}}/images/tools/editconfig-yml.png" alt="Edit config.yml" style="width:150%; border-radius: 12px;"/>  
    <div class="validator">
      <h4>✅ Validate Step 2</h4>
      <p>Once you've made changes to your files in VSCode, click the button below:</p>
      <button class="confirm-btn" onclick="validateStep2()">I've Made Changes in VSCode</button>
      <div id="step2Status" class="status" style="display: none;"></div>
    </div>
  </div>
</details>

<details id="step3">
  <summary>Next Steps: Save and push your changes onto your website.</summary>
  <div>
    <p>1. Now that you've finished making your changes to your site:</p>
    <p>2. Click the Source Control icon on the left sidebar (it looks like a branch).</p>
    <p>You should see your changes listed under <strong>Changes</strong>.</p>
    <p>3. Type a commit message in the input box at the top, like <strong>"Update index.md with my name"</strong>.</p>
    <p>4. Click the button which says "commit and push" your changes.</p>
    <img src="{{site.baseurl}}/images/tools/makechangescommit.png" alt="Commit changes" style="width:50%; border-radius: 12px;"/>
    
    <div class="validator">
      <h4>✅ Validate Step 3</h4>
      <p>Once you've committed and pushed your changes, click the button below:</p>
      <button class="confirm-btn" onclick="validateStep3()">I've Committed and Pushed My Changes</button>
      <div id="step3Status" class="status" style="display: none;"></div>
    </div>
  </div>
</details>

<details id="step4">
  <summary>Publish with GitHub Pages</summary>
  <div>
    <p>Once you've made changes to your site:</p>
    <p>Go to your repository on GitHub.</p>
    <p>1. Click <strong>Settings > Pages</strong>.</p>
    <p>2. Under <strong>Source</strong>, choose your main branch instead of none </p>
    <p>3. Click <strong>Save</strong>.</p>
    <p>After a moment, your website will be live at:</p>
    <pre><code>your_github_username.github.io/student/</code></pre>
    <p>4. Click "Visit site" to see your changes live!</p>
    <img src="{{site.baseurl}}/images/tools/changegithubpagesbuild.png" alt="Change GitHub Pages Build" style="width:50%; border-radius: 12px;"/>  
    <div class="validator">
      <h4>✅ Validate Step 4</h4>
      <p>Enter your GitHub Pages URL to verify your website is live:</p>
      <input type="url" id="websiteUrl" placeholder="https://yourusername.github.io/student/" />
      <button class="validate-btn" onclick="validateStep4()">Check Website</button>
      <div id="step4Status" class="status" style="display: none;"></div>
    </div>
  </div>
</details>

<details>
  <summary>Summary</summary>
  <div>
    <ul>
      <li>GitHub Pages hosts your static website — no server required.</li>
      <li>VSCode in the browser lets you code anytime, anywhere.</li>
      <li>For this basic way, all you need is a GitHub account and a browser — no installations!</li>
    </ul>
  </div>
</details>

<script>
let currentProgress = 0;
let completedSteps = new Set();

function updateProgress(targetProgress) {
  const progressBar = document.getElementById('progressBar');
  const progressText = document.getElementById('progressText');
  
  if (targetProgress > currentProgress) {
    currentProgress = targetProgress;
    progressBar.style.width = currentProgress + '%';
    progressText.textContent = currentProgress + '%';
    
    if (currentProgress === 100) {
      setTimeout(() => {
        progressBar.style.background = 'linear-gradient(90deg, #28a745, #20c997)';
        progressText.textContent = '100% Complete! 🎉';
      }, 500);
    }
  }
}

function showStatus(elementId, type, message) {
  const statusElement = document.getElementById(elementId);
  statusElement.className = `status ${type}`;
  statusElement.textContent = message;
  statusElement.style.display = 'block';
}

function markStepComplete(stepNumber) {
  if (!completedSteps.has(stepNumber)) {
    completedSteps.add(stepNumber);
    document.getElementById(`step${stepNumber}`).classList.add('step-complete');
    updateProgress(stepNumber * 25);
  }
}

async function validateStep1() {
  const username = document.getElementById('githubUsername').value.trim();
  if (!username) {
    showStatus('step1Status', 'error', 'Please enter your GitHub username');
    return;
  }
  
  showStatus('step1Status', 'loading', 'Checking repository...');
  
  try {
    const response = await fetch(`https://api.github.com/repos/${username}/student`);
    
    if (response.ok) {
      showStatus('step1Status', 'success', '✅ Great! Repository found successfully!');
      markStepComplete(1);
    } else if (response.status === 404) {
      showStatus('step1Status', 'error', '❌ Repository not found. Make sure you created a repository named "student"');
    } else {
      showStatus('step1Status', 'error', '❌ Error checking repository. Please try again.');
    }
  } catch (error) {
    showStatus('step1Status', 'error', '❌ Network error. Please check your connection and try again.');
  }
}

function validateStep2() {
  showStatus('step2Status', 'success', '✅ Step 2 completed! Moving to the next step.');
  markStepComplete(2);
}

function validateStep3() {
  showStatus('step3Status', 'success', '✅ Step 3 completed! Your changes are now saved.');
  markStepComplete(3);
}

async function validateStep4() {
  const url = document.getElementById('websiteUrl').value.trim();
  if (!url) {
    showStatus('step4Status', 'error', 'Please enter your website URL');
    return;
  }
  
  if (!url.includes('github.io')) {
    showStatus('step4Status', 'error', 'Please enter a valid GitHub Pages URL (should contain "github.io")');
    return;
  }
  
  showStatus('step4Status', 'loading', 'Checking if your website is live...');
  
  try {
    const response = await fetch(url, { mode: 'no-cors' });
    
    showStatus('step4Status', 'success', '✅ Congratulations! Your website is live and accessible!');
    markStepComplete(4);
    
  } catch (error) {
    showStatus('step4Status', 'error', '⚠️ Unable to verify website status. If you just enabled GitHub Pages, it might take a few minutes to go live. Try visiting the URL directly to check!');
  }
}
</script>
