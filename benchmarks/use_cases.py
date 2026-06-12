import numpy as np

def case_unoptimized():
    """Inefficient string concatenation"""
    s = ""
    for i in range(50000):
        s += str(i)

def case_optimized():
    """Efficient list joining"""
    return "".join([str(i) for i in range(50000)])

def run_experiment():
    from core.profiler import EnviroMetric
    engine = EnviroMetric(tdp=45) # Set to your laptop's TDP
    
    print("Running Legacy Code...")
    data_a = engine.measure(case_unoptimized, "Legacy_Concat")
    
    print("Running Optimized Code...")
    data_b = engine.measure(case_optimized, "Optimized_Join")
    
    full_df = pd.DataFrame(data_a + data_b)
    full_df.to_csv("research_data.csv", index=False)
    print("Experiment Complete. Data saved to research_data.csv")

if __name__ == "__main__":
    run_experiment()
