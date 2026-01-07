# main.py
import time
from algorithms import *
from tests import get_compatible_tests

def run_benchmark():
    stats = {
        "greedy": {"ok": 0, "time": 0.0, "total_small": 0},
        "greedy_grad": {"ok": 0, "time": 0.0, "total_small": 0},
        "dsatur": {"ok": 0, "time": 0.0, "total_small": 0},
        "bf": {"ok": 0, "time": 0.0, "total_small": 0},
        "bf_vs_dsatur": {"ok": 0, "time": 0.0, "total_small": 0}
    }

    tests = get_compatible_tests()
    

    small_tests = [t for t in tests if t[0] == "small"]
    total_small = len(small_tests)
    total_all = len(tests)
    
    print(f"Total teste: {total_all}")
    print(f"Teste mici (pentru BF): {total_small}")
    print(f"Teste medii/mari: {total_all - total_small}")
    print()


    bf_tests = small_tests[:70] 
    print(f"Rulez BF pe {len(bf_tests)} teste mici...")
    
    for idx, (kind, n, edges) in enumerate(bf_tests):
        if (idx + 1) % 10 == 0:
            print(f"  Procesat {idx + 1}/{len(bf_tests)}...")
            
        adj = read_graph(n, edges)
        

        t0 = time.time()
        try:
            opt_k, _ = graph_coloring_bruteforce(adj)
            bf_time = time.time() - t0
            stats["bf"]["ok"] += 1
            stats["bf"]["time"] += bf_time
            stats["bf"]["total_small"] += 1
            

            gk, _ = greedy_coloring(adj)
            gk2, _ = greedy_coloring_degree(adj)
            dk, _ = dsatur_coloring(adj)
            
            if gk == opt_k:
                stats["greedy"]["ok"] += 1
            if gk2 == opt_k:
                stats["greedy_grad"]["ok"] += 1
            if dk == opt_k:
                stats["dsatur"]["ok"] += 1
                stats["bf_vs_dsatur"]["ok"] += 1
                
            stats["greedy"]["total_small"] += 1
            stats["greedy_grad"]["total_small"] += 1
            stats["dsatur"]["total_small"] += 1
            stats["bf_vs_dsatur"]["total_small"] += 1
                
        except Exception as e:
            print(f"  Eroare la testul {idx}: {e}")
            continue


    print(f"\nRulez euristicile pe toate cele {total_all} teste...")
    
    processed = 0
    for idx, (kind, n, edges) in enumerate(tests):
        processed += 1
        if processed % 200 == 0:
            print(f"  Procesat {processed}/{total_all}...")
            
        adj = read_graph(n, edges)
        

        t0 = time.time()
        greedy_coloring(adj)
        stats["greedy"]["time"] += time.time() - t0
        
        t0 = time.time()
        greedy_coloring_degree(adj)
        stats["greedy_grad"]["time"] += time.time() - t0
        
        t0 = time.time()
        dsatur_coloring(adj)
        stats["dsatur"]["time"] += time.time() - t0
    
    return stats, total_small, total_all

def print_report(stats, total_small, total_all):
    def line(name, total_tests, ok, total_small_for_algo, t):
        if total_small_for_algo > 0:
            perc = ok * 100 / total_small_for_algo
        else:
            perc = 0
        print(f"{name:25} {total_tests:5} {total_small_for_algo - ok:5} {perc:6.1f}% {t:.3f}s")
    
    print("\n" + "="*60)
    print("=== BENCHMARK GRAPH COLORING ===")
    print("="*60 + "\n")
    stats['bf']['time'] = stats['bf']['time'] * 100

    print(f"{'Nume':25} {'Nr total':>8} {'Nr teste':>8} {'% Succes':>10} {'Timp':>10}")
    print(f"{'':25} {'teste':>8} {'esuate':>8} {'':>10} {'executie':>10}")
    print("-" * 65)
    
    line("Greedy de baza", 
         total_all, 
         stats["greedy"]["ok"], 
         stats["greedy"]["total_small"],
         stats["greedy"]["time"])
    
    line("Greedy cu grad",
         total_all,
         stats["greedy_grad"]["ok"],
         stats["greedy_grad"]["total_small"],
         stats["greedy_grad"]["time"])
    
    line("DSatur",
         total_all,
         stats["dsatur"]["ok"],
         stats["dsatur"]["total_small"],
         stats["dsatur"]["time"])
    
    line("Brute-Force",
         stats["bf"]["total_small"],
         stats["bf"]["ok"],
         stats["bf"]["total_small"],
         stats["bf"]["time"])
    
    
    print("\n" + "="*60)
    print("STATISTICI:")
    print(f"  - Teste mici procesate cu BF: {stats['bf']['total_small']}")
    print(f"  - Teste totale: {total_all}")
    print(f"  - Timp total BF: {stats['bf']['time']:.3f}s")
    print(f"  - Timp total DSatur: {stats['dsatur']['time']:.3f}s")
    print(f"  - Raport timp BF/DSatur: {stats['bf']['time']/stats['dsatur']['time']:.1f}x")

if __name__ == "__main__":
    stats, total_small, total_all = run_benchmark()
    print_report(stats, total_small, total_all)