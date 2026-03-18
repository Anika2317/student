---
layout: aesthetihawk
title: Bathroom
permalink: /hallpass_queue
active_tab: hallpass
toc: False
---

<div class="container">
    <div class="components">
        <!-- queue header and your info like ETA -->
        <div class="div1">
            <div class="queue-header">
                <h2>Mr. Mortensen's Queue</h2>
            </div>
            <hr>
        </div>
        <!-- students in line -->
        <div class="div2">
            <div class="queue-list">
                <p>Students currently in line:</p>
                <ul id="studentList">
                    <!-- Students will be listed here -->
                </ul>
            </div>
            <div class="queue-buttons flex flex-wrap gap-2 justify-center mt-4">
                <button type="button" class="min-w-[12rem] h-12 px-4 py-2 text-center flex items-center justify-center bg-blue-600 text-white rounded-md" onclick="window.addToQueue()">Add Me to Queue</button>
                <button type="button" class="min-w-[12rem] h-12 px-4 py-2 text-center flex items-center justify-center bg-blue-600 text-white rounded-md" onclick="window.removeFromQueue()">Remove Me from Queue</button>
            </div>
        </div>
    </div>
</div>

<!-- Moved here -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>

<script type="module">
    import {javaURI, fetchOptions} from "{{site.baseurl}}/assets/js/api/config.js";

    const deleteOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    };  
    const getUrl = javaURI + "/api/queue/getActive";
    const approvalUrl = javaURI + "/api/approval";
    const removeUrl = javaURI + "/api/queue/remove";
    const teacherEmail = "jmort1021@gmail.com";

    window.addEventListener("load", () => {
        fetchUser();
    });

    async function fetchUser() {
        try {
            const response = await fetch(javaURI + "/api/person/get", {
                method: "GET",
                cache: "no-cache",
                credentials: "include",
                headers: { 
                    "Content-Type": "application/json",
                    "X-Origin": "client",
                },
            });
            
            if (response.ok) {
                const userInfo = await response.json();
                window.studentName = userInfo.name;
                window.sid = userInfo.sid;
                window.roles = userInfo.roles.map(role => role.name).join(", ");
                console.log("Person: ", userInfo);
                
                updateUIWithUserInfo();
                window.fetchQueueData();
            } else {
                console.error("Failed to fetch user info. Status:", response.status);
                showLoginMessage();
            }
        } catch (error) {
            console.error("Error fetching user data:", error);
        }
    }

    function updateUIWithUserInfo() {
        if (window.studentName) {
            const queueInfo = document.querySelector(".queue-info");
            const userInfo = document.createElement("p");
            userInfo.textContent = `Logged in as: ${window.studentName}`;
            queueInfo?.appendChild(userInfo);
        }
    }

    window.addToQueue = function() {
        if (!window.studentName) {
            alert("Failed to join queue: You must be logged in first.");
            return;
        }
        
        const requestData = {
            teacherEmail: teacherEmail,
            studentName: window.studentName,
            timeIn: null
        };
        
        const now = new Date();
        const timeIn = `${now.getHours()}:${now.getMinutes().toString().padStart(2, "0")}:${now.getSeconds().toString().padStart(2, "0")}`;
        localStorage.setItem("timeIn", timeIn);

        fetch(approvalUrl + "/sendApprovalRequest", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestData),
        })
        .then(response => {
            if (response.ok) {
                console.log(`✅ Approval request sent for: ${window.studentName}`);
            } else {
                alert("Failed to request approval.");
            }
        })
        .catch(error => {
            console.error("Error requesting approval:", error);
            alert("Failed to request approval: Network error.");
        });
    };

    window.removeFromQueue = function() {
        if (!window.studentName) {
            alert("Failed to remove from queue: You must be logged in first.");
            return;
        }
        
        const queuer = {
            teacherEmail: teacherEmail,
            studentName: window.studentName,
        };

        fetch(removeUrl, {
            ...deleteOptions,
            body: JSON.stringify(queuer),
        })
        .then(response => {
            if (response.ok) {
                window.fetchQueueData();
            } else {
                alert("Failed to remove from queue.");
            }
        })
        .catch(error => {
            console.error("Error removing from queue:", error);
            alert("Failed to remove from queue: Network error.");
        });
    };

    window.displayQueue = function() {
        const studentList = document.getElementById("studentList");
        studentList.innerHTML = "";

        window.studentsInQueue.forEach((student, index) => {
            const listItem = document.createElement("li");
            const studentName = student || "Unknown Student";
            listItem.textContent = index === 0 ? `${studentName} (waiting for approval)` : studentName;

            if (window.studentName && student === window.studentName) {
                listItem.style.color = "red";
            }
            
            studentList.appendChild(listItem);
        });
    };

    window.fetchQueueData = function() {
        fetch(getUrl, fetchOptions)
            .then(response => {
                if (response.status !== 200) {
                    console.error("Failed to fetch queue data.");
                    return;
                }
                return response.json();
            })
            .then(data => {
                const mortensenQueue = data.find(queue => queue.teacherEmail === teacherEmail);
                if (mortensenQueue) {
                    window.studentsInQueue = mortensenQueue.peopleQueue.split(",");
                    const isFrontOfQueue = window.studentName && window.studentsInQueue[0] === window.studentName;

                    if (isFrontOfQueue && !window.isApproving) {
                        window.location.href = "{{site.baseurl}}/hallpass_queue/hallpass";
                        return;
                    }
                }
                window.displayQueue();
            })
            .catch(error => console.error("Error fetching data:", error));
    };

    window.approveStudent = function() {
        // Placeholder for future logic
    };

    if (window.queueInterval) clearInterval(window.queueInterval);
    window.queueInterval = setInterval(window.fetchQueueData, 5000);
</script>

