# 24-Hour Live Digital Clock System

Author: Omowu George Omajuwa.
Matric Number: 25/18097.
Department: Software Engineering.
Course: SEN 201.

The 24-Hour Live Digital Clock System is a simple console-based application developed using Python. The system continuously displays the current system time in a 24-hour format and updates the display every second in real time.

This project was developed as part of a Software Engineering (SEN) assignment to demonstrate the application of the Software Development Life Cycle (SDLC).

The **Waterfall SDLC model** was used for this project because the system requirements were clearly defined and remained unchanged throughout development. Each phase was completed sequentially before moving to the next.

---

## Software Development Life Cycle (SDLC)

### 1. Requirement Analysis

The objective of the system is to display the current system time continuously in a 24-hour format.

#### Functional Requirements

- The system shall retrieve the current system time.
- The system shall display hours, minutes, and seconds.
- The system shall update the displayed time every second.
- The system shall run continuously until manually stopped.

#### Non-Functional Requirements

- The system should be lightweight and efficient.
- The display should be clear and readable.
- The system should respond in real time.

---

### 2. System Design

The system was designed using a procedural approach.

#### Design Tools

##### Flowchart

![Flowchart of the 24-Hour Live Digital Clock System](24-Hour-Digital-Clock-Flowchart.jpg)

##### Pseudocode [Click here to view the pseudocode](24-Hour-Digital-Clock-Pseudocode.txt)

The design outlines the logical flow of the system, from retrieving the current time to formatting and continuously updating the display.

---

### 3. Implementation

The system was implemented using the Python programming language.

#### Technologies Used

- Programming Language: Python 3.x
- Libraries:
  - `time` — to retrieve and format system time
  - `os` — to clear the console screen

The program retrieves the current system time, formats it with leading zeros where necessary, and updates the display every second.

---

### 4. Testing

The system was tested manually by running the program and observing the output.

#### Test Cases

- Correct display of current time
- Accurate updating every second
- Proper formatting with leading zeros
- Continuous execution without crashing

All test cases passed successfully.

---

### 5. Deployment

To run the application:

```bash
python 24-Hour\ Digital\ Clock.py
```

The program can be executed on any platform with Python installed (Windows, Linux, macOS).

---

### 6. Maintenance

Future enhancements to the system may include:

- Adding date display
- Adding AM/PM switch
- Supporting a graphical interface
- Improving cross-platform compatibility

---

## Repository Contents

- `24-Hour-Digital-Clock.py` — Python source code
- `24-Hour-Digital-Clock-Pseudocode.txt` — Pseudocode for system logic
- `24-Hour-Digital-Clock-Flowchart.jpg` — Flowchart representation of the system
- `README.md` — Project documentation
