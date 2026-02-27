# 42_Python_Module_10
42_Python_Module_10

## FuncMage Chronicles: El Camino de la Programación Funcional

Bienvenido a **FuncMage**. 

En el año 2142, el reino digital está en caos y solo los magos de las funciones pueden restaurar el equilibrio mediante el dominio de las artes antiguas de Python.

---

### Reglas de la Alianza (Normas y Estilo)

Para que tus hechizos sean aceptados por el gremio, debes seguir estas estrictas directrices:

* **Entorno:** Python 3.10 o superior.
* **Estándar:** Código adherido a la norma `flakes`.
* **Robustez:** Manejo de excepciones obligatorio para evitar caídas del sistema.
* **Claridad:** Uso de **Type Hints** en todas las firmas y retornos de funciones.
* **Estructura:** Un archivo por ejercicio en su carpeta correspondiente.
* **Enfoque:** Priorizar patrones funcionales claros sobre algoritmos complejos.

---

### Kit de Herramientas (Permitido vs. Prohibido)

#### Objetos Sagrados (Permitidos)
* `functools`: El artefacto principal para decoradores y reducción.
* `typing`: Para definir la naturaleza de tus datos.
* `operator` e `itertools`: Para operaciones y patrones de iteración avanzados.
* Funciones built-in: `lambda`, `map`, `filter`, `sorted`, `callable`.

#### Magia Oscura (Prohibida)
* **Librerías externas:** Nada de `pip install`.
* **I/O de Archivos:** Todo debe ser procesamiento en memoria.
* **Variables Globales:** Prohibidas; se busca la pureza funcional.
* **Funciones Prohibidas:** No uses `eval()` ni `exec()`.

---

### Los 5 Reinos del Conocimiento

| Desafío | Archivo | Concepto Maestro | Dificultad |
| :--- | :--- | :--- | :---: |
| **Ex 0** | `lambda_spells.py` | Funciones anónimas y ordenamiento de datos. | 🟢 3/10 |
| **Ex 1** | `higher_magic.py` | Funciones de orden superior (recibir/retornar funciones). | 🟡 5/10 |
| **Ex 2** | `scope_mysteries.py` | Ámbito léxico, clausuras y persistencia (`nonlocal`). | 🟠 6/10 |
| **Ex 3** | `functools_artifacts.py` | `reduce`, `partial`, `lru_cache` y `singledispatch`. | 🔴 8/10 |
| **Ex 4** | `decorator_mastery.py` | Decoradores complejos, `@wraps` y métodos estáticos. | 🟣 9/10 |

---

### Resumen de los Ejercicios

#### 0. Lambda Sanctum
Domina las funciones de una sola línea. Aprenderás a ordenar artefactos por poder, filtrar magos por nivel y transformar listas de hechizos usando `map` y `filter`.

#### 1. Higher Realm
Aquí las funciones son "ciudadanos de primera clase". Crearás combinadores de hechizos que unen dos efectos en uno y amplificadores que multiplican los resultados de otros hechizos.

#### 2. Memory Depths
Explora las clausuras. Crearás funciones que "recuerdan" variables incluso después de que su entorno original haya desaparecido, permitiendo llevar contadores y memorias privadas sin usar globales.

#### 3. Ancient Library
Usa el módulo `functools` para reducir listas de poder a un solo valor (`reduce`), pre-configurar hechizos con argumentos fijos (`partial`) y optimizar el rendimiento con caché.

#### 4. Master's Tower
El reto final. Crearás decoradores que miden el tiempo de ejecución, validan niveles de poder automáticamente y reintentan hechizos que fallan debido a errores mágicos.

---

### Guía de Supervivencia en el Peer-Review

Durante la evaluación, no basta con que el código funcione. Debes ser capaz de explicar:
1.  **¿Por qué usar `lambda`?** Para operaciones rápidas donde definir una función con `def` sería excesivo.
2.  **¿Qué es una clausura?** Una función que mantiene acceso al entorno donde fue creada.
3.  **¿Para qué sirve `@wraps`?** Para que tus decoradores no "borren" el nombre y la documentación de la función original.

---

### Pruebas
Puedes usar el `tools/data_generator.py` incluido para generar datos de prueba temáticos (artefactos, magos y hechizos) y verificar tus implementaciones.