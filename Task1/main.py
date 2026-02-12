import time
import matplotlib.pyplot as plt
from avlset import AVLSet


def measure_operations(sizes):
    """Measure the time complexity of various AVL operations."""
    insert_times = []
    find_times = []
    find_min_times = []
    find_next_times = []
    
    for size in sizes:
        avl = AVLSet()
        
        # Measure insert time
        start = time.perf_counter()
        for i in range(size):
            avl.insert(i, f"value_{i}")
        insert_time = time.perf_counter() - start
        insert_times.append(insert_time)
        
        # Measure find time (search for middle element repeatedly)
        start = time.perf_counter()
        for i in range(size):
            avl.find(size // 2)
        find_time = time.perf_counter() - start
        find_times.append(find_time)
        
        # Measure find_min time
        start = time.perf_counter()
        for i in range(size):
            avl.find_min()
        find_min_time = time.perf_counter() - start
        find_min_times.append(find_min_time)
        
        # Measure find_next time
        start = time.perf_counter()
        for i in range(size):
            avl.find_next(i)
        find_next_time = time.perf_counter() - start
        find_next_times.append(find_next_time)
        
        print(f"Size {size:6d}: insert={insert_time:.6f}s, find={find_time:.6f}s, "
              f"find_min={find_min_time:.6f}s, find_next={find_next_time:.6f}s")
    
    return insert_times, find_times, find_min_times, find_next_times


def main():
    """Test AVL Set complexity with increasing input sizes."""
    print("=" * 80)
    print("AVL Set - Operation Complexity Analysis")
    print("=" * 80)
    print("\nMeasuring operation times for various input sizes...\n")
    
    sizes = [1000, 5000, 10000, 20000, 50000]
    insert_times, find_times, find_min_times, find_next_times = measure_operations(sizes)
    
    # Create the graph
    plt.figure(figsize=(12, 7))
    plt.plot(sizes, insert_times, marker='o', linewidth=2.5, label='insert()', markersize=8)
    plt.plot(sizes, find_times, marker='s', linewidth=2.5, label='find()', markersize=8)
    plt.plot(sizes, find_min_times, marker='^', linewidth=2.5, label='find_min()', markersize=8)
    plt.plot(sizes, find_next_times, marker='D', linewidth=2.5, label='find_next()', markersize=8)
    
    plt.xlabel('Number of Elements', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('AVL Set - Operation Complexity vs Input Size', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11, loc='best')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('avlset_complexity_graph.png', dpi=300, bbox_inches='tight')
    print(f"\n✓ Graph saved as 'avlset_complexity_graph.png'")
    plt.show()


if __name__ == "__main__":
    main()
