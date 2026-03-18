---
layout: base
title: Reporting Issues
permalink: /hallpass/requestpass
---

<div class="container">
    <div class="components">
        <!-- header section -->
        <div class="div1">
            <div class="queue-header">
                <h2>Welcome to Hall Pass Request</h2>
            </div>
            <div class="queue-info">
                <img src="https://github.com/user-attachments/assets/0f91ecf3-72a3-4712-b0ba-8d0f8ca55bb3" alt="Hall Pass Icon" height="80">
            </div>
            <hr>
        </div>

        <!-- content section -->
        <div class="div2">
            <!-- Confirmation Message Container -->
            <div id="confirmation-container" style="display: none;">
                <p id="confirm-message"></p>
            </div>

            <!-- Error Message Container -->
            <div id="error-container" style="display: none;" role="alert">
                <p id="error-message"></p>
            </div>

            <!-- Active Pass Container -->
            <div id="active-pass-container" style="display: none;">
                <h3>You have an active hall pass</h3>
                <div>
                    <p>Teacher: <span id="active-teacher"></span></p>
                    <p>Activity: <span id="active-activity"></span></p>
                    <p>Period: <span id="active-period"></span></p>
                </div>
                <div class="queue-buttons">
                    <button id="checkinBtn" type="button" class="medium primary">Check-in Hall Pass</button>
                </div>
            </div>

            <!-- Request Pass Form -->
            <div id="pass-form" style="display: none;">
                <h3>Request Hall Pass</h3>
                <div>
                    <div>
                        <label for="period">Period:</label>
                        <select id="period" name="period">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                        </select>
                    </div>
                    <div>
                        <label for="activity">Activity:</label>
                        <select id="activity" name="activity">
                            <option value="bathroom">Bathroom</option>
                            <option value="library">Library</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="queue-buttons">
                        <button id="requestPassBtn" type="button" class="medium primary">Request Hall Pass</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<script type="module">
    import { javaURI, pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
    document.addEventListener("DOMContentLoaded", function () {
            // Add click event listener to the "Request Hall Pass" button
            document.getElementById("requestPassBtn").addEventListener("click", requestHallPass);
            document.getElementById("checkinBtn").addEventListener("click", checkinHallPass);
        });
    async function fetchTeacherData() {
        try {
            let response = await fetch(javaURI + "/api/hallpass/getTeacher?fname=John&lname=Mortensen", fetchOptions);
            if (!response.ok) throw new Error("Network response was not ok");

            const contentType = response.headers.get("content-type");
            let data = contentType && contentType.includes("application/json") ? await response.json() : await response.text();

            if (!data || (typeof data === "object" && Object.keys(data).length === 0)) {
                document.getElementById("error-message").textContent = "Teacher not found. Scan QR Code again. Reach out to your teacher for assistance.";
                document.getElementById("error-container").style.display = "block";
            } else {
                await fetchActivePass();
            }
        } catch (error) {
            console.error("Error fetching teacher data:", error);
            document.getElementById("error-message").textContent = "An error occurred while fetching data. Please try again later.";
            document.getElementById("error-container").style.display = "block";
        }
    }

    async function fetchActivePass() {
        try {
            let response = await fetch(javaURI + "/api/hallpass/getactivepass?email=toby", fetchOptions);
            if (!response.ok) throw new Error("Network response was not ok");

            const contentType = response.headers.get("content-type");
            let data = contentType && contentType.includes("application/json") ? await response.json() : await response.text();

            if (!data || (typeof data === "object" && Object.keys(data).length === 0)) {
                document.getElementById("pass-form").style.display = "block";
            } else {
                document.getElementById("active-pass-container").style.display = "block";
                document.getElementById("active-teacher").textContent = 'John Mortensen' //`${data.teacher_id}`;
                document.getElementById("active-activity").textContent = data.activity;
                document.getElementById("active-period").textContent = data.period;
            }
        } catch (error) {
            console.error("Error fetching active pass:", error);
            document.getElementById("error-message").textContent = "An error occurred while fetching data. Please try again later.";
            document.getElementById("error-container").style.display = "block";
        }
    }

    async function requestHallPass() {
        const period = document.getElementById("period").value;
        const activity = document.getElementById("activity").value;
        const resultDiv = document.getElementById("confirm-message");

        resultDiv.innerHTML = ""; // Clear previous results

        const requestBody = {
            userName: "toby",
            teacherId: "26",
            period: period,
            activity: activity
        };

        try {
            const response = await fetch(javaURI + "/api/hallpass/request", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(requestBody)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.text();
            document.getElementById("pass-form").style.display = "none";
            document.getElementById("active-pass-container").style.display = "none";
            document.getElementById("confirmation-container").style.display = "block";
            resultDiv.innerHTML = "Thank you! Your hall pass request has been successfully processed. You may leave the classroom now. Reload the page once you return.";

        } catch (error) {
            //resultDiv.innerHTML = `<span style="color: red;">${error.message}</span>`;
        }
    }

    async function checkinHallPass() {

        try {
            const response = await fetch(javaURI + "/api/hallpass/checkout?email=toby", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                }
            });
            const resultDiv = document.getElementById("confirm-message");

            resultDiv.innerHTML = ""; // Clear previous results

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.text();

            document.getElementById("pass-form").style.display = "none";
            document.getElementById("active-pass-container").style.display = "none";
            document.getElementById("confirmation-container").style.display = "block";
            
            resultDiv.innerHTML = "Thank You! Your hall pass visit has been recorded. Have a nice day!";

        } catch (error) {
            //resultDiv.innerHTML = `<span style="color: red;">${error.message}</span>`;
        }
    }

    fetchTeacherData();
</script>
