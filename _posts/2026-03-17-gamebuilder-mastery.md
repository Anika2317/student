---
layout: post
title: "GameBuilder Mastery: FA1, FA2 & Red Riding Hood Final"
description: "Sprint 6 Final Portfolio — Anika Seksaria. Covers FA1 SkyKingdom Mini-Game, FA2 Interaction Design, Red Riding Hood three-level final project, and complete CS 111 Mira Costa college credit evidence."
author: Anika Seksaria
date: 2026-03-17
permalink: /gamebuilder-mastery/
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

> **Why Scrummer is technical, not just administrative:**  
> My code runs at every level boundary. The `destroy()` function and state transitions are mine. If my inter-level systems break, Mateo's visuals and Rashi's physics have nowhere to land.  
> Every GitHub Issue was moved from **Backlog → Mini Game Tasks → Done** only when committed code actually passed — not when it was merely submitted.

---

## FA1 — SkyKingdom Mini-Game {#fa1-skykingdom}

> **GitHub Issue #1:** `S4 Anika Seksaria — FA1: Mini Game SkyKingdom` · Closed ✅  
> **Repo:** `Rashig-1804/new_csse2_team`

### Game Concept

**SpaceKingdom** is a custom exploration level set in a celestial cloud environment. The concept focuses on a "low-gravity" experience where an astronaut navigates a serene sky atmosphere. Goal: a visually distinct, floaty movement style that feels different from a standard ground-level game.

### FA1 Requirements — 4 Configured Objects

| Object | Role | Key Decision |
|---|---|---|
| **Background** | Cloud texture (1280×720) | Establishes Sky Kingdom theme and world bounds |
| **Player (Astro)** | Main astronaut character | `STEP_FACTOR: 1000` — intentional floaty physics |
| **NPC (Astronaut1)** | Stationary guide at `(500, 300)` | `SCALE_FACTOR: 4` — slightly smaller, reads as landmark |
| **Barrier (dbarrier_1)** | Collision boundary | `fromOverlay: true` — enables physics mapping |

### Key Configuration Decisions

- **`STEP_FACTOR: 1000`** — double the default value. Deliberate design choice to simulate zero-gravity drift. The player overshoots slightly by intention.
- **`SCALE_FACTOR: 5` (player) vs `4` (NPC)** — size differential makes the player visually dominant, NPC reads as a distant guide landmark.
- **Player at `(100, 300)`, NPC at `(500, 300)`** — creates a built-in left-to-right spatial goal without requiring any written instructions.
- **`fromOverlay: true` on barrier** — critical boolean flag. Without it, the barrier exists in the scene visually but has zero physics effect.
- **NPC `hitbox: { widthPercentage: 0.0, heightPercentage: 0.0 }`** — decorative only in FA1. This specific decision was then *changed* in FA2 to create the interaction trigger.

### FA1 Full Code — JSDoc Annotated

```javascript
/**
 * @class GameLevelCustom
 * @description FA1: SkyKingdom Mini-Game.
 * Configured objects: One Background (clouds), One Player (Astro),
 * One NPC (Astronaut1), One Barrier (dbarrier_1).
 * Key theme: low-gravity floaty movement via STEP_FACTOR: 1000.
 */
import GameEnvBackground from '/assets/js/GameEnginev1/essentials/GameEnvBackground.js';
import Player           from '/assets/js/GameEnginev1/essentials/Player.js';
import Npc              from '/assets/js/GameEnginev1/essentials/Npc.js';
import Barrier          from '/assets/js/GameEnginev1/essentials/Barrier.js';

class GameLevelCustom {
  constructor(gameEnv) {
    const path = gameEnv.path;  // STRING: base path for asset resolution

    /** @type {Object} bgData — ONE BACKGROUND: Cloud texture */
    const bgData = {
      name:   "custom_bg",                                    // STRING
      src:    path + "/images/gamebuilder/bg/clouds.jpg",    // STRING concatenation (+)
      pixels: { height: 720, width: 1280 }                   // NUMBERS in nested OBJECT
    };

    /** @type {Object} playerData — ONE PLAYER: Astronaut with floaty physics */
    const playerData = {
      id:             'playerData',
      src:            path + "/images/gamebuilder/sprites/astro.png",
      SCALE_FACTOR:   5,     // NUMBER: large for visual prominence
      STEP_FACTOR:    1000,  // NUMBER: 2× default — deliberate floaty physics
      ANIMATION_RATE: 50,
      INIT_POSITION:  { x: 100, y: 300 },   // OBJECT with NUMBER coords
      pixels:         { height: 770, width: 513 },
      orientation:    { rows: 4, columns: 4 },
      // Direction map — OBJECTS with NUMBER row indices + MATH (/) for rotation
      down:      { row: 0, start: 0, columns: 3 },
      right:     { row: 2, start: 0, columns: 3 },
      left:      { row: 1, start: 0, columns: 3 },
      up:        { row: 3, start: 0, columns: 3 },
      downRight: { row: 1, start: 0, columns: 3, rotate: Math.PI / 16 }, // MATH /
      downLeft:  { row: 0, start: 0, columns: 3, rotate: -Math.PI / 16 },
      hitbox:    { widthPercentage: 0.2, heightPercentage: 0.2 },
      keypress:  { up: null, left: null, down: null, right: null } // disabled in FA1
    };

    /** @type {Object} npcData1 — ONE NPC: Decorative guide, no dialogue in FA1 */
    const npcData1 = {
      id:            'Astronaut1',
      src:           path + "/images/gamebuilder/sprites/astro.png",
      SCALE_FACTOR:  4,                         // Slightly smaller — landmark role
      INIT_POSITION: { x: 500, y: 300 },        // Center-right — spatial goal
      // Math.min() guards row index against exceeding sheet bounds
      right:    { row: Math.min(1, 4 - 1), start: 0, columns: 3 },
      hitbox:   { widthPercentage: 0.0, heightPercentage: 0.0 }, // No trigger in FA1
      greeting: "", dialogues: []
    };

    /** @type {Object} dbarrier_1 — ONE BARRIER: Physical boundary */
    const dbarrier_1 = {
      id:          'dbarrier_1',
      x: 315, y: 42, width: 228, height: 117,  // NUMBERS: precise coordinates
      visible:     true,          // BOOLEAN: renders in scene
      fromOverlay: true,          // BOOLEAN: enables physics mapping (critical!)
      hitbox: { widthPercentage: 0.0, heightPercentage: 0.0 }
    };

    // ARRAY: engine iterates this.classes on every game loop tick (ITERATION)
    this.classes = [
      { class: GameEnvBackground, data: bgData    },
      { class: Player,            data: playerData },
      { class: Npc,               data: npcData1   },
      { class: Barrier,           data: dbarrier_1 },
    ];
  }
}

export const gameLevelClasses = [GameLevelCustom];
```

---

## FA2 — Interaction Design {#fa2-interaction}

> **GitHub Issue #2:** `S4 Anika Seksaria — FA2: Interaction Design` · Closed ✅  
> **Repo:** `Rashig-1804/new_csse2_team`

### What FA2 Required

FA2 built directly on the FA1 codebase with three targeted modifications:

1. **One defined interaction** — proximity-based player/NPC collision
2. **One observable reaction** — `showReactionDialogue()` overlay state change
3. **Loop integration documentation** — interaction running in the Update Phase

### FA2 Modifications (Delta from FA1)

| What Changed | FA1 Value | FA2 Value | Why |
|---|---|---|---|
| Player `keypress.up` | `null` | `87` (W key) | Re-enable WASD movement |
| Player `keypress.left` | `null` | `65` (A key) | Re-enable WASD movement |
| Player `keypress.down` | `null` | `83` (S key) | Re-enable WASD movement |
| Player `keypress.right` | `null` | `68` (D key) | Re-enable WASD movement |
| NPC `hitbox.widthPercentage` | `0.0` | `0.1` | Creates trigger zone |
| NPC `hitbox.heightPercentage` | `0.0` | `0.2` | Creates trigger zone |
| NPC `greeting` | `""` | `'Welcome to Space Kingdom!'` | Dialogue content |
| NPC `dialogues` | `[]` | `['Welcome to Space Kingdom!']` | Array of responses |
| NPC `reaction()` | not present | function added | Trigger handler |
| NPC `interact()` | not present | function added | E/Enter handler |

> **Key insight:** Two number changes (`0.0 → 0.1` and `0.0 → 0.2`) on the hitbox produce an entirely new game mechanic. This is data-driven design — behavior flows from data, not from rewriting logic.

### FA2 Interaction Logic — Annotated

```javascript
// FA2 NPC additions

const npcData1 = {
  id:       'Astronaut1',
  greeting: 'Welcome to Space Kingdom!',  // STRING added in FA2

  hitbox: {
    widthPercentage:  0.1,  // was 0.0 in FA1 — now creates trigger zone (NUMBER)
    heightPercentage: 0.2,
  },

  dialogues: ['Welcome to Space Kingdom!'],  // ARRAY of strings

  /**
   * reaction() — fires when player enters NPC hitbox
   * Called by the engine's Update Phase, ~60 times per second
   * Demonstrates: CONDITIONAL inside game loop ITERATION
   */
  reaction: function() {
    if (this.dialogueSystem) {       // CONDITIONAL: truthy boolean guard
      this.showReactionDialogue();   // state change — dialogue overlay renders
    } else {
      console.log(this.greeting);   // fallback output for debugging
    }
  },

  /**
   * interact() — fires on E/Enter keypress
   * Demonstrates: CONDITIONAL checking object property
   */
  interact: function() {
    if (this.dialogueSystem) {
      this.showRandomDialogue();  // cycles through dialogues ARRAY
    }
  }
};

// Keypress enabled: WASD as ASCII NUMBER keycodes
keypress: { up: 87, left: 65, down: 83, right: 68 }
```

### FA2 — Game Loop Integration

The proximity check runs inside the engine's **Update Phase** approximately 60 times per second. Every frame, the engine calculates whether the player's bounding box intersects the NPC's hitbox. When the condition is true, `reaction()` fires and the dialogue system state changes.

This is the canonical CSSE example of a **conditional embedded inside iteration** — they are not separate concepts, they are the same execution path in game logic.

---

## Live Game Demo {#live-demo}

> **Run the SkyKingdom level below.** Use **WASD** to move the astronaut. Walk toward the NPC guide to trigger the "Welcome to Space Kingdom!" interaction.

{% assign runner_id = "skykingdom_demo" %}
{% assign challenge = "Run the SkyKingdom level! Use WASD to move the Astro player. Walk up to the NPC guide to trigger the proximity interaction added in FA2." %}
{% assign code %}
// FA2: SkyKingdom with interaction enabled
import GameControl from '/assets/js/GameEnginev1/essentials/GameControl.js';
import GameEnvBackground from '/assets/js/GameEnginev1/essentials/GameEnvBackground.js';
import Player from '/assets/js/GameEnginev1/essentials/Player.js';
import Npc from '/assets/js/GameEnginev1/essentials/Npc.js';
import Barrier from '/assets/js/GameEnginev1/essentials/Barrier.js';

class SkyKingdomLevel {
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
      downRight: { row: 1, start: 0, columns: 3, rotate: Math.PI / 16 },
      downLeft:  { row: 0, start: 0, columns: 3, rotate: -Math.PI / 16 },
      hitbox:    { widthPercentage: 0.2, heightPercentage: 0.2 },
      keypress:  { up: 87, left: 65, down: 83, right: 68 }
    };

    const npcData1 = {
      id:            'Astronaut1',
      greeting:      'Welcome to Space Kingdom!',
      src:           path + "/images/gamebuilder/sprites/astro.png",
      SCALE_FACTOR:  4,
      ANIMATION_RATE: 50,
      INIT_POSITION: { x: 500, y: 300 },
      pixels:        { height: 770, width: 513 },
      orientation:   { rows: 4, columns: 4 },
      down:  { row: 0, start: 0, columns: 3 },
      right: { row: Math.min(1, 4 - 1), start: 0, columns: 3 },
      left:  { row: Math.min(2, 4 - 1), start: 0, columns: 3 },
      up:    { row: Math.min(3, 4 - 1), start: 0, columns: 3 },
      hitbox:    { widthPercentage: 0.1, heightPercentage: 0.2 },
      dialogues: ['Welcome to Space Kingdom!'],
      reaction: function() {
        if (this.dialogueSystem) { this.showReactionDialogue(); }
        else { console.log(this.greeting); }
      },
      interact: function() {
        if (this.dialogueSystem) { this.showRandomDialogue(); }
      }
    };

    const dbarrier_1 = {
      id: 'dbarrier_1',
      x: 315, y: 42, width: 228, height: 117,
      visible: true,
      hitbox: { widthPercentage: 0.0, heightPercentage: 0.0 },
      fromOverlay: true
    };

    this.classes = [
      { class: GameEnvBackground, data: bgData    },
      { class: Player,            data: playerData },
      { class: Npc,               data: npcData1   },
      { class: Barrier,           data: dbarrier_1 },
    ];
  }
}

export const gameLevelClasses = [SkyKingdomLevel];
export { GameControl };
{% endassign %}

{% include game-runner.html runner_id=runner_id challenge=challenge code=code %}

---

## Red Riding Hood Final Project {#red-riding-hood}

### Project Overview

| Property | Detail |
|---|---|
| **Game Name** | The Revelation of Little Red Riding Hood |
| **Levels** | 3 — Cookie Collection → Wolf Maze → Resolution |
| **Team Repo** | `Rashig-1804/new_csse2_team` |
| **Development Method** | SDLC + Agile Scrum (GitHub Kanban) |

### SDLC — Development Process

**1. Planning & Ideation**  
Mapped the fairytale to game mechanics before writing code. Level 1 = collect 5 cookies. Level 2 = navigate invisible maze barriers while Wolf AI chases. Every win condition was defined in writing first — this is the planning phase of the SDLC.

**2. Data-Driven Design**  
All dimensions, speeds, and paths stored in Object Literals — `sprite_data_red`, `playerData`. Changing the character's size requires editing one value; the rest of the game updates automatically. This is the Single Responsibility Principle applied to data.

**3. OOP Architecture with Inheritance**  
Both Player and Wolf use `extends Character`. The parent handles position, velocity, gravity, `update()`, and `draw()`. Player adds WASD input and score tracking. Wolf adds waypoint AI. Same physical laws, unique behaviors — core OOP design.

**4. Build, Test & Verify**  
Milestones committed to the team repo each sprint. GameBuilder used to test each level visually before integration. Bugs caught with browser console (F12) and DevTools breakpoints.

**5. Integration & Pull Requests**  
Selective Pull Requests submitted to the instructor fork after each formative was verified. FA1 (#1) and FA2 (#2) closed only when code passed.

---

### My Technical Contribution: Level Transitions & Memory Management

```javascript
/**
 * Level 1 win condition — Anika's code.
 * CONDITIONAL: triggers when score reaches 5.
 * Demonstrates: NUMBER comparison (===), BOOLEAN state flag, CONDITIONAL.
 */
if (this.score === 5) {         // NUMBER === NUMBER
  this.wonLevel = true;         // BOOLEAN: state flag updated
  this.transitionToLevel2();    // calls destroy() then loads Level 2
}

/**
 * destroy() — Memory Management.
 * Owned by Anika (Scrummer role). Runs at every level boundary.
 * 
 * Without this: Level 1 DOM elements (cookies, score text, overlays)
 * persist invisibly in Level 2 — consuming memory and firing ghost
 * collision events. This is not game-specific: same pattern exists in
 * React unmounting, DB connection teardown, network socket cleanup.
 * 
 * Demonstrates: ITERATION, NESTED CONDITIONS, BOOLEAN EXPRESSIONS.
 */
destroy() {

  // ITERATION: forEach loop over cookies ARRAY
  this.cookies.forEach(cookie => {

    // NESTED CONDITIONAL with BOOLEAN &&
    // Requires BOTH conditions true before DOM removal
    // Without this guard: runtime TypeError if cookie is detached
    if (cookie && cookie.parentNode) {
      cookie.parentNode.removeChild(cookie);
    }
  });

  // Remove UI overlays (score display, congratulations message)
  if (this.scoreDisplay)    this.scoreDisplay.remove();
  if (this.congratsOverlay) this.congratsOverlay.remove();

  // BOOLEAN: signals engine to stop running this level's loop
  this.continue = false;
}
```

> **Why `destroy()` is the most critical system in a multi-level game:**  
> Every DOM element persists in memory after a level ends unless explicitly removed. They don't render, but they consume memory and can fire ghost collision events. This pattern appears in every production software system — not just games.

---

### Game Characters

**Player — Red Riding Hood**
- Extends `Character` with `super(data, gameEnv)`
- Overrides `update()` with WASD input handling
- Overrides `handleCollision(other, direction)` with score logic
- Win condition: `if (this.score === 5)` triggers `transitionToLevel2()`

**Wolf — Rashi's AI**
- Extends `Character` with `super(data, gameEnv)`
- Overrides `update()` with waypoint array navigation
- Calculates `Math.sqrt(dx*dx + dy*dy)` each frame to find distance to next target
- Zero player input — pure conditional-inside-iteration autonomous AI

**Path Barriers — Maze**
- X/Y coordinates define invisible walls in Level 2 woods
- AABB collision: `if (colliding) velocity = 0`
- Configured with `fromOverlay: true` for physics mapping

---

## OOP Deep Dive {#oop-deep-dive}

### Inheritance Hierarchy (CS 111: 2+ levels required)

```
GameObject (base)
  └── Character extends GameObject
        ├── Player extends Character
        └── Wolf extends Character
```

This is a **3-level hierarchy** — meeting and exceeding the CS 111 requirement of 2+ levels.

### Full OOP Code — Annotated

```javascript
/**
 * Player — extends Character
 * CS 111: Inheritance, Method Override, Constructor Chaining, 2-param methods
 */
class Player extends Character {
  constructor(data, gameEnv) {
    super(data, gameEnv);     // CONSTRUCTOR CHAINING: calls Character constructor
    this.score    = 0;        // NUMBER: score tracking
    this.wonLevel = false;    // BOOLEAN: state flag
  }

  // METHOD OVERRIDE: replaces Character's default update() with WASD input
  update() {
    super.update();           // parent physics still apply (gravity, velocity)
    this.handleInput();       // adds input-driven movement on top
  }

  // METHOD OVERRIDE with 2 PARAMETERS (CS 111: Methods & Parameters)
  handleCollision(other, direction) {
    if (other.isCookie()) {             // CONDITIONAL
      this.score++;                     // NUMBER increment
      other.destroy();
      if (this.score === 5) {           // NESTED CONDITIONAL: win check
        this.wonLevel = true;           // BOOLEAN
        this.transitionToLevel2();
      }
    }
  }
}

/**
 * Wolf — extends Character
 * CS 111: Inheritance, Method Override, Constructor Chaining
 * Autonomous AI using waypoint ARRAY — no player input
 */
class Wolf extends Character {
  constructor(data, gameEnv) {
    super(data, gameEnv);           // CONSTRUCTOR CHAINING
    this.waypoints     = data.waypoints;  // ARRAY: AI targets
    this.waypointIndex = 0;               // NUMBER: current target index
  }

  // METHOD OVERRIDE: replaces update() with waypoint-following AI
  update() {
    super.update();    // parent physics still apply
    const target = this.waypoints[this.waypointIndex];  // ARRAY access
    const dx   = target.x - this.x;   // MATH subtraction
    const dy   = target.y - this.y;
    const dist = Math.sqrt(dx*dx + dy*dy);  // MATH: *, +, sqrt
    if (dist < 10) {                        // CONDITIONAL: reached waypoint?
      this.waypointIndex++;                 // NUMBER increment
    }
  }
}
```

### Why Inheritance (not just copy-paste)

Both Player and Wolf need position, velocity, gravity, canvas drawing, and lifecycle management. Without `extends Character`, that code would be duplicated twice — any change to physics would need to be applied in two places. Inheritance means we write it once and both classes get it automatically. The `super()` call chains the constructor upward so Character initializes the shared properties before Player or Wolf adds their own.

---

## CS Concepts — Complete Evidence Map {#cs-concepts}

> Every concept below maps to a specific, real line in FA1, FA2, or the Final Project — not generic examples.

### Control Structures

**Iteration**
```javascript
// Final Project — destroy(): forEach over cookies ARRAY
this.cookies.forEach(cookie => {
  if (cookie && cookie.parentNode) {
    cookie.parentNode.removeChild(cookie);
  }
});
// Engine: requestAnimationFrame loop (~60fps) — iteration that runs the whole game
```

**Conditionals**
```javascript
// Final: win condition check
if (this.score === 5) { this.transitionToLevel2(); }

// FA2: NPC reaction guard
if (this.dialogueSystem) { this.showReactionDialogue(); }
```

**Nested Conditions**
```javascript
// Final destroy(): two-level boolean guard
if (cookie && cookie.parentNode) {   // outer: cookie exists
  cookie.parentNode.removeChild(cookie);  // inner: safe to remove
}
// Without &&: TypeError crash if cookie is already detached from DOM
```

### Data Types

**Numbers**
```javascript
STEP_FACTOR:    1000,    // movement speed — 2× default for floaty physics
SCALE_FACTOR:   5,       // sprite scale
INIT_POSITION:  { x: 100, y: 300 },  // initial position
ANIMATION_RATE: 50,      // frame cycling speed
keypress: { up: 87, left: 65, down: 83, right: 68 }  // ASCII keycodes
```

**Strings**
```javascript
greeting: 'Welcome to Space Kingdom!',   // NPC dialogue
id:       'dbarrier_1',                  // object identifier
src:      path + "/images/.../astro.png" // asset path (string concatenation)
```

**Booleans**
```javascript
visible:     true,   // barrier renders in scene
fromOverlay: true,   // enables physics mapping (critical!)
wonLevel:    false,  // game state flag (set to true on win)
continue:    false,  // signals engine to stop level loop
isPaused:    false,  // freezes game loop when true
```

**Arrays**
```javascript
this.classes = [Background, Player, Npc, Barrier];  // game objects (iterated by engine)
dialogues:   ['Welcome to Space Kingdom!'];           // NPC dialogue strings
this.cookies = [...];                                 // collectibles (iterated in destroy)
this.waypoints = [...];                               // Wolf AI navigation targets
```

**Objects (JSON)**
```javascript
// Every entity is a deeply nested object literal
const playerData = {
  pixels:        { height: 770, width: 513 },   // nested object
  INIT_POSITION: { x: 100, y: 300 },            // nested object
  hitbox:        { widthPercentage: 0.2, heightPercentage: 0.2 }, // nested object
  down:          { row: 0, start: 0, columns: 3 }  // nested object
};
```

### Operators

**Mathematical**
```javascript
rotate: Math.PI / 16        // division: diagonal sprite rotation angle
rotate: -Math.PI / 16       // negation: mirror rotation for opposite direction
Math.sqrt(dx*dx + dy*dy)    // multiplication + addition + sqrt: Wolf distance calc
Math.min(1, 4 - 1)          // subtraction + min: NPC row index guard
```

**String Operations**
```javascript
// + concatenation on every src field
src: path + "/images/gamebuilder/bg/clouds.jpg"
src: path + "/images/gamebuilder/sprites/astro.png"
```

**Boolean Expressions**
```javascript
cookie && cookie.parentNode   // &&: both must be true
!isPaused && isGrounded       // &&, !: compound state check
if (this.dialogueSystem)      // truthy evaluation
```

---

## Retrospective {#retrospective}

### Engineering Takeaways

Working through FA1 → FA2 → Final in sequence produced cumulative understanding that isolated exercises can't replicate.

**FA1** establishes the object structure. Four configured objects, JSDoc comments, deliberate property decisions.

**FA2** changes two values — `hitbox: 0.0 → 0.1` and `keypress: null → 87` — and produces an entirely new mechanic. This is the power of data-driven design: behavior flows from configuration, not from rewriting logic.

**Final** requires all of it working simultaneously across three levels with shared memory — which is where the `destroy()` system becomes critical.

---

The most technically demanding thing I built was the **memory management system**. It forced me to understand that a running game level is a collection of live DOM elements, event listeners, and state variables — and none of them self-clean when the level ends. The `destroy()` pattern I implemented appears throughout production software:

- **React**: `componentWillUnmount()` / `useEffect` cleanup functions
- **Database**: connection pool teardown on session end
- **Network**: socket `close()` events and resource deallocation
- **Game engines**: all major engines (Unity, Unreal) have a destroy/cleanup lifecycle

As Scrummer, I also learned that **technical ownership and project management aren't separate skills**. My level transitions are the seams holding all three technical domains together. The GitHub Kanban board was only useful when issues were honest — closed when code passed, not when it was submitted.

### SDLC Engineering Practices Used

| Practice | How I Applied It |
|---|---|
| Source Control | Daily commits to `Rashig-1804/new_csse2_team` |
| Issue Tracking | FA1 (#1) and FA2 (#2) tracked on GitHub Kanban board |
| Branching | Feature branches for each formative before merging |
| Pull Requests | Selective PRs to instructor fork after verification |
| Testing | GameBuilder visual testing + browser console (F12) |
| Retrospective | This blog post — documenting what was learned and why |

---
---

## 📚 Homework Portfolio — CS 111 Evidence

All completed homework assignments demonstrating mastery of JavaScript fundamentals:

| Assignment | Topic | Link |
|---|---|---|
| Variables | `let`, `const`, `var`, data types, DOM output | [View](/variables) |
| Math Expressions | Operators, arithmetic functions, DOM output | [View](/Math) |
| Functions | Parameters, return values, recursion, DOM | [View](/Functions) |
| Booleans | Boolean flags, conditionals, state management | [View](/Boolean) |
| Arrays (Foundations) | Array methods, push/pop, iteration | [View](/UnderstandArray) |
| Arrays (Applied) | Array manipulation, DOM rendering | [View](/Arrays) |
| Classes & Variables | Class syntax, constructor, instances | [View](/classes-Variables-HW) |
| Classes & Constructors | Inheritance, methods, cookie clicker OOP | [View](/classes-constructors-HW) |
| Data Abstraction | Functions + classes, player system | [View](/Penguins-homework) |
| Iteration | `while` loops, `for...of`, array iteration | [View](/Iteration) |
| Strings | `.length`, `.toUpperCase()`, template literals | [View](/strings-homework) |

> These homework assignments directly evidence the **Data Types, Operators, Control Structures, and OOP** requirements for Mira Costa CS 111 college credit.
*Anika Seksaria · CSSE Sprint 6 · Spring 2026 · Mira Costa CS 111 · GameEngine v1.1*
