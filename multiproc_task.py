import os
import time
from multiprocessing import Pool
from filters import process_and_save

def run_multiprocessing_test(dataset_path, num_processes):
    # Fetch image paths
    images = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Setup unique output directory in home folder
    size_label = os.path.basename(dataset_path)
    output_dir = f"/home/maaroszi/output_multi_{size_label}_p{num_processes}"
    os.makedirs(output_dir, exist_ok=True)

    start_time = time.time()
    # Execute the parallel paradigm
    with Pool(processes=num_processes) as pool:
        pool.starmap(process_and_save, [(img, output_dir) for img in images])
            
    return time.time() - start_time

if __name__ == "__main__":
    # Absolute paths matching your terminal structure
    subsets = [
        "/home/maaroszi/data/subset_100", 
        "/home/maaroszi/data/subset_200", 
        "/home/maaroszi/data/subset_300", 
        "/home/maaroszi/data/subset_500"
    ]
    
    process_counts = [1, 2, 4, 8]

    print("="*70)
    print("PARADIGM 1: MULTIPROCESSING PERFORMANCE BENCHMARK")
    print("="*70)
    
    for folder in subsets:
        if not os.path.exists(folder):
            print(f"\n[!] MISSING FOLDER: {folder}")
            continue
            
        imgs = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png'))]
        print(f"\nDATASET: {os.path.basename(folder)} | TOTAL IMAGES: {len(imgs)}")
        print("-" * 65)
        print(f"{'Workers':<10} | {'Time (s)':<12} | {'Speedup (S)':<12} | {'Efficiency (E)':<12}")
        print("-" * 65)

        t_serial = 0 # To store T1 for speedup calculation
        
        for p in process_counts:
            duration = run_multiprocessing_test(folder, p)
            
            if p == 1:
                t_serial = duration
                speedup = 1.00
                efficiency = 100.0
            else:
                speedup = t_serial / duration
                efficiency = (speedup / p) * 100
                
            print(f"{p:<10} | {duration:>10.4f}s | {speedup:>12.2f} | {efficiency:>11.2f}%")
    
    print("\n" + "="*70)
    print("BENCHMARK COMPLETE")
    print("="*70)
