# 📚 Taller: Aplicaciones de Grafos en la Ingeniería de Software

Este repositorio contiene soluciones a tres problemas prácticos de grafos aplicados a la ingeniería de software. Cada ejercicio implementa algoritmos fundamentales de teoría de grafos para resolver problemas reales en sistemas distribuidos.

## 🛠️ Configuración del entorno

### Requisitos
- Python 3.8+
- No se requieren dependencias externas

### Clonar el repositorio
```bash
git https://github.com/JHONCE79/Taller-3-estructuras.git
cd Taller-3-estructuras
```

## 📋 Ejercicios

### 1. Camino más corto entre servicios
**Archivo:** `ejercicio1_camino_mas_corto.py`  
**Datos:** `datos/ejercicio1_datos.json`

```bash
python ejercicio1_camino_mas_corto.py
```
Salida esperada:
```
Camino más corto: ['frontend', 'auth', 'db', 'cache', 'storage']
Costo total: 45
```

### 2. Cuellos de botella en navegación
**Archivo:** `ejercicio2_cuellos_de_botella.py`  
**Datos:** `datos/ejercicio2_datos.json`

```bash
python ejercicio2_cuellos_de_botella.py
```
Salida esperada:
```
{
  'login': 1,
  'dashboard': 4,
  'search': 3,
  'product': 2,
  'cart': 2,
  'faq': 1,
  'profile': 1,
  'settings': 1
}
```

### 3. Árbol de expansión mínima
**Archivo:** `ejercicio3_arbol_expansion_minima.py`  
**Datos:** `datos/ejercicio3_datos.py`

```bash
python ejercicio3_arbol_expansion_minima.py
```
Salida esperada:
```
MST: [('Srv2', 'Srv3', 1), ('Srv1', 'Srv2', 3), ('Srv3', 'Srv5', 2), ('Srv4', 'Srv5', 3), ('Srv5', 'Srv6', 4)]
Costo total: 13
```



## 📂 Estructura del proyecto
```
/
├── ejercicio1_camino_mas_corto.py       # Solución Dijkstra
├── ejercicio2_cuellos_de_botella.py     # Solución BFS/DFS
├── ejercicio3_arbol_expansion_minima.py # Solución Kruskal/Prim
├── datos/
│   ├── ejercicio1_datos.json            # Grafo dirigido ponderado
│   ├── ejercicio2_datos.json            # Grafo de navegación
│   └── ejercicio3_datos.py              # Grafo no dirigido

```

## 📝 Personalización
Para modificar los datos de entrada:
1. Edita los archivos JSON correspondientes
2. Para el ejercicio 3, modifica el diccionario en `ejercicio3_datos.py`

