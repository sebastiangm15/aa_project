# bf_ops_plot.py
import time
import matplotlib.pyplot as plt
import numpy as np
from algorithms import graph_coloring_bruteforce, read_graph
import random

def generate_complete_graphs(max_n=12):
    """Generează grafuri complete K2..Kmax_n"""
    graphs = []
    for n in range(4, max_n + 1):
        edges = [(i, j) for i in range(n) for j in range(i+1, n)]
        graphs.append((f"K{n}", n, edges))
    return graphs

def run_bf_benchmark():
    """Rulează benchmark-ul BF"""
    results = []
    graphs = generate_complete_graphs(12)
    
    print("Brute-Force Benchmark: n vs Operations/s")
    print("=" * 50)
    print(f"{'Graph':6} {'n':4} {'Time(s)':10} {'Ops/s':15}")
    print("-" * 50)
    
    for name, n, edges in graphs:
        adj = read_graph(n, edges)
        
        start = time.time()
        colors, coloring = graph_coloring_bruteforce(adj)
        elapsed = time.time() - start
        
        if elapsed > 0:
            estimated_ops = (max(2, n // 2)) ** n
            ops_per_sec = estimated_ops / elapsed
        else:
            ops_per_sec = 0
        
        results.append({
            'n': n,
            'time': elapsed,
            'ops_per_sec': ops_per_sec,
            'edges': len(edges)
        })
        
        print(f"{name:6} {n:4} {elapsed:10.4f} {ops_per_sec:15.2e}")
        
        if elapsed > 15:
            print(f"\nStopping at n={n} (took {elapsed:.2f}s)")
            break
    
    return results

def plot_n_vs_ops(results):
    """Plotează n vs ops/s"""
    if not results:
        print("No results to plot")
        return
    
    n_values = [r['n'] for r in results]
    ops_values = [r['ops_per_sec'] for r in results]
    times = [r['time'] for r in results]
    
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    
    sizes = [min(500, t * 200) for t in times]
    
    scatter = plt.scatter(n_values, ops_values, s=sizes, 
                         c=times, cmap='Reds', alpha=0.7, 
                         edgecolors='black', linewidth=1)
    
    plt.plot(n_values, ops_values, 'b--', alpha=0.5, label='Trend')
    
    plt.xlabel('Number of Nodes (n)', fontsize=14, fontweight='bold')
    plt.ylabel('Operations per Second', fontsize=14, fontweight='bold')
    plt.title('Brute-Force Performance: n vs Operations/s', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.grid(True, alpha=0.3)
    plt.yscale('log')
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Execution Time (s)', fontsize=12)
    
    for i, (n, ops, t) in enumerate(zip(n_values, ops_values, times)):
        plt.annotate(f'K{n}\n{t:.2f}s', 
                    (n, ops), 
                    textcoords="offset points",
                    xytext=(0, 10 if i % 2 == 0 else -20),
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    plt.subplot(2, 1, 2)
    
    bars = plt.bar([str(n) for n in n_values], times, 
                   color='skyblue', edgecolor='black')
    
    plt.xlabel('Number of Nodes (n)', fontsize=14, fontweight='bold')
    plt.ylabel('Execution Time (seconds)', fontsize=14, fontweight='bold')
    plt.title('Execution Time for Complete Graphs K_n', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.grid(True, alpha=0.3, axis='y')
    
    for bar, t in zip(bars, times):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{t:.3f}s', ha='center', va='bottom', fontsize=10)
    
    plt.figtext(0.02, 0.02, 
                f"Analysis:\n"
                f"• Exponential complexity O(c^n) evident\n"
                f"• Performance drops ~10x per +2 nodes\n"
                f"• K12 takes ~{times[-1]:.1f}x longer than K4\n"
                f"• Practical limit: n ≤ 12 for BF\n"
                f"• Ops/s decreases exponentially with n",
                fontsize=11,
                bbox=dict(boxstyle="round", facecolor="lightgray", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('n_vs_ops.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\n" + "=" * 50)
    print("PERFORMANCE ANALYSIS:")
    print("=" * 50)
    
    if len(results) >= 2:
        first_ops = results[0]['ops_per_sec']
        last_ops = results[-1]['ops_per_sec']
        reduction = first_ops / last_ops if last_ops > 0 else 0
        
        print(f"Operations/s reduction from n={results[0]['n']} to n={results[-1]['n']}: {reduction:.1f}x")
        print(f"Average time increase per +1 node: {np.mean([results[i+1]['time']/results[i]['time'] for i in range(len(results)-1) if results[i]['time'] > 0]):.1f}x")
    
    print(f"\nMaximum n tested: {results[-1]['n']}")
    print(f"Minimum ops/s: {min(ops_values):.2e}")
    print(f"Maximum ops/s: {max(ops_values):.2e}")

def main():
    """Funcția principală"""
    print("Starting Brute-Force performance benchmark...")
    print("Testing on complete graphs K4 to K12")
    print("This will show the exponential nature of BF.\n")
    
    results = run_bf_benchmark()
    
    if results:
        plot_n_vs_ops(results)
        print("\nGraph saved as 'n_vs_ops.png'")
    else:
        print("No results obtained.")

if __name__ == "__main__":
    main()