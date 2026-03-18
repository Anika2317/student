---
---

layout: opencs
title: Red Riding Hood Game 
permalink: /ridinghoodport
codemirror: true
--- 
# The Red Riding Hood Game
### Made by Anika, Rashi, and Mateo! 

Our game is <span style="color:red"> Red Riding Hood </span><br>
The game consists of **two** levels! 
- Level 1: <span style="color:red">The Revelation of Red Riding Hood </span><br>
Red Riding has to collect cookies for her grandma, throughout the woods, to move on to level 2

- Level 2:<span style="color:red"> The Chase </span><br>
Red Riding has to successfully follow the path to her grandma's house, without colliding with the wolf


**Mateo** (Designer): UI/UX, Asset Curation, and CSS Overlay Styling. <br>
**Rashi** (Technologist): Physics Logic, Collision Mathematics, and AI Waypoints. <br>
**Anika** (Scrummer): Level Transitions, Memory Management, and Project Timeline. <br>

Red Riding Hood (Player.js): Uses a keypress object to track WASD inputs. It handles 8-way movement (up, down, left, right, and diagonals). <br>
<br>
The Evil Wolf (Wolf.js): Uses an array of Waypoints. It calculates the distance to its next target and moves toward it automatically without human input.


```python
%%js
// GAME_RUNNER: Help Red collect cookies and reach the cottage! | hide_edit: false

import GameControl from '/assets/js/GameEnginev1/essentials/GameControl.js';
import GameEnvBackground from '/assets/js/GameEnginev1/essentials/GameEnvBackground.js';
import Player from '/assets/js/GameEnginev1/essentials/Player.js';
import Character from '/assets/js/GameEnginev1/essentials/Character.js';

// --- SHARED CLASSES (Combined from your level files) ---

class FloorItem {
    constructor(x, y, data, container) {
        this.x = x; this.y = y;
        this.element = document.createElement('img');
        this.element.src = data.image;
        this.element.style.position = 'absolute';
        this.element.style.left = x + 'px';
        this.element.style.top = y + 'px';
        this.element.style.width = '50px';
        this.element.style.zIndex = '100';
        if (container) container.appendChild(this.element);
    }
}

class PathBarrier {
    constructor(x, y, w, h, gameEnv) {
        this.x = x; this.y = y; this.width = w; this.height = h;
        this.ctx = gameEnv.ctx;
    }
    draw(debug = false) {
        if (debug) {
            this.ctx.fillStyle = "rgba(255, 0, 0, 0.5)"; 
            this.ctx.fillRect(this.x, this.y, this.width, this.height);
        }
    }
}

class Wolf extends Character {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this.velocity = { x: 0, y: 0 };
        this.speed = data.SPEED || 2;
        this.waypoints = null;
        this.waypointIndex = 0;
    }
    buildWaypoints() {
        const W = this.gameEnv.innerWidth;
        const H = this.gameEnv.innerHeight;
        return [
            { x: W * 0.09, y: H * 0.80 }, { x: W * 0.14, y: H * 0.72 },
            { x: W * 0.32, y: H * 0.41 }, { x: W * 0.50, y: H * 0.22 },
            { x: W * 0.58, y: H * 0.72 }, { x: W * 0.90, y: H * 0.13 }
        ];
    }
    update() {
        if (!this.waypoints) {
            this.waypoints = this.buildWaypoints();
            this.position.x = this.waypoints[0].x;
            this.position.y = this.waypoints[0].y;
            this.waypointIndex = 1;
        }
        const target = this.waypoints[this.waypointIndex];
        const dx = target.x - this.position.x;
        const dy = target.y - this.position.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < this.speed + 1) {
            this.waypointIndex = (this.waypointIndex + 1) % this.waypoints.length;
        } else {
            this.position.x += (dx / dist) * this.speed;
            this.position.y += (dy / dist) * this.speed;
        }
        this.draw();
    }
}

// --- LEVEL 1: THE REVELATION ---
class GameLevelRedRidingHood1 {
  constructor(gameEnv) {
    this.gameEnv = gameEnv;
    const width = gameEnv.innerWidth;
    const height = gameEnv.innerHeight;
    const path = gameEnv.path;
    const container = gameEnv.gameContainer;

    this.score = 0;

    // Title Overlay
    this.titleElement = document.createElement('div');
    this.titleElement.style.cssText = "position:absolute; top:40px; width:100%; text-align:center; color:red; font-size:30px; font-weight:900; font-family:Courier New; text-shadow:2px 2px black; z-index:999;";
    this.titleElement.innerHTML = "The Revelation of Little Red Riding Hood";
    container.appendChild(this.titleElement);

    // Score Overlay
    this.scoreElement = document.createElement('div');
    this.scoreElement.style.cssText = "position:absolute; bottom:20px; left:20px; color:red; font-size:20px; font-weight:bold; font-family:Courier New; z-index:999;";
    this.scoreElement.innerHTML = "Cookies Collected: 0";
    container.appendChild(this.scoreElement);

    const image_data_wood = { name: 'woods', src: path + "/images/gamify/ridinghood/woods.png", pixels: { height: 580, width: 1038 } };
    const sprite_data_red = {
      id: 'Red', src: path + "/images/gamify/ridinghood/red.png",
      SCALE_FACTOR: 5, STEP_FACTOR: 1000, ANIMATION_RATE: 50,
      INIT_POSITION: { x: 50, y: height * 0.75 },
      pixels: { height: 192, width: 144 }, orientation: { rows: 4, columns: 3 },
      keypress: { up: 87, left: 65, down: 83, right: 68 }
    };

    this.classes = [{ class: GameEnvBackground, data: image_data_wood }, { class: Player, data: sprite_data_red }];

    this.cookies = [];
    const cookieItem = { image: path + '/images/gamify/ridinghood/cookie.png' };
    [0.1, 0.3, 0.5, 0.7, 0.9].forEach(pos => {
        this.cookies.push(new FloorItem(width * pos, height * 0.8, cookieItem, container));
    });
  }

  update() {
    const player = this.gameEnv.gameObjects.find(obj => obj instanceof Player);
    for (let i = this.cookies.length - 1; i >= 0; i--) {
        const c = this.cookies[i];
        if (player && !(player.position.x + 50 < c.x || player.position.x > c.x + 50 || player.position.y + 50 < c.y || player.position.y > c.y + 50)) {
            c.element.remove();
            this.cookies.splice(i, 1);
            this.score++;
            this.scoreElement.innerHTML = "Cookies Collected: " + this.score;
            if (this.score === 5) alert("Success! Switch to Level 2 in the menu.");
        }
    }
  }
}

// --- LEVEL 2: THE CHASE ---
class GameLevelRedRidingHood2 {
  constructor(gameEnv) {
    this.gameEnv = gameEnv;
    const path = gameEnv.path;
    const width = gameEnv.innerWidth;
    const height = gameEnv.innerHeight;
    const container = gameEnv.gameContainer;

    this.wonGame = false;
    this.redStartPosition = { x: 50, y: height * 0.75 };
    this.cottageZone = { x: width * 0.82, y: 0, width: width * 0.15, height: height * 0.25 };

    // Barrier logic from your code
    this.barriers = [
      new PathBarrier(0, 0, width * 0.28, height * 0.70, gameEnv),
      new PathBarrier(width * 0.75, height * 0.55, width * 0.22, height * 0.37, gameEnv)
    ];

    const image_data_chase = { name: 'chase', src: path + "/images/gamify/ridinghood/chase.png", pixels: { height: 580, width: 1038 } };
    const sprite_data_red = {
      id: 'Red', src: path + "/images/gamify/ridinghood/red.png",
      SCALE_FACTOR: 5, STEP_FACTOR: 1000, ANIMATION_RATE: 50,
      INIT_POSITION: { x: 50, y: height * 0.75 },
      pixels: { height: 192, width: 144 }, orientation: { rows: 4, columns: 3 },
      keypress: { up: 87, left: 65, down: 83, right: 68 }
    };
    const sprite_data_wolf = {
      id: 'Wolf', src: path + "/images/gamify/ridinghood/wolfff.png",
      SCALE_FACTOR: 3.5, STEP_FACTOR: 1000, ANIMATION_RATE: 8,
      INIT_POSITION: { x: width * 0.09, y: height * 0.82 },
      pixels: { height: 395, width: 632 }, orientation: { rows: 1, columns: 1 },
      SPEED: 2
    };

    this.classes = [
      { class: GameEnvBackground, data: image_data_chase },
      { class: Player, data: sprite_data_red },
      { class: Wolf, data: sprite_data_wolf }
    ];
  }

  update() {
    const player = this.gameEnv.gameObjects.find(obj => obj instanceof Player);
    const wolf = this.gameEnv.gameObjects.find(obj => obj instanceof Wolf);

    // Win check
    if (player && !this.wonGame && player.position.x > this.cottageZone.x && player.position.y < this.cottageZone.height) {
      this.wonGame = true;
      alert("CHAPTER CLOSED. Red knew the fairytale better.");
    }

    // Wolf Collision
    if (player && wolf) {
        const dx = player.position.x - wolf.position.x;
        const dy = player.position.y - wolf.position.y;
        if (Math.sqrt(dx*dx + dy*dy) < 45) {
            player.position.x = this.redStartPosition.x;
            player.position.y = this.redStartPosition.y;
        }
    }

    // Barrier Collisions
    this.barriers.forEach(barrier => {
        if (player && player.position.x < barrier.x + barrier.width && player.position.x + 30 > barrier.x && player.position.y < barrier.y + barrier.height && player.position.y + 30 > barrier.y) {
            player.position.x -= player.velocity.x;
            player.position.y -= player.velocity.y;
        }
    });
  }

  draw() { this.barriers.forEach(b => b.draw(false)); }
}

export const gameLevelClasses = [GameLevelRedRidingHood1, GameLevelRedRidingHood2];
export { GameControl };
```
