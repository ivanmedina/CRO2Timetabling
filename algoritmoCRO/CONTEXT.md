# algoritmoCRO — Contexto · NIVEL: componente
> ⬆ Padre: ../CONTEXT.md
> ⬇ Hijos: —
> 🔎 codegraph: ./.codegraph

## Propósito

Implementación del algoritmo metaheurístico **CRO (Chemical Reaction Optimization)** en Python puro. Opera sobre una población de moléculas que representan soluciones candidatas; minimiza la energía potencial (PE) aplicando 4 tipos de reacciones químicas para explorar el espacio de soluciones combinatorias.

Librería standalone — no tiene acoplamiento con el dominio timetabling; puede reutilizarse para otros problemas de optimización.

## Stack

- Python 3 — sin dependencias externas
- `decimal.Decimal` con precisión 16 dígitos (estabilidad numérica en PE/KE)
- Tests: `unittest` en `tests/`

## Módulos clave

| Módulo | Rol |
|---|---|
| `lib/molecula.py` — `Molecula` | Entidad del algoritmo: `w` (solución), `KE` (energía cinética), `PE` (energía potencial), `hits`, `minimumw/PE`, `Z` (% uso salones), `valid` |
| `lib/cro.py` — `CRO(...)` | Loop principal: itera hasta criterio de parada, selecciona reacción, aplica operador, evalúa fitness |
| `lib/reacciones.py` | 4 reacciones: colisión ineficaz en pared, descomposición, colisión intermolecular, síntesis |
| `lib/operadores.py` | Operadores de vecindad que generan nuevas soluciones `w` |
| `CROTimetabling.py` | Entry point de integración: carga semilla del output de `timetabling`, define `finicio`/`fun_objetivo`, lanza `CRO()` y guarda resultado optimizado |

## Parámetros CRO (en CROTimetabling.py)

| Param | Rol |
|---|---|
| `KELossRate` | Pérdida de energía cinética por iteración |
| `colision` | Probabilidad de colisión intermolecular vs. colisión en pared |
| `alfa` / `beta` | Pesos del fitness |
| `popSize` | Tamaño de población |
| `criterios` | `{'a': maxIter, 'b': minPE, 'c': maxHits}` — cualquiera detiene el loop |

## Dependencias

- `../timetabling/output/JSON/salida-<N>.json` — semilla de entrada (solución válida generada por `timetabling`)
- `../timetabling/lib/*` — funciones de dominio para evaluar la función objetivo

## Cómo correr solo

```bash
# Desde cro2timetabling/algoritmoCRO/
python CROTimetabling.py
# Requiere: ../timetabling/output/JSON/salida-<instancia>.json (generado por timetabling/main.py)
```

```bash
# Tests
python -m unittest discover tests/
```

## Gotchas

- `CROTimetabling.py` usa `os.getcwd()` como `PROJECT_PATH` → debe ejecutarse desde `algoritmoCRO/`, no desde la raíz del repo; de lo contrario los imports relativos fallan.
- La semilla para optimizar viene del output de `timetabling/main.py`; si no existe ese JSON, el script falla al cargar.
- El parámetro `instancia` está hardcodeado al 10 en el script — cambiar manualmente para otras instancias.
