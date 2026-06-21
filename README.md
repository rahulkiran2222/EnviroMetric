# 🌱 EnviroMetric AI

<div align="center">

### Algorithmic Energy Profiling and Carbon-Aware Software Analysis

**Measuring computational energy, power behavior, and carbon impact across software workloads**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Research](https://img.shields.io/badge/Research-Sustainable%20Software%20Engineering-success.svg)

---

*A framework for estimating energy consumption and carbon emissions from software execution traces.*

</div>

---

# Overview

**EnviroMetric AI** is a lightweight experimental framework for studying the relationship between software execution patterns and energy consumption.

Traditional software engineering primarily focuses on:

* Time complexity
* Memory complexity
* Throughput

However, modern computing systems increasingly require understanding a third dimension:

> **Energy complexity**

EnviroMetric AI provides an extensible pipeline for estimating energy consumption and carbon impact from CPU utilization traces and execution workloads, enabling comparative studies across browsers, algorithms, and software configurations.

---

# Research Motivation

Software systems may exhibit identical runtimes while consuming substantially different amounts of energy.

This framework investigates:

* Algorithmic energy behavior
* Browser engine efficiency
* CPU utilization dynamics
* Carbon-equivalent emissions
* Energy-aware software optimization

---

# Features

## Execution Profiling

Capture:

* CPU utilization
* Memory usage
* Execution time
* Frequency statistics

---

## Comparative Benchmarking

Evaluate:

* Chrome vs Edge
* Different algorithms
* Alternative implementations

---

## Carbon Impact Estimation

Convert energy estimates into carbon-equivalent emissions using configurable grid intensity coefficients.

---

## Visualization

Generate:

* Power timelines
* Energy distributions
* Comparative plots
* Pareto analysis

---

# System Architecture

```text
Workload
     │
     ▼
EnviroMetric Collector
     │
     ├── CPU Utilization
     ├── Memory Statistics
     ├── Execution Time
     │
     ▼
Energy Model
     │
     ▼
JSON Dataset
     │
     ▼
Visualization Layer
     │
     ▼
Statistical Analysis
```

---

# Methodology

The framework uses indirect energy estimation:

[
E=\int_0^T \left(P_{static}+(P_{max}-P_{static})\mu(t)\right)dt
]

where:

| Variable     | Description           |
| ------------ | --------------------- |
| (P_{static}) | Estimated idle power  |
| (P_{max})    | Maximum processor TDP |
| (\mu(t))     | CPU utilization       |
| (T)          | Execution time        |

Outputs:

* Energy (Joules)
* Average power (Watts)
* Carbon-equivalent emissions

---

# Tech Stack

| Category        | Technology     |
| --------------- | -------------- |
| Language        | Python 3.10+   |
| Profiling       | psutil         |
| Automation      | Selenium       |
| Data Processing | NumPy, Pandas  |
| Visualization   | Plotly, Gradio |
| Storage         | JSON           |

---

# Repository Structure

```bash
EnviroMetricAI/

├── core/
│   └── collector.py
│
├── benchmarks/
│   └── browser_benchmark.py
│
├── dashboard/
│   └── app.py
│
├── sample_data/
│   └── benchmark_data.json
│
├── visualizations/
│
├── requirements.txt
│
└── README.md
```

---

# Getting Started

### Clone Repository

```bash
git clone https://github.com/RahulGK/EnviroMetricAI
cd EnviroMetricAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Benchmark

```bash
python benchmarks/browser_benchmark.py
```

---

# Example Applications

* Browser energy analysis
* Algorithmic comparisons
* Carbon-aware software design
* Sustainable software engineering experiments

---

# Future Directions

### Quantization-aware LLM energy analysis

* FP32
* FP16
* INT8

---

### Cross-platform studies

* Windows
* Linux
* macOS

---

### Carbon-aware scheduling

Dynamic workload optimization based on energy efficiency.

---

### Hardware-level measurements

Integration with:

* Intel RAPL
* NVIDIA NVML
* Apple powermetrics

---

# Author

### Rahul Kiran G

AI Research • Sustainable Software Engineering • Energy-Aware Computing

---

> Toward energy-conscious software systems.
