---
layout: post
title: "GameBuilder Mastery: Sprint 6 Final Portfolio"
description: "Sprint 6 Final Portfolio — Anika Seksaria. CS 111 college credit evidence."
author: anika
date: 2026-03-17
categories: [Sprint6, GameBuilder, OOP, CS111]
---

# 🎮 GameBuilder Mastery: Sprint 6 Final Portfolio

**Author:** Anika Seksaria | **Role:** Scrummer | **Sprint:** 6 — Weeks 19–25
**Team:** Anika (Scrummer) · Mateo (Designer) · Rashi (Technologist)
**Course:** Mira Costa CS 111 — Introduction to Computer Science I

---

## 📋 Portfolio Navigation

| Page | What's Inside | Link |
|:-----|:-------------|:-----|
| 🏠 **Main Page** | SDLC, OOP Rubric, Engineering Practices | You are here |
| 📝 **Homework Lessons** | All 13 assignments mapped to rubric | [Open]({{site.baseurl}}/cs111/2026/03/18/index.html) |
| 🏰 **FA1 & FA2** | SkyKingdom + Interaction Design | [Open]({{site.baseurl}}/cs111/2026/03/18/cs111-accounts.html) |
| 🐺 **Red Riding Hood** | Final Project — Full Engine Architecture | [Open]({{site.baseurl}}/cs111/setup) |

---

## 🛠️ Software Engineering Practices {#sdlc}

### Planning & Agile Workflow
As **Scrummer**, I owned the team's sprint planning process end to end:

- **Checklists & Burndowns:** Maintained weekly burndown charts to track completion rate and flag blockers before they became blockers for teammates
- **Planning Changes:** Revised sprint scope twice based on live demo feedback — removing a power-up mechanic in Week 22 to protect the core collision system
- **Mini-Lesson Documentation:** Wrote comic-style inline documentation for every major method, explaining the *why* behind each design decision, not just the *what*

### Software Development Lifecycle (SDLC)
| Phase | What I Did |
|:------|:-----------|
| **Source Control** | Feature branches per task, commits after every working change |
| **Forking** | Forked instructor base repo, maintained sync with upstream |
| **Branching** | Isolated `level-transition`, `npc-reaction`, `destroy-system` branches |
| **Building** | Incremental builds tested locally before any push |
| **Testing & Verification** | Each game object verified for collision logic before merging |
| **Pull Requests** | Selective PRs submitted to instructor fork for structured assessment |
| **Merging** | Squash merges to keep main branch history clean |
| **Deployment** | Deployed via GitHub Pages after passing all verification checks |

### Retrospective Engineering Practices
- **Live Reviews:** Participated in weekly team code reviews identifying memory leaks in level transitions
- **Demos:** Presented SkyKingdom and Red Riding Hood live to class
- **Code Reviews:** Flagged hardcoded NPC positions in teammate's code, refactored to JSON config
- **Revising Plans:** Revised `handleCollision` logic after FA2 feedback to add directional response

---

## 🏗️ OOP & Coding Practices Evidence {#oop}

### Inheritance Hierarchy
```text
GameObject                    ← Base class (Level 1)
  └── Character               ← extends GameObject (Level 2)
        ├── Player            ← extends Character (Level 3)
        └── Wolf              ← extends Character (Level 3)
```

### Classes & Constructor Chaining
```javascript
class Wolf extends Character {
    constructor(data, gameEnv) {
        super(data, gameEnv); // constructor chaining ✅
        this.type = "Wolf";
        this.isHostile = true; // boolean flag ✅
    }

    // Method with 2 parameters ✅
    handleCollision(other, direction) {
        if (other instanceof Player) {        // condition ✅
            if (this.distanceTo(other) < 50) { // nested condition ✅
                this.reaction("hostile");
            }
        }
    }

    update() {
        super.update(); // method overriding ✅
        this.checkProximity();
    }
}
```

### Coding Practices Checklist

| Principle | Evidence |
|:----------|:---------|
| **Single Responsibility** | `update()` only updates state, `draw()` only renders, `handleCollision()` only handles collision |
| **Data-Driven Design** | GameBuilder Object Literals initialize all game objects |
| **OOP** | `GameObject` base class with full inheritance hierarchy |
| **State Management** | Game loop states, pause conditions, level transition flags |

### Full OOP Rubric

| Requirement | Evidence | ✅ |
|:------------|:---------|:----|
| 2+ custom classes | `Player`, `Wolf` both extend `Character` | ✅ |
| Methods with 2+ params | `handleCollision(other, direction)` | ✅ |
| Object instantiation | GameLevel config objects | ✅ |
| 2+ level inheritance | `GameObject → Character → Player/Wolf` | ✅ |
| Method overriding | `update()`, `draw()`, `handleCollision()` all overridden | ✅ |
| Constructor chaining | `super(data, gameEnv)` in all subclasses | ✅ |

---

## 🔢 Data Types, Operators & Control Structures {#data}

### Data Types

| Type | Example | Where Used |
|:-----|:--------|:-----------|
| `Number` | `x: 100, velocity: 3, score: 0` | Position, physics, scoring |
| `String` | `"Wolf"`, `"hostile"`, sprite paths | Names, states, asset paths |
| `Boolean` | `isJumping`, `isPaused`, `isVulnerable` | Game state flags |
| `Array` | `[wolf, player, barrier1, barrier2]` | Game object collections |
| `JSON Object` | `{ name: "Wolf", hitbox: { width: 40 } }` | NPC configuration |

### Operators
```javascript
// Mathematical operators — physics
this.x += this.velocity * deltaTime;
this.y += this.gravity * Math.pow(deltaTime, 2);

// String operations — asset paths
const spritePath = `${baseUrl}/assets/${this.name}.png`;

// Boolean expressions — compound conditions
if (this.isColliding && !this.isPaused && direction === "left") {
    this.handleCollision(other, direction);
}
```

### Control Structures
```javascript
// Iteration — game loop
gameObjects.forEach(obj => {
    obj.update();
    obj.draw();
});

// Nested conditions — NPC logic
if (other.type === "Player") {
    if (player.hasItem("basket")) {
        if (this.distanceTo(player) < this.hitbox.range) {
            this.reaction("friendly");
        }
    } else {
        this.reaction("hostile");
    }
}
```

### Input/Output

| I/O Type | Implementation |
|:---------|:--------------|
| **Canvas Rendering** | `draw()` renders every object each frame via `requestAnimationFrame` |
| **Keyboard Events** | Event listeners on `keydown`/`keyup` for player movement |
| **GameEnv Config** | Object literals configure level dimensions and game state |
| **API Calls** | Leaderboard and NPC AI calls via `fetch()` |

---

*Anika Seksaria · CSSE Sprint 6 · Spring 2026 · Mira Costa CS 111 · GameEngine v1.1*