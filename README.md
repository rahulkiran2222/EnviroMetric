<div align="center">
🌱 EnviroMetric AI

Sustainable Computing: Algorithmic Energy Profiling & Carbon Quantification
![alt text](https://img.shields.io/badge/%F0%9F%A4%97%20Live%20Research-Dashboard-yellow?style=for-the-badge)

![alt text](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)

![alt text](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

![alt text](https://img.shields.io/badge/Status-PhD_Admissions_Candidate-emerald?style=for-the-badge)

EnviroMetric AI is an advanced systems-level framework designed to quantify the relationship between software execution patterns and hardware energy expenditure.

Interactive Dashboard • Methodology • GitHub Pages

</div>
📄 I. Research Abstract
Current software optimization paradigms focus almost exclusively on Temporal Complexity (
O
(
n
)
O(n)
 time) and Spatial Complexity (Memory usage). EnviroMetric AI introduces Energy Proportionality as a primary metric for software quality. This project provides a rigorous pipeline for measuring CPU power draw and carbon intensity, enabling researchers to identify "carbon-heavy" algorithmic patterns and browser-engine inefficiencies.

🚀 II. Key Features
High-Frequency Sampling: 20Hz polling of system-level power states via TDP modeling.

Comparative Benchmarking: A/B testing suite for different browsers (Chrome vs. Edge) and algorithms.

Carbon Intensity Mapping: Real-time conversion of Joules to 
C
O
2
e
CO 
2
​	
 e
 using global grid intensity coefficients.

Power Signatures: Visualizes instantaneous wattage spikes to pinpoint inefficient code blocks.

🛠 III. Technical Stack
Category	Technology	Purpose
Language	Python 3.10+	Core logic and numerical processing.
System Interface	psutil	Low-level hardware resource monitoring.
Automation	Selenium	Reproducible browser-engine benchmarking.
Math & Data	NumPy, Pandas	Statistical aggregation and energy integration.
Visualization	Gradio, Plotly	Academic dashboard and Pareto charting.
🧪 IV. Scientific Methodology
The framework employs an Indirect Energy Modeling approach to calculate the total energy consumed (
E
E
) in Joules:

E
=
∫
t
=
0
T
(
P
s
t
a
t
i
c
+
(
P
m
a
x
−
P
s
t
a
t
i
c
)
⋅
μ
(
t
)
)
d
t
E=∫ 
t=0
T
​	
 (P 
static
​	
 +(P 
max
​	
 −P 
static
​	
 )⋅μ(t))dt

Variables:

P
s
t
a
t
i
c
P 
static
​	
 
: System-specific idle power (15% of CPU TDP).

P
m
a
x
P 
max
​	
 
: Maximum Thermal Design Power (TDP) of the processor.

μ
(
t
)
μ(t)
: Instantaneous CPU utilization percentage.

T
T
: Total execution time in seconds.

🏗 V. Framework Architecture
code
Mermaid
graph LR
    A[Use Case Script] --> B[EnviroMetric Collector]
    B --> C{Sampling Engine}
    C --> D[CPU Load / Frequency]
    C --> E[Selenium UI Events]
    D & E --> F[(Data Serialization: JSON)]
    F --> G[Hugging Face Dashboard]
    G --> H[Statistical Analysis]
    G --> I[Carbon Reporting]
📦 VI. Project Structure
code
Text
EnviroMetric/
├── core/
│   └── collector.py       # Measurement Engine & Power Models
├── benchmarks/
│   └── real_test.py       # Selenium Browser Use-Cases
├── dashboard/
│   └── app.py             # Gradio Visualization Logic
├── sample_data/
│   └── browser_data.json  # Pre-generated Research Dataset
├── requirements.txt       # Framework Dependencies
└── index.html             # Research Landing Page
🏁 VII. Getting Started

1. Installation
code
Bash
git clone https://github.com/RahulGK/EnviroMetric.git
pip install -r requirements.txt
2. Local Experimentation
Run the automated browser energy comparison:

code
Bash
python benchmarks/real_test.py
3. Analysis
Upload the resulting envirometric_data.json to the Live Dashboard to view the energy distributions and power timelines.

📋 VIII. Requirements
Hardware: Intel/AMD x86_64 or Apple Silicon (M-series).

Software: Python 3.9+, Google Chrome / Microsoft Edge (for Selenium tests).

System Permissions: The collector requires access to system monitoring APIs (Standard user).

🎯 IX. Future Research Directions

Quantization Impact: Measuring energy variance in int8 vs fp16 LLM inference.

Network Energy: Quantifying the cost of HTTP protocols vs gRPC.

OS Schedulers: Investigating energy management differences between Windows 11 and Ubuntu 24.04.
👨‍🔬 X. Contact & Attribution
Rahul GK

"The most efficient line of code is the one that is never executed. The second most efficient is profiled by EnviroMetric."
[© EnviroMetric AI - MIT License]
