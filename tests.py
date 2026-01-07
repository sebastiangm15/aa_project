# static_tests.py
"""
TOATE testele hardcodate pentru benchmark.
Respectă limitele: noduri ≤ 20, muchii ≤ 380, culori ≤ 20
"""

def get_all_hardcoded_tests():
    """Returnează exact 2087 de teste hardcodate"""
    tests = []
    
    # ==================== 70 DE TESTE DIFICILE PENTRU BF ====================
    # Acestea sunt dense, 8-12 noduri (pentru BF lent dar în limite)
    
    import random
    random.seed(42)
    
    # 1-10: Grafuri complete K6-K10 (dense dar în limite)
    # K10 are 45 muchii (< 380), K12 are 66 muchii (< 380)
    for n in [6, 7, 8, 8, 9, 9, 10, 10, 11, 11]:
        if n <= 20:  # Respectă limită noduri
            edges = [(i, j) for i in range(n) for j in range(i+1, n)]
            if len(edges) <= 380:  # Verifică limita muchii
                tests.append(("small", n, edges))
    
    # 11-20: Grafuri dense dar în limite
    dense_patterns = [
        # 6 noduri, 10 muchii
        [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(2,4),(3,5),(4,5)],
        # 7 noduri, 14 muchii
        [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,6),(2,4),(2,6),(3,5),(4,5),(4,6),(5,6)],
        # 8 noduri, 18 muchii
        [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),(1,7),(2,4),(2,7),(3,5),(4,6),(5,6),(5,7),(6,7)],
        # 9 noduri, 22 muchii
        [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,6),(2,4),(2,7),(3,5),(3,8),(4,6),(4,8),(5,7),(5,8),(6,7),(6,8),(7,8)],
        # 10 noduri, 26 muchii
        [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,2),(1,3),(1,7),(2,4),(2,8),(3,5),(3,9),(4,6),(4,9),(5,7),(5,9),(6,8),(6,9),(7,8),(7,9),(8,9)],
    ]
    
    for edges in dense_patterns:
        n = max(max(u,v) for u,v in edges) + 1
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
    
    # 21-30: Crown graphs (bipartițite dense)
    for base in [4, 5, 6]:  # 8, 10, 12 noduri total
        n = base * 2  # 8, 10, 12 noduri
        edges = []
        # Crown: bipartițit complet minus matching perfect
        for i in range(base):
            for j in range(base, n):
                if i != j - base:  # exclude matching-ul
                    edges.append((i, j))
        # Adaugă câteva muchii în părți
        for i in range(base):
            for j in range(i+1, base):
                if (i + j) % 2 == 0:  # jumătate din muchii
                    edges.append((i, j))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
    
    # 31-40: Circulant graphs (grafuri circulante)
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
    
    # 41-50: Wheel graphs (roată)
    for n in [7, 8, 9, 10, 11]:
        edges = []
        # Cycle (n-1 noduri în cerc)
        for i in range(n-1):
            edges.append((i, (i+1) % (n-1)))
        # Conectează la centru
        for i in range(n-1):
            edges.append((i, n-1))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
    
    # 51-60: Grafuri random dense (în limite)
    for i in range(10):
        n = random.choice([8, 9, 10, 11, 12])
        edges = []
        # Density 50-70%
        density = random.uniform(0.5, 0.7)
        for u in range(n):
            for v in range(u+1, n):
                if random.random() < density:
                    edges.append((u, v))
        if n <= 20 and len(edges) <= 380:
            tests.append(("small", n, edges))
    
    # 61-70: Grafuri speciale din literatură (în limite)
    # Grötzsch graph (11 noduri, 25 muchii)
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
    
    # Chvátal graph (12 noduri, 24 muchii)
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
    
    # Complete the 70 tests
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
    
    # ==================== 1000 DE TESTE MEDII ====================
    # 15-20 noduri, moderate density
    for i in range(1000):
        n = random.randint(15, 20)  # În limite!
        
        if i < 300:
            # First 300: medium density
            p = random.uniform(0.3, 0.5)
            edges = []
            for u in range(n):
                for v in range(u+1, n):
                    if random.random() < p:
                        edges.append((u, v))
            if len(edges) <= 380:
                tests.append(("medium", n, edges))
                
        elif i < 600:
            # Next 300: bipartite-like
            left = n // 2
            edges = []
            # Conectează între părți
            for u in range(left):
                for v in range(left, n):
                    if random.random() < 0.5:
                        edges.append((u, v))
            # Câteva muchii în interior
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
            # Last 400: sparse to medium
            p = random.uniform(0.2, 0.4)
            edges = []
            for u in range(n):
                for v in range(u+1, n):
                    if random.random() < p:
                        edges.append((u, v))
            if len(edges) <= 380:
                tests.append(("medium", n, edges))
    
    # ==================== 1000 DE TESTE MARI ====================
    # Pentru euristici: 21-70 noduri, dar muchii ≤ 380
    
    for i in range(1000):
        if i < 400:
            # First 400: 21-40 noduri, sparse
            n = random.randint(21, 40)
            p = random.uniform(0.05, 0.15)  # Sparse
        elif i < 700:
            # Next 300: 25-50 noduri, very sparse
            n = random.randint(25, 50)
            p = random.uniform(0.03, 0.1)   # Foarte sparse
        elif i < 850:
            # Next 150: 30-60 noduri, extremely sparse
            n = random.randint(30, 60)
            p = random.uniform(0.02, 0.06)  # Extrem de sparse
        else:
            # Last 150: 35-70 noduri, ultra sparse
            n = random.randint(35, 70)
            p = random.uniform(0.01, 0.04)  # Ultra sparse
        
        # Generează muchii, verfică limita 380
        edges = []
        max_possible = n * (n - 1) // 2
        target_edges = min(380, int(p * max_possible))
        
        # Generează muchii aleatorii până la target
        all_pairs = [(u, v) for u in range(n) for v in range(u+1, n)]
        random.shuffle(all_pairs)
        edges = all_pairs[:target_edges]
        
        if len(edges) <= 380:
            if n <= 30:
                tests.append(("medium", n, edges))
            else:
                tests.append(("large", n, edges))
    
    # ==================== ADAUGĂ TESTE SPECIALE ====================
    special_graphs = [
        # Grafuri din specificație
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
        
        # Grafuri goale (easy)
        ("small", 1, []),
        ("small", 2, []),
        ("small", 3, []),
        ("small", 4, []),
        ("small", 5, []),
        
        # Grafuri complet K3-K8
        ("small", 3, [(0,1),(0,2),(1,2)]),
        ("small", 4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
        ("small", 5, [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]),
        ("small", 6, [(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]),
        ("small", 7, [(i,j) for i in range(7) for j in range(i+1, 7)]),
        ("small", 8, [(i,j) for i in range(8) for j in range(i+1, 8)][:100]),  # Primele 100 muchii din K8
    ]
    
    # Adaugă până ajungem la 2087
    current_count = len(tests)
    needed = 2087 - current_count
    
    for i in range(min(needed, len(special_graphs))):
        kind, n, edges = special_graphs[i]
        if len(edges) <= 380:
            tests.append((kind, n, edges))
    
    # Dacă tot nu avem destule, adaugă grafuri random
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
        
        # Verifică limita muchii
        if len(edges) > 380:
            edges = edges[:380]  # Trunchiază la 380
        
        kind = "small" if n <= 12 else ("medium" if n <= 30 else "large")
        tests.append((kind, n, edges))
    
    # Verificări finale
    assert len(tests) == 2087, f"Expected 2087 tests, got {len(tests)}"
    
    small_tests = [t for t in tests if t[0] == "small"]
    assert len(small_tests) >= 70, f"Expected at least 70 small tests, got {len(small_tests)}"
    
    # Verifică limitele pentru toate testele
    for kind, n, edges in tests:
        assert n <= 70, f"Graph has {n} nodes (> 70)"
        assert len(edges) <= 380, f"Graph has {len(edges)} edges (> 380)"
        # Culori vor fi verificate la rulare, dar teoretic ≤ 20 pentru n ≤ 20
    
    print(f"Generated {len(tests)} tests")
    print(f"Small tests (for BF): {len(small_tests)}")
    print(f"Medium tests: {len([t for t in tests if t[0] == 'medium'])}")
    print(f"Large tests: {len([t for t in tests if t[0] == 'large'])}")
    
    return tests


def get_compatible_tests():
    """Wrapper pentru compatibilitate"""
    return get_all_hardcoded_tests()


def generate_tests():
    """Alias pentru compatibilitate"""
    return get_compatible_tests()