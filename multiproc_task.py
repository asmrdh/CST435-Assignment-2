import os
import time
from multiprocessing import Pool
from filters import process_and_save

def run_multiprocessing_test(dataset_path, num_processes):
    """
    Sets up a Process Pool and maps tasks to available CPU cores.
    """
    # Collect all valid image paths from the subset directory
    images = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Organize outputs by dataset size and core count
    size_label = os.path.basename(dataset_path)
    output_dir = f"/home/maaroszi/output_multi_{size_label}_p{num_processes}"
    os.makedirs(output_dir, exist_ok=True)

    start_time = time.time()
    
    # Initialize the Pool with the specific number of processes (1, 2, 4, 8)
    with Pool(processes=num_processes) as pool:
        # starmap allows passing multiple arguments (image path + output dir) to the function
        pool.starmap(process_and_save, [(img, output_dir) for img in images])
            
    return time.time() - start_time

if __name__ == "__main__":
    subsets = [
        "/home/maaroszi/data/subset_100", 
        "/home/maaroszi/data/subset_200", 
        "/home/maaroszi/data/subset_300", 
        "/home/maaroszi/data/subset_500"
    ]
    process_counts = [1, 2, 4, 8]

    print("="*75)
    print("PARADIGM 1: MULTIPROCESSING PERFORMANCE BENCHMARK")
    print("="*75)
    
    for folder in subsets:
        if not os.path.exists(folder): continue
            
        imgs = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png'))]
        print(f"\nDATASET: {os.path.basename(folder)} | TOTAL IMAGES: {len(imgs)}")
        print("-" * 70)
        print(f"{'Workers':<10} | {'Time (s)':<12} | {'Speedup (S)':<15} | {'Efficiency (E)':<15}")
        print("-" * 70)

        t_serial = 0 # Baseline for S = T1 / Tp
        for p in process_counts:
            duration = run_multiprocessing_test(folder, p)
            if p == 1:
                t_serial = duration
                speedup, efficiency = 1.00, 100.00
            else:
                speedup = t_serial / duration
                efficiency = (speedup / p) * 100
            print(f"{p:<10} | {duration:>10.4f}s | {speedup:>15.2f} | {efficiency:>14.2f}%")
