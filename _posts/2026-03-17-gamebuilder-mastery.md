---
layout: post
title: "GameBuilder Mastery: FA1, FA2 & Red Riding Hood Final"
description: "Sprint 6 Final Portfolio — Anika Seksaria. FA1 SkyKingdom, FA2 Interaction Design, Red Riding Hood Final, CS 111 college credit evidence."
author: anika
date: 2026-03-17
categories: [Sprint6, GameBuilder, OOP, CS111]
---

# 🎮 GameBuilder Mastery: Sprint 6 Final Portfolio

**Author:** Anika Seksaria | **Role:** Scrummer | **Sprint:** 6 — Weeks 19–25  
**Team:** Anika (Scrummer) · Mateo (Designer) · Rashi (Technologist)  
**Course Alignment:** Mira Costa CS 111 — JavaScript OOP, Control Structures, Data Types

---

## 📋 Table of Contents

| Section | Topic |
|---|---|
| [1. CS 111 Rubric Alignment](#cs111-rubric) | Every learning objective checked |
| [2. My Role](#my-role) | Scrummer — level transitions & memory management |
| [3. FA1 — SkyKingdom](#fa1-skykingdom) | Mini-game: 4 configured objects |
| [4. FA2 — Interaction Design](#fa2-interaction) | NPC proximity trigger |
| [5. Live Game Demo](#live-demo) | Embedded runtime game |
| [6. Red Riding Hood Final](#red-riding-hood) | 3-level final project |
| [7. OOP Deep Dive](#oop-deep-dive) | Inheritance, overriding, super() |
| [8. CS Concepts Evidence](#cs-concepts) | Every data type, operator, control structure |
| [9. Retrospective](#retrospective) | Engineering takeaways |

---

## CS 111 Rubric — Every Objective Met {#cs111-rubric}

> This portfolio is structured to meet **Mira Costa CS 111** learning objectives for college credit. The table below maps each requirement to specific evidence in my code.

### Object-Oriented Programming

| CS 111 Requirement | My Evidence | ✅ |
|---|---|---|
| 2+ custom classes extending base classes | `GameLevelCustom` (FA1/FA2), `Player extends Character`, `Wolf extends Character` (Final) | ✅ |
| Methods with 2+ parameters | `handleCollision(other, direction)` on Player and Wolf | ✅ |
| Instantiate game objects in GameLevel config | `this.classes = [Background, Player, Npc, Barrier]` — FA1 | ✅ |
| 2+ level inheritance hierarchy | `GameObject → Character → Player` and `→ Wolf` | ✅ |
| Override parent methods | Player overrides `update()` with WASD; Wolf overrides `update()` with waypoint AI | ✅ |
| Constructor chaining with `super()` | `super(data, gameEnv)` in Player and Wolf constructors | ✅ |

### Control Structures, Data Types, Operators

| CS 111 Requirement | My Evidence | ✅ |
|---|---|---|
| Iteration | `this.cookies.forEach(...)` in `destroy()`, `requestAnimationFrame` game loop | ✅ |
| Conditionals | `if (this.score === 5)` win condition, `if (this.dialogueSystem)` NPC guard | ✅ |
| Nested Conditions | `if (cookie && cookie.parentNode)` in `destroy()` | ✅ |
| Numbers | `STEP_FACTOR: 1000`, `SCALE_FACTOR: 5`, `x: 100, y: 300`, WASD keycodes `87, 65, 83, 68` | ✅ |
| Strings | `greeting: 'Welcome to Space Kingdom!'`, `id: 'dbarrier_1'`, all `src` paths | ✅ |
| Booleans | `visible: true`, `fromOverlay: true`, `wonLevel`, `isPaused`, `continue = false` | ✅ |
| Arrays | `this.classes = [...]`, `dialogues: [...]`, `this.cookies`, Wolf waypoints | ✅ |
| Objects (JSON) | `playerData`, `bgData`, `npcData1`, `dbarrier_1` — all deeply nested object literals | ✅ |
| Math operators | `Math.PI / 16` (rotation), `Math.sqrt(dx*dx + dy*dy)` (Wolf distance) | ✅ |
| String operations | `path + "/images/gamebuilder/sprites/astro.png"` — concatenation on every `src` | ✅ |
| Boolean expressions | `cookie && cookie.parentNode`, `!isPaused && isGrounded` | ✅ |
| Keyboard Input | `keypress: { up: 87, left: 65, down: 83, right: 68 }` — WASD (FA2 activation) | ✅ |
| Canvas Rendering | `GameEnvBackground` + Player `draw()` renders sprite frames to canvas each tick | ✅ |
| Code Comments | JSDoc `@class`, `@description`, `@type {Object}` on every block — >10% density | ✅ |

---

## My Role: Scrummer {#my-role}

On the **Red Riding Hood Final Project**, our team divided ownership by technical domain:

| Team Member | Role | Technical Ownership |
|---|---|---|
| **Anika (me)** | **Scrummer** | Level transitions, `destroy()` memory management, Scrum timeline, GitHub Issues |
| Mateo | Designer | UI/UX, asset curation, CSS overlay styling |
| Rashi | Technologist | Physics logic, collision math, Wolf AI waypoints |

---

## FA1 — SkyKingdom Mini-Game {#fa1-skykingdom}

> **GitHub Issue #1:** `S4 Anika Seksaria — FA1: Mini Game SkyKingdom` · Closed ✅  

### Game Concept

**SpaceKingdom** is a custom exploration level set in a celestial cloud environment. The concept focuses on a "low-gravity" experience where an astronaut navigates a serene sky atmosphere. Goal: a visually distinct, floaty movement style that feels different from a standard ground-level game.

### FA1 Requirements — 4 Configured Objects

| Object | Role | Key Decision |
|---|---|---|
| **Background** | Cloud texture (1280×720) | Establishes Sky Kingdom theme and world bounds |
| **Player (Astro)** | Main astronaut character | `STEP_FACTOR: 1000` — intentional floaty physics |
| **NPC (Astronaut1)** | Stationary guide at `(500, 300)` | `SCALE_FACTOR: 4` — slightly smaller, reads as landmark |
| **Barrier (dbarrier_1)** | Collision boundary | `fromOverlay: true` — enables physics mapping |

### FA1 Full Code — JSDoc Annotated

```javascript
import GameEnvBackground from '/assets/js/GameEnginev1/essentials/GameEnvBackground.js';
import Player           from '/assets/js/GameEnginev1/essentials/Player.js';
import Npc              from '/assets/js/GameEnginev1/essentials/Npc.js';
import Barrier          from '/assets/js/GameEnginev1/essentials/Barrier.js';

class GameLevelCustom {
  constructor(gameEnv) {
    const path = gameEnv.path;

    const bgData = {
      name:   "custom_bg",
      src:    path + "/images/gamebuilder/bg/clouds.jpg",
      pixels: { height: 720, width: 1280 }
    };

    const playerData = {
      id:             'playerData',
      src:            path + "/images/gamebuilder/sprites/astro.png",
      SCALE_FACTOR:   5,
      STEP_FACTOR:    1000,
      ANIMATION_RATE: 50,
      INIT_POSITION:  { x: 100, y: 300 },
      pixels:         { height: 770, width: 513 },
      orientation:    { rows: 4, columns: 4 },
      down:      { row: 0, start: 0, columns: 3 },
      right:     { row: 2, start: 0, columns: 3 },
      left:      { row: 1, start: 0, columns: 3 },
      up:        { row: 3, start: 0, columns: 3 },
      hitbox:    { widthPercentage: 0.2, heightPercentage: 0.2 },
      keypress:  { up: null, left: null, down: null, right: null }
    };

    this.classes = [
      { class: GameEnvBackground, data: bgData    },
      { class: Player,            data: playerData },
      { class: Npc,               data: { id: 'NPC', SCALE_FACTOR: 4, INIT_POSITION: { x: 500, y: 300 } } },
      { class: Barrier,           data: { id: 'dbarrier_1', fromOverlay: true } },
    ];
  }
}