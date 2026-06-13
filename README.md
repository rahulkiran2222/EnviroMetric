# 🌱 EnviroMetric: Sustainable Software Analytics

Quantifying the Environmental Impact of Computational Logic

Hugging Face Space Python 3.9+ License: MIT Research

EnviroMetric is a high-fidelity energy profiling framework designed to bridge
the gap between software engineering and environmental sustainability. It allows
researchers and developers to measure the Joule-level consumption of different
software implementations, helping identify "Carbon-heavy" code.

🔬 Research Abstract

As the global energy consumption of data centers continues to rise, the need for
"Green Software" is paramount. EnviroMetric provides an automated pipeline for:

1.  Algorithmic Benchmarking: Comparing Legacy vs. Optimized implementations.
2.  Browser Energy Profiling: Measuring the power draw of web-based environments
    (Chrome vs. Edge vs. Firefox).
3.  Hardware-Aware Modeling: Using CPU TDP (Thermal Design Power) and dynamic
    load sampling to estimate energy proportionality.

🚀 Live Dashboard

Access the interactive visualization suite hosted on Hugging Face: 👉
EnviroMetric Live Dashboard

🛠️ System Architecture

| Component          | Technology            | Role                                          |
| :----------------- | :-------------------- | :-------------------------------------------- |
| **Data Collector** | `psutil`, `threading` | High-frequency CPU load & frequency sampling. |
| **Automation**     | `Selenium`            | Reproducible browser & UI use-case testing.   |
| **Analytics**      | `NumPy`, `Pandas`     | Statistical processing of Joule consumption.  |
| **Visualization**  | `Gradio`, `Plotly`    | Comparative research dashboards.              |

📊 Methodology

To ensure academic rigor, EnviroMetric utilizes a Linear Power Model:

P_{total} = P_{static} + (P_{dynamic} \times \mu_{usage})

Where:

  - P_{static}: The idle power baseline (calculated as 15% of TDP).
  - P_{dynamic}: The variable power range (85% of TDP).
  - \mu_{usage}: Real-time CPU utilization percentage.
  - Carbon Estimation: Energy is converted to CO_2e using the global average
    grid intensity coefficient (400g/kWh).

📸 Dashboard Preview

| Energy Distribution                                                                | Power Over Time                                                            |
| :--------------------------------------------------------------------------------: | :------------------------------------------------------------------------: |
| ![Energy Comparison](https://img.shields.io/badge/Visual-Energy_Bar_Chart-emerald) | ![Timeline](https://img.shields.io/badge/Visual-Power_Timeline_Graph-blue) |
| *Compare Joules between App versions*                                              | *Identify power spikes during execution*                                   |

💻 How to Run Locally

1. Clone the Repository

git clone https://github.com/RahulGK/EnviroMetric.git
cd EnviroMetric

2. Install Dependencies

pip install psutil numpy selenium webdriver-manager

3. Run a Research Experiment

Modify the real_test.py with your CPU's TDP and run:

python real_test.py

4. Visualize

Upload the generated envirometric_data.json to the Hugging Face Dashboard.

📈 Research Use Cases

  - Case 1: Comparing Recursive vs Iterative algorithms to see if "shorter time"
    always means "less energy."
  - Case 2: Measuring the impact of Dark Mode vs Light Mode on display-related
    energy (for OLED).
  - Case 3: Analyzing the energy overhead of Garbage Collection in different
    programming languages.

🤝 Contributing

This project is part of a PhD Research Application. If you are a professor or
researcher interested in Sustainable Computing, feel free to reach out.

📜 License

This project is licensed under the MIT License - see the LICENSE file for
details.

📩 Contact

Rahul GK
GitHub Profile | Hugging Face
