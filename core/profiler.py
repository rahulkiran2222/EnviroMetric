import time
import psutil
import platform
import pandas as pd

class EnviroMetric:
    def __init__(self, tdp=25):
        self.tdp = tdp  # Thermal Design Power of your CPU
        self.system_info = platform.uname()._asdict()

    def get_instant_power(self):
        """Estimate power based on CPU load and frequency."""
        cpu_pct = psutil.cpu_percent(interval=None) / 100.0
        # Simple linear power model: P = P_idle + (P_max - P_idle) * load
        # Research standard: Base power is ~20% of TDP
        p_idle = self.tdp * 0.2
        p_dynamic = self.tdp * 0.8 * cpu_pct
        return p_idle + p_dynamic

    def measure(self, func, name, iterations=5):
        results = []
        for i in range(iterations):
            start_time = time.perf_counter()
            start_power_samples = []
            
            # Execute and sample power every 0.1s
            # Note: For PhD level, use a thread to sample while func runs
            # Simplified version for stability:
            func() 
            
            end_time = time.perf_counter()
            duration = end_time - start_time
            power_draw = self.get_instant_power() 
            joules = power_draw * duration
            
            results.append({
                "Label": name,
                "Iteration": i + 1,
                "Duration_S": round(duration, 4),
                "Energy_J": round(joules, 4),
                "Power_W": round(power_draw, 2)
            })
        return results
