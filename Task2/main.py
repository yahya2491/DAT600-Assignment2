import time
import matplotlib.pyplot as plt
from disjointset import DisjointSet


def main():
    """Test runtime complexity of make_set, find_set, and union operations."""
    
    test_sizes = [1000, 10000, 50000, 100000]
    
    # Storage for plotting
    make_set_times = []
    union_times = []
    find_set_times = []
    
    print("=" * 80)
    print("Disjoint Set Runtime Complexity Test")
    print("=" * 80)
    
    for size in test_sizes:
        print(f"\nTesting with {size} elements:")
        print("-" * 40)
        
        ds = DisjointSet()
        
        # Test make_set runtime
        start = time.perf_counter()
        for i in range(size):
            ds.make_set(i)
        make_set_time = time.perf_counter() - start
        make_set_times.append(make_set_time)
        print(f"make_set({size}): {make_set_time:.6f} seconds")
        
        # Test union runtime
        start = time.perf_counter()
        for i in range(1, size):
            ds.union(i, i - 1)
        union_time = time.perf_counter() - start
        union_times.append(union_time)
        print(f"union({size}): {union_time:.6f} seconds")
        
        # Test find_set runtime
        start = time.perf_counter()
        for i in range(size):
            ds.find_set(i)
        find_set_time = time.perf_counter() - start
        find_set_times.append(find_set_time)
        print(f"find_set({size}): {find_set_time:.6f} seconds")
        
        # Calculate average times
        avg_make_set = make_set_time / size * 1_000_000  # Convert to microseconds
        avg_union = union_time / (size - 1) * 1_000_000
        avg_find_set = find_set_time / size * 1_000_000
        
        print(f"\nAverage times (per operation):")
        print(f"  make_set: {avg_make_set:.3f} μs")
        print(f"  union: {avg_union:.3f} μs")
        print(f"  find_set: {avg_find_set:.3f} μs")
    
    print("\n" + "=" * 80)
    print("Complexity Analysis:")
    print("-" * 40)
    print("make_set:  O(1) - constant time")
    print("find_set:  O(α(n)) - nearly constant with path compression")
    print("union:     O(α(n)) - nearly constant with union by rank")
    print("=" * 80)
    
    # Plot the graph
    plt.figure(figsize=(12, 7))
    plt.plot(test_sizes, make_set_times, marker='o', linewidth=2, label='make_set', markersize=8)
    plt.plot(test_sizes, union_times, marker='s', linewidth=2, label='union', markersize=8)
    plt.plot(test_sizes, find_set_times, marker='^', linewidth=2, label='find_set', markersize=8)
    
    plt.xlabel('Number of Elements', fontsize=12)
    plt.ylabel('Time (seconds)', fontsize=12)
    plt.title('Disjoint Set Operations - Runtime vs Input Size', fontsize=14, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('disjoint_set_graph.png', dpi=300, bbox_inches='tight')
    print("\nGraph saved as 'disjoint_set_graph.png'")
    plt.show()


if __name__ == "__main__":
    main()
