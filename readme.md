# CATEGORII DE GRAFURI GENERATE

## 1. GRAFURI COMPLETE (Tests 1–10)

K6 (6 noduri, 15 muchii)
K7 (7 noduri, 21 muchii)
K8 (8 noduri, 28 muchii) ×2
K9 (9 noduri, 36 muchii) ×2
K10 (10 noduri, 45 muchii) ×2
K11 (11 noduri, 55 muchii) ×2

markdown
Copiază codul

**Caracteristici:**
- Grafurile cele mai dense posibile.
- Pentru `K11` (55 muchii), numărul cromatic este:
χ(G) = 11

markdown
Copiază codul
- Necesită 11 culori → extrem de dificil pentru backtracking.

---

## 2. GRAFURI DENSE CU STRUCTURĂ (Tests 11–20)

- **Test 11:** 6 noduri, 10 muchii  
Graf dens cu structură specifică

- **Test 12:** 7 noduri, 14 muchii  
Graf asemănător cu K7, dar cu câteva muchii lipsă

- **Test 13:** 8 noduri, 18 muchii  
Graf aproape complet

- **Test 14:** 9 noduri, 22 muchii  
Graf dens cu nod central

- **Test 15:** 10 noduri, 26 muchii  
Graf dens, structură aproape bipartițită

---

## 3. CROWN GRAPHS (Tests 21–30)

**Structură:**  
Grafuri bipartițite complete `K_{n,n}` **minus** un matching perfect.

- **Test 21–22:** Crown(8) – 8 noduri  
- **Test 23–24:** Crown(10) – 10 noduri  
- **Test 25–26:** Crown(12) – 12 noduri  

**Proprietate importantă:**
χ(Crown(n)) = ⌈n / 2⌉

yaml
Copiază codul

→ grafuri cu număr cromatic cunoscut, utile pentru validare.

---

## 4. CIRCULANT GRAPHS (Tests 31–40)

**Definiție:**  
Grafuri circulante cu offset-uri:
[1,2], [1,3], [2,3], [1,2,3]

markdown
Copiază codul

- **Test 31–34:** 8 noduri, offset-uri diferite
- **Test 35–38:** 9 noduri, offset-uri diferite
- Continuă similar pentru 10, 11 și 12 noduri

**Caracteristici:**
- Grafuri regulate
- Structură simetrică
- Teste bune pentru euristici greedy și DSATUR

---

## 5. WHEEL GRAPHS (Tests 41–50)

**Definiție:**  
Un ciclu + un nod central conectat la toate nodurile ciclului.

- **Test 41:** Wheel(7) – 7 noduri, 12 muchii
- **Test 42:** Wheel(8) – 8 noduri, 14 muchii
- etc. pentru 9, 10, 11 noduri

**Proprietate:**
χ(Wheel(n)) = 4 dacă n este impar
χ(Wheel(n)) = 3 dacă n este par

Copiază codul

---

## 6. GRAFURI RANDOM DENSE (Tests 51–60)

- 8–12 noduri
- Densitate: **50–70%** (foarte dense)
- Generare random cu **seed fix** pentru reproducibilitate

---

## 7. GRAFURI SPECIALE DIN LITERATURĂ (Tests 61–70)

### 61–62: Grötzsch Graph
- 11 noduri, 25 muchii
- Cel mai mic graf **fără triunghiuri** care necesită 4 culori
χ(G) = 4

Copiază codul
Link:  
https://en.wikipedia.org/wiki/Gr%C3%B6tzsch_graph

---

### 63–64: Chvátal Graph
- 12 noduri, 24 muchii
- Primul graf 4-cromatic descoperit de Chvátal
χ(G) = 4

Copiază codul
Link:  
https://en.wikipedia.org/wiki/Chv%C3%A1tal_graph

---

### 65–70: Grafuri dense random
- 8–12 noduri
- Densitate: 40–80%
- Completează setul de 70 teste

---

## 🔬 PROPRIETĂȚI IMPORTANTE

### Pentru algoritmi exacți:
- Teste mici dar dificile: 8–12 noduri sunt suficiente pentru algoritmi exponențiali
- Densitate mare → multe restricții → spațiu de căutare complex
- Număr cromatic cunoscut pentru grafurile speciale
- Structuri diverse:
  - complete
  - bipartițite
  - circulante
  - wheel graphs

---

## ⏱️ Complexitate estimată

- **K11:**  
11! = 39.916.800

yaml
Copiază codul
asignări posibile → extrem de dificil pentru backtracking simplu

- **Crown(12):**
- Bipartițit, dar dens
- χ = 6

- **Wheel graphs:**  
Structură specifică ce poate induce în eroare algoritmii greedy

---

## 🚀 CUM SĂ FOLOSEȘTI

### 1. Generare fișiere
```bash
python static_tests.py
