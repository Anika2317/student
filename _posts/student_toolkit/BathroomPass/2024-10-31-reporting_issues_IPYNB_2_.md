---
layout: toolkit
title: Reporting Issues
permalink: /bathroom/issues
---

<head>
    <link rel="stylesheet" href="{{site.baseurl}}/assets/Bathroom/report-issues.css">
</head>

<style>
    #additionalInfo {
        display: none;
    }
</style>

<div class="container">
    <div class="components">
        <form id="login-form" class="form">
            <div class="div1">
                <!-- choose what bathroom has an issue and report it -->
                <div class="segmented-control">
                    <input type="radio" name="radio2" value="3" id="tab-1" checked />
                    <label for="tab-1" class="segmented-control__1">
                        <p>D</p>
                    </label>
                    <input type="radio" name="radio2" value="4" id="tab-2" />
                    <label for="tab-2" class="segmented-control__2">
                        <p>L</p>
                    </label>
                    <input type="radio" name="radio2" value="5" id="tab-3" />
                    <label for="tab-3" class="segmented-control__3">
                        <p>A</p>
                    </label>
                    <input type="radio" name="radio2" value="6" id="tab-4" />
                    <label for="tab-4" class="segmented-control__3">
                        <p>FF</p>
                    </label>
                    <input type="radio" name="radio2" value="7" id="tab-5" />
                    <label for="tab-5" class="segmented-control__3">
                        <p>LR</p>
                    </label>
                    <div class="segmented-control__color"></div>
                </div>
            </div>
            <!-- checkbox for selecting an issue -->
            <div class="checkbox">
                <label class="switch">
                    <span class="toggle">
                        <input type="checkbox" id="checkbox-1">
                        <span class="slider"></span>
                    </span>
                    <span class="label-text">No door lock</span>
                </label><br>

                <label class="switch">
                    <span class="toggle">
                        <input type="checkbox" id="checkbox-2">
                        <span class="slider"></span>
                    </span>
                    <span class="label-text">No Toilet Paper</span>
                </label><br>

                <label class="switch">
                    <span class="toggle">
                        <input type="checkbox" id="checkbox-3">
                        <span class="slider"></span>
                    </span>
                    <span class="label-text">No Stall Doors</span>
                </label><br>

                <label class="switch">
                    <span class="toggle">
                        <input type="checkbox" id="checkbox-4">
                        <span class="slider"></span>
                    </span>
                    <span class="label-text">Other</span>
                </label><br>
            </div>            
            <div>
                <!-- any additional info to add -->
                <input id="additionalInfo" type="text" placeholder="Anything else?" /><br>
                <!-- report an issue Button -->
                <button id="report-btn" class="large filledHighlight primary" type="button" style="margin-right: 10px">
                    <p>Report Issue</p>
                </button>
                <!-- cancel Button -->
                <a href="{{site.baseurl}}/bathroom"><button class="large secondary">Cancel</button></a>
            </div>
        </form>
        <!-- Error Chip (Hidden Initially) -->
        <div class="chip" id="error-chip" style="display:none;">
            <div class="chip__icon">
                <ion-icon name="warning-outline"></ion-icon>
            </div>
            <p>Error reporting issue.</p> <!-- This message can change dynamically -->
            <span class="chip__close" onclick="hideChip()"><ion-icon name="close"></ion-icon></span>
        </div>
    </div>
</div>

<div class="map-container">
    <img src="{{site.baseurl}}/images/bathroom/map.png" alt="Map">
</div>

<script type="module">
    import { javaURI, pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    async function fetchLocations() {
        try {
            const response = await fetch(javaURI + '/api/issue/issues', fetchOptions);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const issues = await response.json();

            const mapContainer = document.querySelector('.map-container');

            issues.forEach(issue => {
                console.log(issue.bathroom)
                if (issue.count == 0) {
                    return;
                }
                const locElement = document.createElement('div');
                locElement.className = 'location';
                locElement.style.position = 'absolute';
                locElement.style.top = (issue.positionY * 100) + '%';
                locElement.style.left = (issue.positionX * 100) + '%';

                const icon = document.createElement('img');
                icon.src = '{{site.baseurl}}/images/bathroom/marker.webp';
                icon.alt = 'Location Icon';
                icon.style.width = '48px';
                icon.style.height = '48px';

                const info = document.createElement('div');
                info.className = 'info';
                info.textContent = `${issue.bathroom} Bathroom: ${issue.issue}`;

                locElement.appendChild(icon);
                locElement.appendChild(info);
                mapContainer.appendChild(locElement);
            });
        } catch (error) {
            console.error('Error fetching issues:', error);
        }
    }

    // Fetch locations on page load
    fetchLocations();

    const other = document.getElementById("checkbox-4");
    const report_button = document.getElementById("report-btn");

    other.addEventListener('click', function (){
        console.log('other clicked');
        document.getElementById('additionalInfo').style.display = 'block';
    });

    const url = javaURI + '/api/issue/update/';

    window.report_box = function report_box() {
        // Collect all selected checkboxes
        const selectedBathroom = document.querySelector('input[name="radio2"]:checked');
        if (!selectedBathroom) {
            alert("Please select a bathroom.");
            return;
        }
        let bathroomValue = selectedBathroom.value; // Make sure to use `let` for reassignment
        switch (bathroomValue) {
            case '3':
                bathroomValue = 'D Building Bathroom';
                break;
            case '4':
                bathroomValue = 'L Building Bathroom';
                break;
            case '5':
                bathroomValue = 'A Building Bathroom';
                break;
            case '6':
                bathroomValue = 'Football Field Bathroom';
                break;
            case '7':
                bathroomValue = 'Locker Room Bathroom';
                break;
        }

        const checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
        const selectedIssues = [];

        checkboxes.forEach(checkbox => {
            selectedIssues.push(checkbox.value); // Collect the values of selected checkboxes
        });

        const additionalIssue = document.getElementById("additionalInfo").value;
        if (selectedIssues.length === 0 && additionalIssue == null) {
            alert("Please select at least one issue.");
            return;
        }
        if (selectedIssues[0] == 'Other' && additionalIssue != null) {
            selectedIssues[0] = additionalIssue;
        }

        const reportData = {
            bathroomName: bathroomValue,
            issue: selectedIssues[0], // Sending all issues instead of just the first one
            count: 1
        };
        console.log(JSON.stringify(reportData));

        // Create a unique URL for each issue
        const putOptions = {
            ...fetchOptions,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(reportData), // Send the current issue in the body
        };

        // Send individual PUT requests for each issue
        fetch(javaURI + '/api/issue/add', putOptions)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                console.log('Success for issue:', data);
            })
            .catch(error => {
                console.error('Error for issue:', error);
            });


        alert("Issues reported!");
        // Fetch locations on page load
        fetchLocations();
    };

    report_button.addEventListener("click", report_box)

</script>

<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>

<style>
    .map-container {
        position: relative;
        width: 800px;
        height: 600px;
    }
    .map-container img {
        width: 100%;
        height: 100%;
        display: block;
    }
    .location {
        position: absolute;
        cursor: pointer;
    }
    .location:hover .info {
        display: block;
    }
    .info {
        display: none;
        position: absolute;
        bottom: 30px;
        left: -50px;
        background-color: rgba(0, 0, 0, 0.7);
        color: #fff;
        padding: 8px;
        border-radius: 4px;
        white-space: nowrap;
        z-index: 10;
    }
</style>
