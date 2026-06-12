import gradio as gr
import pandas as pd
import plotly.express as px
import json

def analyze_energy(file):
    with open(file.name, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    
    # Energy Chart
    fig1 = px.bar(df, x="Label", y="Energy_J", color="Label", 
                 title="EnviroMetric: Energy Consumption (Joules)",
                 template="plotly_dark")
    
    # Power Timeline Chart
    timeline = data[0]['Power_Timeline']
    fig2 = px.line(y=timeline, title=f"Power Profile: {data[0]['Label']} (Watts)",
                  template="plotly_dark")
    
    # Stats
    savings = ((df['Energy_J'].max() - df['Energy_J'].min()) / df['Energy_J'].max()) * 100
    report = f"## EnviroMetric Research Report\n\n"
    report += f"Optimization achieved a **{savings:.2f}%** reduction in energy.\n\n"
    report += f"**Carbon Impact:** {df['Carbon_gCO2'].min():.6f} gCO2 (Optimized) vs {df['Carbon_gCO2'].max():.6f} gCO2 (Legacy)"
    
    return fig1, fig2, report

demo = gr.Interface(
    fn=analyze_energy,
    inputs=gr.File(label="Upload EnviroMetric JSON"),
    outputs=[gr.Plot(), gr.Plot(), gr.Markdown()],
    title="EnviroMetric: Sustainable Software Analytics",
    description="PhD Research Project: Analyzing the correlation between code efficiency and hardware power draw."
)

demo.launch()
