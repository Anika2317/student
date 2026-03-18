---
layout: post
title: Java Kernel
description: This page will teach you how to set up your Java kernel in Jupyter Notebooks.
categories: ['Kernels']
permalink: /tools/kernels/java
breadcrumb: True
---

# Install IJava 1.3.0 Kernel for Jupyter (Java 17) on WSL (Ubuntu) & macOS (Homebrew)

---

## Prerequisites

- Java 17 (OpenJDK 17) installed
- Python and Jupyter Notebook installed
- Git installed

---

## 1. Install OpenJDK 17

### WSL (Ubuntu)
~~~
sudo apt update
sudo apt install openjdk-17-jdk
java -version
~~~
### macOS(Homebrew)
~~~
brew update
brew install openjdk@17
echo 'export PATH="/usr/local/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
java -version
~~~
## 2. Install Git and Gradle
### Windows (Ubuntu)
~~~
# WSL (Ubuntu)
sudo apt install git
~~~
### macOS (Homebrew)
~~~
# macOS
brew install git
~~~
## 3. Clone the IJava Repository
~~~
git clone https://github.com/SpencerPark/IJava.git
cd IJava
git checkout v1.3.0
~~~
## 4. Build and Install IJava Kernel w/ Gradle Wrapper
~~~
chmod +x gradlew
~~~
~~~
./gradlew installKernel
~~~
## 5. Verify Kernel 
~~~
jupyter kernelspec list
~~~
## 6. Setting up Kernel in Notebook File
- Create New .ipynb file. 
- Click on select kernel (Top Right Corner)
- Select Java 
- Make a code cell
- Test following Code


~~~
System.out.println("Hello from IJava 1.3.0 with Java 17!");
~~~
---



## **Why Do We Need Both OpenJDK and IJava for Java in Jupyter?**




## 1. OpenJDK: The Java Development Kit

- **OpenJDK** is the official open-source implementation of the Java platform.
- It provides the **Java compiler (javac)** and the **Java Virtual Machine (JVM)**.
- The compiler translates your Java source code into bytecode.
- The JVM runs this bytecode on your computer.
- Without OpenJDK (or any JDK), you cannot compile or run Java programs at all.

---

## 2. IJava: The Jupyter Kernel for Java

- **IJava** is a special program that acts as a **kernel** for Jupyter notebooks.
- Jupyter itself doesn’t understand Java; it only provides the notebook interface.
- The kernel is what executes your code behind the scenes.
- IJava lets Jupyter communicate with the JVM and compile/run your Java code interactively.
- It manages compiling code on-the-fly, keeping the Java environment alive, and sending results back to the notebook interface.

---

## Why Both Are Needed Together?

- **OpenJDK** provides the essential Java tools (compiler + runtime) but **does not have any interface for Jupyter notebooks.**
- **IJava** provides the integration layer that connects Jupyter with Java, making Java interactive inside notebooks.
- Think of it like this:
  - **OpenJDK = the engine** that actually runs Java programs.
  - **IJava = the driver** that knows how to talk to Jupyter and control that engine interactively.

---

## What Happens When You Run Java in Jupyter?

1. You write Java code in a notebook cell.
2. Jupyter sends your code to the **IJava kernel**.
3. IJava uses **OpenJDK’s compiler and JVM** to compile and run your code.
4. Output or errors get sent back through IJava to the notebook to display.

---

## Summary Table

| Component      | Role                                                  |
|----------------|-------------------------------------------------------|
| OpenJDK        | Provides compiler and runtime to run Java programs.   |
| IJava Kernel   | Bridges Jupyter notebook interface and the JVM.       |
| Together       | Enable running Java interactively inside Jupyter.     |

---
