# README **SkyEye** - AI-Based Search and Rescue System

## Overview 
**SkyEye** is an advanced AI-powered search and rescue system designed to locate survivors in disaster-stricken areas and send immediate alerts to emergency response teams. Leveraging cutting-edge technologies in artificial intelligence, robotics, and communication networks, SkyEye aims to revolutionize the efficiency and accuracy of rescue missions, reducing response times and saving lives.

---

### Key Features

1. **Survivor Detection:**
   - Utilizes AI models trained to recognize signs of life, including body heat, movement, and vocalizations, through sensors such as infrared cameras, LiDAR, and microphones.
   - Equipped to detect survivors in challenging environments like collapsed buildings, dense forests, or underwater.

2. **Autonomous Navigation:**
   - Operates through drones, ground robots, or aquatic vehicles capable of autonomous navigation.
   - Adaptive pathfinding algorithms enable the system to maneuver through debris, navigate hazardous terrains, and access hard-to-reach locations.

3. **Real-Time Communication:**
   - Sends automated alerts with precise GPS coordinates and survivor status to emergency response teams.
   - Provides live feeds and environmental data to aid in planning rescue strategies.

4. **Multi-Unit Coordination:**
   - Deploys multiple units that communicate seamlessly to cover large areas efficiently.
   - Ensures minimal redundancy and maximum coverage through intelligent task allocation.

5. **Scalability:**
   - Can be deployed in various disaster scenarios, including earthquakes, floods, wildfires, and maritime emergencies.
   - Scalable architecture allows integration with existing rescue frameworks and technology.

---

### Benefits

- **Faster Response Times:** Rapid detection and notification reduce the critical window for survival.
- **Enhanced Safety:** Minimizes risk to human rescuers by assessing danger zones before deployment.
- **Cost-Effective Operations:** Automates key processes, reducing the reliance on large teams and expensive equipment.
- **Global Applicability:** Designed for diverse environments and disaster types, ensuring widespread usability.

---

### Vision

SkyEye seeks to be a game-changer in search and rescue operations by combining AI’s capabilities with innovative robotics and sensing technologies. The project envisions a future where no disaster survivor goes unnoticed, ensuring every life has the highest chance of being saved.

## Video
[Watch the demo on YouTube](https://youtu.be/hW3rBgcTqko)

## Versions
Add the versions that you tested the examples on.

## Setup Instructions

### Prerequisites - 
1. Rpi5, AI HAT, RpiCam
2. Projector (We used BENQ TH685)
3. Sandbox (We used 80 KG of sand over 50cm X 70cm X 30cm plastic box)
4. We hanged the projector from the ceiling, a picture of our setup can be found [here](https://drive.google.com/drive/folders/1oga1fwvLBtspIVwjxbryvHNtxSWr6N6F?usp=sharing)
5. Extra - We used 3D printed cover for the projector + Rpi. 3D models can be found [here](https://drive.google.com/drive/folders/1UvcrxFtw0vaQCFMcMy3W8CueZKsj-L-H?usp=sharing)

### Calculating Offsets
The project accepts x and y offsets to match different configurations of camera/projector for smooth mapping between different perspectives. The offsets can be given fromt he command line, and they can be calculated with:

### Variables:
- \( X \): Horizontal distance between the camera and projector (in their shared plane).
- \( Y \): Height of the camera-projector plane above the ground.
- \( \theta_c \): Camera's field of view (FOV) angle in the horizontal direction.
- \( \phi_c \): Camera's FOV angle in the vertical direction.
- \( \theta_p \): Projector's field of view (FOV) angle in the horizontal direction.
- \( \phi_p \): Projector's FOV angle in the vertical direction.
 
### Formulas:
#### Horizontal Offset \( Δ x \):
\[
Δ x = X \cdot \frac{\tan(\theta_c / 2)}{\tan(\theta_p / 2)}
\]

#### Vertical Offset \( Δ y \):
\[
Δ y = Y \cdot \frac{\tan(\phi_c / 2)}{\tan(\phi_p / 2)}
\]

## Usage
With Δ x and Δ y you can now runt he application:
```bash
X_OFFSET=<\delta x>  Y_OFFSET=<\delta y>  python community_projects/SkyEye/SkyEye.py
```
