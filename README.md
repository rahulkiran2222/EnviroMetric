🌱 EnviroMetric AI

High-Fidelity Software Energy Profiling & Carbon Quantification Framework
![alt text](https://img.shields.io/badge/%F0%9F%A4%97%20Live%20Research-Dashboard-yellow?style=for-the-badge)

![alt text](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)

![alt text](https://img.shields.io/badge/Field-Sustainable_Computing-emerald?style=for-the-badge)

![alt text](https://img.shields.io/badge/Stage-PhD_Research_Candidate-orange?style=for-the-badge)

EnviroMetric AI is an advanced systems-level framework designed to quantify the relationship between software execution patterns and hardware energy expenditure. Developed for Green Software Engineering research.

Explore the Dashboard • View Methodology • Request Collaboration

</div>
📑 Executive Summary
Current software optimization focuses almost exclusively on Latency (Time) and Memory (Space). EnviroMetric AI introduces a third dimension: Energy Efficiency. By utilizing hardware-aware linear regression models, this framework translates raw CPU/GPU load cycles into measurable Joules and Carbon Dioxide Equivalents (
C
O
2
e
CO 
2
​	
 e
).

🏗 system Architecture
code
Mermaid
graph TD
    A[User Code / Browser Use Case] --> B{EnviroMetric Collector}
    B --> C[Multi-threaded Power Sampler]
    B --> D[Process Orchestrator]
    C --> E[CPU TDP & Frequency Analysis]
    D --> F[Selenium Automation Engine]
    E --> G[(Research Data JSON)]
    F --> G
    G --> H[Gradio Dashboard]
    H --> I[Plotly Statistical Visualization]
    H --> J[Carbon Impact Estimation]
🔬 Mathematical Foundation
To ensure scientific validity in restricted environments (Cloud/WSL), EnviroMetric utilizes the Energy Proportionality Model:

E
t
o
t
a
l
=
∫
t
=
0
T
[
P
i
d
l
e
+
(
P
m
a
x
−
P
i
d
l
e
)
×
μ
(
t
)
]
d
t
E 
total
​	
 =∫ 
t=0
T
​	
 [P 
idle
​	
 +(P 
max
​	
 −P 
idle
​	
 )×μ(t)]dt

Where:

E
t
o
t
a
l
E 
total
​	
 
 is the total energy consumed in Joules.

P
i
d
l
e
P 
idle
​	
 
 is the static power leakage (15% of TDP).

μ
(
t
)
μ(t)
 is the instantaneous CPU utilization percentage at time 
t
t
.

T
T
 is the total execution window.

🛠 Tech Stack & Requirements

Core Technologies
Technology	Application
Python 3.9+	Core logic and data processing.
Gradio / Plotly	High-end research dashboard and visualization.
Selenium	Automated browser benchmarking (Chrome/Edge).
Psutil	Low-level system resource monitoring.
NumPy	High-speed calculation of energy integrals.
Hardware Requirements
Architecture: x86_64 or ARM64.

Sensor Access: User permissions for system-level resource polling.

Internet: Required for Webdriver synchronization and Hugging Face hosting.

📊 Features & Research Capabilities
[01] Joule-Level Granularity: Provides energy consumption data at sub-second intervals.

[02] Comparative Analytics: Automated "A/B Testing" between different browser engines or code versions.

[03] Carbon Mapping: Real-time conversion of energy into Carbon Footprint based on Global Grid Intensity (
400
g
/
k
W
h
400g/kWh
).

[04] Power Profiles: Visualizes the "Power Signature" of an application to identify inefficient CPU spikes.

🚀 Installation & Local Execution

1. Environment Setup
code
Bash
git clone https://github.com/RahulGK/EnviroMetric.git
cd EnviroMetric
pip install -r requirements.txt
2. Execution of Research Protocol
Run the real-world browser benchmark (Chrome vs Edge):

code
Bash
python real_test.py
3. Data Visualization
Visit the Hugging Face Dashboard.

Upload the generated envirometric_data.json.

Analyze the Statistical Distribution and Power Timelines.

📂 Project Structure
code
Text
EnviroMetric/
├── core/
│   └── collector.py       # Measurement logic & Power Modeling
├── benchmarks/
│   └── real_test.py       # Selenium-based Browser Use Cases
├── dashboard/
│   └── app.py             # Gradio Visualization Engine
├── data_samples/
│   └── example_data.json  # Pre-generated research data
├── requirements.txt       # Project Dependencies
└── README.md              # Documentation
🎯 Future Research Roadmap

Quantization Impact: Measuring energy savings of int8 vs fp16 in LLM inference.

Network Energy: Quantifying the energy cost of HTTP requests vs WebSockets.

OS Variance: Comparing Windows Kernel vs. Linux Scheduler energy management.
👨‍🔬 Author
Rahul GK

"The greenest code is the code that never has to run. The second greenest is the code that runs with EnviroMetric."
