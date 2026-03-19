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

## 📋 CS111 Portfolio Navigation

| Section | Link to Specific Blog |
|:---|:---|
| **1. Rubric & Evidence** | [Stay on this Page](#cs111-rubric) |
| **2. CS111 Hub** | [Open CS111 Index Hub]({{site.baseurl}}/cs111/2026/03/18/index.html) |
| **3. Account Setup** | [Open CS111 Accounts Page]({{site.baseurl}}/cs111/2026/03/18/cs111-accounts.html) |
| **4. Tools Setup** | [Open Setup Page]({{site.baseurl}}/cs111/setup) |

---

## CS 111 Rubric — Every Objective Met {#cs111-rubric}

### Object-Oriented Programming Evidence
* **Custom Classes:** `Player extends Character`, `Wolf extends Character`.
* **Methods:** `handleCollision(other, direction)` uses two parameters.
* **Chaining:** `super(data, gameEnv)` used in constructors.
* **Hierarchy:** 3-level inheritance (`GameObject` -> `Character` -> `Player`).

---

## My Role: Scrummer {#my-role}

As **Scrummer**, I managed the technical "seams." My biggest contribution was the **level transition engine** and the cleanup system. I ensured that the game remained performant by cleaning up memory between levels.

---

## FA1 & FA2 — SkyKingdom & Interaction {#fa1-skykingdom}

FA1 established the environment. FA2 added the interaction. By configuring the `hitbox` and adding a `reaction` function, I enabled the NPC to trigger dialogue when the player is in range.

---

## OOP Deep Dive {#oop-deep-dive}

### Inheritance Hierarchy
```text
GameObject (base)
  └── Character extends GameObject
        ├── Player extends Character
        └── Wolf extends Character
Retrospective {#retrospective}
The most technically demanding thing I built was the memory management system. It forced me to understand that live DOM elements don't self-clean when a level ends. This project proved that effective game architecture relies as much on "cleaning up" as it does on "building up."
Anika Seksaria · CSSE Sprint 6 · Spring 2026 · Mira Costa CS 111 · GameEngine v1.1