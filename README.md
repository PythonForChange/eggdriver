# eggdriver

Your proyect trusted driver.

## Quick start

### 1. Install eggdriver

    pip install eggdriver

### 2. Create the file **eggconfig.py** and then write in it the following lines:

    username, password = "{your user}", "{your password}"

    pypi = {<br>
        "user" : "{your PyPI user or "\__token__"}",
        "password" : "{your PyPI password or token}"
    }

## NQS inside

### NQS: Natural Quantum Script. A special domain programming language that aims to simplify the first contact with quantum computing

Natural Quantum Script is a special domain programming language that aims to simplify the first contact with quantum computing for people who have prior knowledge in quantum circuits, but not in quantum software development.

Scripts written in NQS seek to visually resemble quantum circuits as much as possible. For example:

    q0 q1
    X
    H
    .--- X
    c1

NQS is initially based on Qiskit, but seeks to go mainstream in the future. This is an OS project whose initial goal was to make it easier to write basic scripts in Qiskit and to bridge the gap for people who don't dare to delve into quantum computing.
