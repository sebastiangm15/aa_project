# static_tests.py
"""
TOATE testele hardcodate pentru benchmark.
Respectă limitele: noduri ≤ 20, muchii ≤ 380
"""

import os
import random


def write_test_to_file(test_id, n, edges, base_dir="static_test_files"):
    """Scrie un test într-un fișier"""
    os.makedirs(base_dir, exist_ok=True)
    path = os.path.join(base_dir, f"test_{test_id:03d}.txt")
    with open(path, "w") as f:
        f.write(f"{n} {len(edges)}\n")
        for u, v in edges:
            f.write(f"{u} {v}\n")
    return path


def get_all_hardcoded_tests():
    """Returnează exact 2087 de teste hardcodate și creează fișiere pentru primele 70"""
    tests = []
    
    static_dir = "static_test_files"
    if os.path.exists(static_dir):
        import shutil
        shutil.rmtree(static_dir)
    os.makedirs(static_dir, exist_ok=True)
    
    file_counter = 1
    
    
    random.seed(42)
    
    for n in [6, 7, 8, 8, 9, 9, 10, 10, 11, 11]:
        if n <= 20:
            edges = [(i, j) for i in range(n) for j in range(i+1, n)]
            if len(edges) <= 380:
                tests.append(("small", n, edges))
                write_test_to_file(file_counter, n, edges, static_dir)
                file_counter += 1
    
    dense_patterns = [
        [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(2,4),(3,5),(4,5)],
        [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,6),(2,4),(2,6),(3,5),(4,5),(4,6),(5,6)],
        [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),(1,7),(2,4),(2,7),(3,5),(4,6),(5,6),(5,7),(6,7)],
        [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,6),(2,4),(2,7),(3,5),(3,8),(4,6),(4,8),(5,7),(5,8),(6,7),(6,8),(7,8)],
        [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),(1,7),(2,4),(2,8),(3,5),(3,9),(4,6),(4,9),(5,7),(5,9),(6,8),(6,9),(7,8),(7,9),(8,9)],
    ]
    
    for edges in dense_patterns:
        n = max(max(u,v) for u,v in edges) + 1
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
            if file_counter <= 70:
                write_test_to_file(file_counter, n, edges, static_dir)
                file_counter += 1
    
    for base in [4, 5, 6]:
        n = base * 2 
        edges = []
        for i in range(base):
            for j in range(base, n):
                if i != j - base:
                    edges.append((i, j))
        for i in range(base):
            for j in range(i+1, base):
                if (i + j) % 2 == 0:
                    edges.append((i, j))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
            if file_counter <= 70:
                write_test_to_file(file_counter, n, edges, static_dir)
                file_counter += 1
    
    for n in [8, 9, 10, 11, 12]:
        for offsets in [[1,2], [1,3], [2,3], [1,2,3]]:
            edges = []
            for i in range(n):
                for offset in offsets:
                    j = (i + offset) % n
                    if i < j:
                        edges.append((i, j))
            if n <= 20 and len(edges) <= 380:
                tests.append(("small", n, edges))
                if file_counter <= 70:
                    write_test_to_file(file_counter, n, edges, static_dir)
                    file_counter += 1
    
    for n in [7, 8, 9, 10, 11]:
        edges = []
        for i in range(n-1):
            edges.append((i, (i+1) % (n-1)))
        for i in range(n-1):
            edges.append((i, n-1))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
            if file_counter <= 70:
                write_test_to_file(file_counter, n, edges, static_dir)
                file_counter += 1
    
    for i in range(10):
        n = random.choice([8, 9, 10, 11, 12])
        edges = []
        density = random.uniform(0.5, 0.7)
        for u in range(n):
            for v in range(u+1, n):
                if random.random() < density:
                    edges.append((u, v))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
            if file_counter <= 70:
                write_test_to_file(file_counter, n, edges, static_dir)
                file_counter += 1
    
    grotzsch = [
        (0,1),(0,4),(0,6),(0,7),(0,8),
        (1,2),(1,5),(1,7),(1,9),
        (2,3),(2,6),(2,8),(2,9),
        (3,4),(3,5),(3,7),(3,9),
        (4,5),(4,6),(4,9),
        (5,8),(5,10),
        (6,7),(6,10),
        (7,10),
        (8,10),
        (9,10)
    ]
    if len(grotzsch) <= 380:
        tests.append(("small", 11, grotzsch))
        if file_counter <= 70:
            write_test_to_file(file_counter, 11, grotzsch, static_dir)
            file_counter += 1
    
    chvatal = [
        (0,1),(0,4),(0,6),(0,9),
        (1,2),(1,5),(1,7),
        (2,3),(2,6),(2,8),
        (3,4),(3,5),(3,9),
        (4,7),(4,8),
        (5,10),(5,11),
        (6,10),(6,11),
        (7,10),(7,11),
        (8,10),(8,11),
        (9,10),(9,11)
    ]
    if len(chvatal) <= 380:
        tests.append(("small", 12, chvatal))
        if file_counter <= 70:
            write_test_to_file(file_counter, 12, chvatal, static_dir)
            file_counter += 1
    
    while len([t for t in tests if t[0] == "small"]) < 70:
        n = random.choice([8, 9, 10, 11, 12])
        edges = []
        density = random.uniform(0.4, 0.8)
        for u in range(n):
            for v in range(u+1, n):
                if random.random() < density:
                    edges.append((u, v))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
            if file_counter <= 70:
                write_test_to_file(file_counter, n, edges, static_dir)
                file_counter += 1
    
    for i in range(1000):
        n = random.randint(15, 20) 
        
        if i < 300:
            p = random.uniform(0.3, 0.5)
            edges = []
            for u in range(n):
                for v in range(u+1, n):
                    if random.random() < p:
                        edges.append((u, v))
            if len(edges) <= 380:
                tests.append(("medium", n, edges))
                
        elif i < 600:
            left = n // 2
            edges = []
            for u in range(left):
                for v in range(left, n):
                    if random.random() < 0.5:
                        edges.append((u, v))
            for u in range(left):
                for v in range(u+1, left):
                    if random.random() < 0.2:
                        edges.append((u, v))
            for u in range(left, n):
                for v in range(u+1, n):
                    if random.random() < 0.2:
                        edges.append((u, v))
            if len(edges) <= 380:
                tests.append(("medium", n, edges))
                
        else:
            p = random.uniform(0.2, 0.4)
            edges = []
            for u in range(n):
                for v in range(u+1, n):
                    if random.random() < p:
                        edges.append((u, v))
            if len(edges) <= 380:
                tests.append(("medium", n, edges))
    
    
    for i in range(1000):
        if i < 400:
            n = random.randint(21, 40)
            p = random.uniform(0.05, 0.15)  # Sparse
        elif i < 700:
            n = random.randint(25, 50)
            p = random.uniform(0.03, 0.1)   # Foarte sparse
        elif i < 850:
            n = random.randint(30, 60)
            p = random.uniform(0.02, 0.06)  # Extrem de sparse
        else:
            n = random.randint(35, 70)
            p = random.uniform(0.01, 0.04)  # Ultra sparse
        
        edges = []
        max_possible = n * (n - 1) // 2
        target_edges = min(380, int(p * max_possible))
        
        all_pairs = [(u, v) for u in range(n) for v in range(u+1, n)]
        random.shuffle(all_pairs)
        edges = all_pairs[:target_edges]
        
        if len(edges) <= 380:
            if n <= 30:
                tests.append(("medium", n, edges))
            else:
                tests.append(("large", n, edges))
    
    
    special_graphs = [
        ("small", 6, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]),  # n6-m3-regular
        ("small", 6, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(2,3),(2,4),(5,3)]),  # n6-highly-irregular
        ("small", 5, [(0,1),(0,2),(1,2),(2,3),(3,4)]),  # n5-interference-C-sample1
        ("small", 5, [(0,1),(0,3),(1,2),(2,3),(3,4)]),  # n5-interference-C-sample2
        ("small", 6, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,5),(2,4),(2,5),(3,4),(3,5),(4,5)]),  # n6-line-graph
        ("small", 6, [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(0,2),(1,3),(2,4),(3,5),(4,0),(5,1)]),  # n6-m3-antiprism
        ("small", 6, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(2,3),(2,5),(3,4),(4,5)]),  # n6-slf-SHC1
        ("small", 6, [(0,1),(0,2),(0,3),(1,2),(1,4),(2,3),(2,5),(3,4),(4,5)]),  # n6-slf-SHC2
        ("small", 6, [(0,1),(0,2),(0,4),(1,2),(1,3),(2,3),(2,5),(3,4),(4,5)]),  # n6-slf-SHC3
        ("small", 7, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(2,3),(2,6),(3,4),(3,6),(4,5),(5,6)]),  # n7-dsatur-SHC-smallest
        ("small", 8, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,6),(2,3),(2,7),(3,4),(3,7),(4,5),(4,6),(5,6),(5,7),(6,7)]),  # n8-dsatur-HC-smallest
        ("small", 7, [(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,5),(4,6),(5,6)]),  # n7-laman
        
        ("small", 1, []),
        ("small", 2, []),
        ("small", 3, []),
        ("small", 4, []),
        ("small", 5, []),
        
        ("small", 3, [(0,1),(0,2),(1,2)]),
        ("small", 4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
        ("small", 5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]),
        ("small", 6, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]),
        ("small", 7, [(i,j) for i in range(7) for j in range(i+1, 7)]),
        ("small", 8, [(i,j) for i in range(8) for j in range(i+1, 8)][:100]),
    ]
    
    current_count = len(tests)
    needed = 2087 - current_count
    
    for i in range(min(needed, len(special_graphs))):
        kind, n, edges = special_graphs[i]
        if len(edges) <= 380:
            tests.append((kind, n, edges))
    
    
    while len(tests) < 2087:
        if len(tests) < 1500:
            n = random.randint(15, 20)
            p = random.uniform(0.2, 0.4)
        else:
            n = random.randint(25, 40)
            p = random.uniform(0.05, 0.15)
        
        edges = []
        for u in range(n):
            for v in range(u+1, n):
                if random.random() < p:
                    edges.append((u, v))
        
        if len(edges) > 380:
            edges = edges[:380]
        
        kind = "small" if n <= 12 else ("medium" if n <= 30 else "large")
        tests.append((kind, n, edges))
    
    
    assert len(tests) == 2087, f"Expected 2087 tests, got {len(tests)}"
    
    small_tests = [t for t in tests if t[0] == "small"]
    assert len(small_tests) >= 70, f"Expected at least 70 small tests, got {len(small_tests)}"
    
    for kind, n, edges in tests:
        assert n <= 70, f"Graph has {n} nodes (> 70)"
        assert len(edges) <= 380, f"Graph has {len(edges)} edges (> 380)"
    
    print(f"Generated {len(tests)} tests")
    print(f"Small tests (for BF): {len(small_tests)}")
    print(f"Medium tests: {len([t for t in tests if t[0] == 'medium'])}")
    print(f"Large tests: {len([t for t in tests if t[0] == 'large'])}")
    print(f"Static files created: {file_counter - 1} in directory '{static_dir}/'")
    
    return tests


def get_compatible_tests():
    """Wrapper pentru compatibilitate - returnează toate testele"""
    return get_all_hardcoded_tests()


def generate_tests():
    """Alias pentru compatibilitate"""
    return get_compatible_tests()


def load_static_test_files():
    """Încarcă toate testele din fișierele statice"""
    static_dir = "static_test_files"
    tests = []
    
    if not os.path.exists(static_dir):
        print(f"Directory {static_dir} does not exist. Generating tests first...")
        get_all_hardcoded_tests()
    
    file_list = sorted([f for f in os.listdir(static_dir) if f.startswith("test_") and f.endswith(".txt")])
    
    for filename in file_list:
        path = os.path.join(static_dir, filename)
        with open(path, 'r') as f:
            lines = f.readlines()
            n, m = map(int, lines[0].strip().split())
            edges = []
            for line in lines[1:]:
                if line.strip():
                    u, v = map(int, line.strip().split())
                    edges.append((u, v))
            kind = "small" if n <= 12 else ("medium" if n <= 30 else "large")
            tests.append((kind, n, edges))
    
    print(f"Loaded {len(tests)} static tests from files")
    return tests


if __name__ == "__main__":
    tests = get_all_hardcoded_tests()
    print(f"\nFirst 5 tests as example:")
    for i, (kind, n, edges) in enumerate(tests[:5]):
        print(f"Test {i+1}: {kind}, n={n}, edges={len(edges)}")
    
    static_dir = "static_test_files"
    if os.path.exists(static_dir):
        files = os.listdir(static_dir)
        print(f"\nGenerated {len(files)} static test files in '{static_dir}/'")
        if files:
            print(f"Sample file: {files[0]}")
            with open(os.path.join(static_dir, files[0]), 'r') as f:
                print(f"Content preview:\n{f.read()[:100]}...")