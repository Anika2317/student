---
layout: toolkit
title: Hallpass
permalink: /hallpass_queue/hallpass
menu: nav/toolkits/bathroom/menu.html
toc: False
---

<div class="hallpass-container">
    <div class="hallpass-header">Hall Pass</div>
    <img src="https://github.com/user-attachments/assets/414c847a-acb9-4b82-a011-d9c6cf09477f" alt="Bathroom Pass" class="hallpass-icon">
    <p class="hallpass-details">
        <strong>Student:</strong> <span id="studentNameDisplay"></span><br>
        <strong>Teacher:</strong> Mr. Mortensen
    </p>
    <div class="hallpass-buttons">
        <button type="button" onclick="window.approveStudent()">I'm done</button>
        <button type="button" class="exit-button" onclick="window.location.href='{{site.baseurl}}/bathroom'">Exit</button>
    </div>
</div>

<script type="module">
  import { javaURI, fetchOptions } from "{{site.baseurl}}/assets/js/api/config.js";

  const teacherName = "jmort1021@gmail.com"; 
  const url = javaURI + `/api/queue`;
  const adminUrl = `${javaURI}/api/tinkle/add`;
  const removeFrontUrl = `${javaURI}/api/queue/removeFront`;
  const postOptions = {
      ...fetchOptions,
      method: 'POST',
  };

  window.addEventListener('load', () => {
    fetchUser();
  });

  async function fetchUser() {
      const response = await fetch(javaURI + `/api/person/get`, {
          method: 'GET',
          cache: "no-cache",
          credentials: 'include',
          headers: { 
              'Content-Type': 'application/json',
              'X-Origin': 'client' 
          }
      });
      if (response.ok) {
          const userInfo = await response.json();
          window.studentName = userInfo.name;
          window.studentSid = userInfo.sid;
          document.getElementById("studentNameDisplay").textContent = window.studentName;
          console.log("Person: ", userInfo);
      }
  }

  window.approveStudent = async function() {
      const now = new Date();
      const hours = now.getHours();
      const minutes = now.getMinutes().toString().padStart(2, "0");
      const seconds = now.getSeconds().toString().padStart(2, "0");
      const timeOut = `${hours}:${minutes}:${seconds}`;

      const timeIn = localStorage.getItem("timeIn");
      let timeSpentMinutes = 0;
      if (timeIn) {
          const [inHours, inMinutes, inSeconds] = timeIn.split(":").map(Number);
          const [outHours, outMinutes, outSeconds] = timeOut.split(":").map(Number);
          const totalSecondsIn = inHours * 3600 + inMinutes * 60 + inSeconds;
          const totalSecondsOut = outHours * 3600 + outMinutes * 60 + outSeconds;
          const timeSpentSeconds = totalSecondsOut - totalSecondsIn;
          timeSpentMinutes = (timeSpentSeconds / 60).toFixed(2);
          console.log(`Time spent: ${timeSpentMinutes} minutes`);
      }

      const timeInOut = `${timeIn}-${timeOut}`;

      const times = {
          sid: window.studentSid,
          timeIn: timeInOut,
      };

      const queuer = {
          teacherEmail: teacherName,
          studentName: window.studentName,
          uri: javaURI,
      };

      try {
          const adminResponse = await fetch(adminUrl, {
              ...postOptions,
              body: JSON.stringify(times),
          });
          if (adminResponse.ok) {
              console.log("Time added to database");
          } else {
              alert("Failed to add time to database.");
          }

          const removeResponse = await fetch(removeFrontUrl, {
              ...postOptions,
              body: JSON.stringify(queuer),
          });
          if (removeResponse.ok) {
              console.log("✅ Removed student from front of queue");
          } else {
              alert("❌ Failed to remove student from queue.");
          }
      } catch (error) {
          console.error("Error with fetch requests:", error);
      }

      window.location.href = "{{site.baseurl}}/profile";
  }
</script>
