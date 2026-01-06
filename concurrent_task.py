import os
import time
from concurrent.futures import ProcessPoolExecutor
from filters import process_and_save

def run_futures_test(dataset_path, num_workers):
    # Fetch all image paths from the directory
    images = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Define a clean output directory in the home folder
    size_label = os.path.basename(dataset_path)
    output_dir = f"/home/maaroszi/output_futures_{size_label}_w{num_workers}"
    os.makedirs(output_dir, exist_ok=True)

    start_time = time.time()
    # Use ProcessPoolExecutor to map the tasks across workers
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        # Using list comprehension to submit all tasks
        futures = [executor.submit(process_and_save, img, output_dir) for img in images]
        # Ensure all futures are completed
        for future in futures:
            future.result()
            
    return time.time() - start_time

if __name__ == "__main__":
    # Absolute paths to match your verified 'data' directory structure
    subsets = [
        "/home/maaroszi/data/subset_100", 
        "/home/maaroszi/data/subset_200", 
        "/home/maaroszi/data/subset_300", 
        "/home/maaroszi/data/subset_500"
    ]
    
    worker_counts = [1, 2, 4, 8]

    print("="*75)
    print("PARADIGM 2: CONCURRENT.FUTURES PERFORMANCE BENCHMARK")
    print("="*75)
    
    for folder in subsets:
        if not os.path.exists(folder):
            print(f"\n[!] MISSING FOLDER: {folder}")
            continue
            
        imgs = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png'))]
        print(f"\nDATASET: {os.path.basename(folder)} | TOTAL IMAGES: {len(imgs)}")
        print("-" * 70)
        print(f"{'Workers':<10} | {'Time (s)':<12} | {'Speedup (S)':<15} | {'Efficiency (E)':<15}")
        print("-" * 70)

        t_serial = 0 # Baseline for speedup
        
        for w in worker_counts:
            duration = run_futures_test(folder, w)
            
            if w == 1:
                t_serial = duration
                speedup = 1.00
                efficiency = 100.00
            else:
                speedup = t_serial / duration
                efficiency = (speedup / w) * 100
                
            print(f"{w:<10} | {duration:>10.4f}s | {speedup:>15.2f} | {efficiency:>14.2f}%")
    
    print("\n" + "="*75)
    print("BENCHMARK COMPLETE")
    print("="*75)
