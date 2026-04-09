## 🚗 AI-Based Autonomous Navigation System

## 📌 Project Overview

The AI-Based Autonomous Navigation System is a simulation project that demonstrates how intelligent agents (like robots or self-driving vehicles) navigate from a start point to a destination while avoiding obstacles.

The system uses a grid-based environment and implements the A* (A-Star) path planning algorithm to calculate the most efficient route.

---

## 🎯 Problem Statement

Autonomous systems must navigate safely in unknown or dynamic environments.

Challenges include:

- Finding the shortest path
- Avoiding obstacles
- Making real-time decisions

This project addresses these challenges using AI-based path planning techniques.

---

## 🌍 Industry Relevance

This project has real-world applications in:

- 🤖 Robotics navigation
- 🚗 Self-driving cars
- 📦 Warehouse automation (Amazon, Flipkart robots)
- 🚁 Drone path planning
- 🛰️ Autonomous exploration systems

It demonstrates core concepts used in AI, robotics, and intelligent systems.

---

## 🧠 Key Features

- Grid-based simulation environment
- Obstacle avoidance system
- A* path planning algorithm
- Real-time visualization using Pygame
- Interactive start and end point selection
- Efficient shortest path computation

---

## 🛠️ Tech Stack

- Programming Language: Python
- Libraries: Pygame, NumPy
- Concepts Used:
  - Artificial Intelligence
  - Path Planning Algorithms
  - Graph Search (A*)

---

## 🏗️ System Architecture

The system follows a modular architecture:

1. Environment Module
   
   - Creates grid-based simulation
   - Manages obstacles

2. Path Planning Module
   
   - Implements A* algorithm
   - Calculates optimal path

3. Navigation Module
   
   - Controls agent movement
   - Executes computed path

4. Visualization Module
   
   - Displays simulation using Pygame

---

## 📁 Folder Structure

AI-Autonomous-Navigation-System/
│
├── simulation/
│   └── environment.py
│
├── src/
│   ├── navigation.py
│   └── path_planning.py
│
├── assets/
│   └── screenshots/
│       └── demo/
│
├── outputs/
│   ├── images/
│   └── videos/
│
├── docs/
│   └── architecture.md
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore

---

## ⚙️ Installation

git clone <https://github.com/keshkarsaloni-lab/AI-Autonomous-Navigation-System>
cd AI-Autonomous-Navigation-System

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

---

## ▶️ How to Run

python main.py

---

## 🔄 Simulation Workflow

1. Run the program
2. A grid environment is displayed
3. Select start point (Green)
4. Select end point (Red)
5. Algorithm calculates shortest path
6. Agent navigates automatically
7. Final path is visualized

---

## 📊 Results

- Successfully generated shortest path using A*
- Efficient obstacle avoidance
- Smooth real-time visualization
- Accurate navigation from start to destination

---

## 📸 Screenshots

### 🔹 Empty Grid

"Empty Grid" (assets/screenshots/empty.png)

### 🔹 Start & End Selection

"Start End" (assets/screenshots/end.png)

### 🔹 Final Path Output

"Path" (assets/screenshots/path.png)

---

## 🚀 Future Improvements

- Add dynamic/moving obstacles
- Integrate computer vision (OpenCV)
- Upgrade to 3D simulation (CARLA)
- Implement machine learning-based navigation
- Real-world robot integration (ROS)

---

## 📚 Learning Outcomes

Through this project, I learned:

- Implementation of A* path planning algorithm
- Grid-based environment modeling
- AI decision-making concepts
- Simulation using Pygame
- Git & GitHub workflow
- Project structuring and documentation

---

## 👩‍💻 Author

Saloni Keshkar

- 🎓 Engineering Student (Electronics & Telecommunication)
- 💡 Interested in AI, Robotics, and Intelligent Systems

---

## ⭐ Conclusion

This project demonstrates how AI can be applied to real-world navigation problems. It serves as a strong foundation for advanced autonomous systems like self-driving vehicles and robotic navigation.