import time
import psutil
import pandas as pd
import threading
import numpy as np

class EnviroProfiler:
    def __init__(self, tdp=65):
        self.tdp = tdp
        self.sampling = False
        self.data_points = []

    def _sample_power(self):
        while self.sampling:
            cpu_usage = psutil.cpu_percent(interval=0.1)
            # Power Model: P_static + (P_dynamic * usage)
            power = (self.tdp * 0.1) + (self.tdp * 0.9 * (cpu_usage / 100))
            self.data_points.append(power)

    def run_experiment(self, func, label):
        self.data_points = []
        self.sampling = True
        
        # Start background power sampling
        thread = threading.Thread(target=self._sample_power)
        thread.start()
        
        start_time = time.perf_counter()
        func() # Run the actual use case
        end_time = time.perf_counter()
        
        self.sampling = False
        thread.join()
        
        duration = end_time - start_time
        avg_power = np.mean(self.data_points) if self.data_points else 0
        energy_j = avg_power * duration
        
        return {
            "Version": label,
            "Duration_Sec": duration,
            "Avg_Power_W": avg_power,
            "Energy_Joules": energy_j,
            "Samples": self.data_points
        }

# --- USE CASES ---
def use_case_v1():
    # Legacy: Recursive Fibonacci
    def fib(n):
        if n<=1: return n
        return fib(n-1) + fib(n-2)
    fib(30)

def use_case_v2():
    # Optimized: Iterative Fibonacci
    a, b = 0, 1
    for _ in range(30):
        a, b = b, a + b

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    profiler = EnviroProfiler(tdp=45)
    results = []
    
    for _ in range(5): # Multiple trials for statistical significance
        results.append(profiler.run_experiment(use_case_v1, "Legacy_Recursive"))
        results.append(profiler.run_experiment(use_case_v2, "Optimized_Iterative"))
    
    df = pd.DataFrame(results)
    # Explode the samples for time-series analysis
    df.to_json("research_data.json") 
    print("Research complete. File generated: research_data.json")
