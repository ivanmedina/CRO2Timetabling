# timetabling — Contexto · NIVEL: componente
> ⬆ Padre: ../CONTEXT.md
> ⬇ Hijos: —
> 🔎 codegraph: ./.codegraph

## Propósito

Generador de horarios escolares válidos. Dado un archivo de entrada JSON con días, espacios, salones, cursos, profesores y restricciones, produce un horario que satisface las restricciones duras (R1-R8) e intenta satisfacer las suaves (R9-R12). La salida es usada como semilla por `algoritmoCRO` para optimización posterior.

## Stack

- Python 3 — sin dependencias externas
- Input/output: JSON
- Output visual: HTML (tablas de horario)

## Módulos clave

| Módulo | Rol |
|---|---|
| `lib/timetabling.py` — `timetabling(input)` | Algoritmo constructivo: asigna cursos a (día, espacio, salón, profesor) iterando disponibilidad; retorna dict con matrices X, W, Y, V, Q, U, G, O, Z, gamma, omega |
| `lib/inputT.py` — `leerInput(path)` | Carga y parsea el JSON de entrada |
| `lib/funciones.py` | Helpers: `cursosDisponible`, `salonesDisponibles`, `profesoresDisponibles`, `Z`, `GammaX`, `OmegaX`, `nuevaX`, `MatricesX`, etc. |
| `lib/restricciones.py` — `R1..R11` | Verificadores individuales de restricciones; `RD`, `RS`, `RDCheck` para evaluación conjunta |
| `lib/operaciones.py` | Operaciones sobre la solución: `aplanarX`, `rearmarX`, `timetable`, `fobjetivo`, `fitness` |
| `lib/output.py` — `dibujarHorario` | Genera HTML visual del horario |
| `main.py` | Entry point: carga input, corre `timetabling()`, guarda JSON + HTML |

## Variables de la solución

| Variable | Significado |
|---|---|
| `X[d][e][s][c][p]` | 1 si profesor `p` imparte curso `c` en salón `s`, espacio `e`, día `d` |
| `W[d][c]` | 1 si el curso `c` se imparte el día `d` |
| `Y[c][p]` | 1 si el profesor `p` imparte el curso `c` |
| `V[c][s]` | 1 si el curso `c` se imparte en el salón `s` |
| `Q[s]` | 1 si el salón `s` está asignado |
| `Z` | % de uso de salones (métrica de optimización) |

## Input JSON

```json
{
  "dias": [...],
  "espacios": [...],
  "salones": [...],
  "cursos": [{"horas": N, ...}],
  "profesores": [{"disponible": [[...]], ...}],
  "maxCP": N,
  "maxEC": N
}
```

Instancias de prueba en `input/instancia-1.json` … `instancia-10.json`.

## Dependencias

- Solo stdlib de Python
- Output en `output/JSON/` y `output/HTML/` (dirs deben existir)

## Cómo correr solo

```bash
# Desde cro2timetabling/timetabling/
python main.py
# Editar main.py para descomentar la llamada que se quiere probar
```

## Gotchas

- `main.py` tiene casi todo comentado — es un archivo de pruebas/experimentos, no un CLI limpio. Para generar una solución hay que descomentar el bloque `timetabling(input)` relevante.
- El algoritmo constructivo de `timetabling()` es determinista pero no garantiza solución óptima; es la semilla para CRO.
- `os.getcwd()` como `SOURCE_PATH` → ejecutar siempre desde `timetabling/`.
- `output/JSON/` y `output/HTML/` deben existir antes de correr (no se crean automáticamente).
