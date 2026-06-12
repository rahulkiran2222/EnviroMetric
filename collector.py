import time, psutil, json, threading
import numpy as np

# We keep the name EnviroMetric!
class EnviroMetricEngine:
    def __init__(self, tdp=45):
        self.tdp = tdp 
        self.sampling = False

    def _get_power(self):
        cpu = psutil.cpu_percent(interval=None)
        return (self.tdp * 0.15) + (self.tdp * 0.85 * (cpu / 100))

    def profile(self, func, name):
        print(f"🔬 EnviroMetric is profiling: {name}...")
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
        
        return {
            "Label": name,
            "Duration_S": round(duration, 4),
            "Energy_J": round(energy_j, 4),
            "Carbon_gCO2": round((energy_j / 3600000) * 400, 6),
            "Power_Timeline": samples
        }

# --- TEST IT ---
def task_v1(): [i**2 for i in range(1000000)]
def task_v2(): np.square(np.arange(1000000))

engine = EnviroMetricEngine()
data = [engine.profile(task_v1, "Legacy_Code"), engine.profile(task_v2, "Optimized_Code")]

with open("envirometric_data.json", "w") as f:
    json.dump(data, f)
print("Done! Upload 'envirometric_data.json' to your dashboard.")        avg_p = np.mean(samples)
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
