import time, psutil, json, threading
import numpy as np

class GreenTraceCollector:
    def __init__(self, tdp=45, region_carbon_intensity=400):
        self.tdp = tdp 
        self.carbon_factor = region_carbon_intensity  # gCO2/kWh
        self.sampling = False
        self.records = []

    def _get_power(self):
        # Research-grade Linear Power Model
        cpu = psutil.cpu_percent(interval=0.1)
        power_w = (self.tdp * 0.1) + (self.tdp * 0.9 * (cpu / 100))
        return power_w

    def profile(self, func, name):
        self.sampling = True
        samples = []
        
        def collect():
            while self.sampling:
                samples.append(self._get_power())
                time.sleep(0.05)

        thread = threading.Thread(target=collect)
        thread.start()
        
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        
        self.sampling = False
        thread.join()
        
        duration = end - start
        avg_p = np.mean(samples)
        energy_j = avg_p * duration
        # Convert Joules to kWh then to gCO2
        carbon = (energy_j / 3600000) * self.carbon_factor
        
        return {
            "Label": name,
            "Duration_S": round(duration, 4),
            "Energy_J": round(energy_j, 4),
            "Carbon_gCO2": round(carbon, 6),
            "Power_Timeline": samples
        }

# Example use cases
def task_a(): [i**2 for i in range(1000000)]
def task_b(): np.square(np.arange(1000000))

collector = GreenTraceCollector()
data = [collector.profile(task_a, "Legacy_List"), collector.profile(task_b, "Optimized_NumPy")]

with open("data.json", "w") as f:
    json.dump(data, f)
print("Saved data.json")
