# cro2timetabling — Contexto · NIVEL: proyecto
> ⬆ Padre: ../CONTEXT.md
> ⬇ Hijos: algoritmoCRO/ · timetabling/

## Identidad
- **NAME:** CRO2Timetabling
- **GROUP:** ivanmedina
- **BRAND:** 1.ivanmedina.dev
- **ORIGIN:** https://github.com/ivanmedina/CRO2Timetabling.git
- **UPSTREAM:** —
- **DESCRIPTION:** Investigación académica: optimización de horarios escolares (timetabling) mediante el algoritmo metaheurístico CRO (Chemical Reaction Optimization).

## TL;DR

Investigación académica: optimización de horarios escolares (timetabling) mediante el algoritmo metaheurístico CRO (Chemical Reaction Optimization). Pipeline de 2 etapas: primero se genera un horario válido, luego se optimiza el uso de salones.

## Flujo end-to-end

```
1. timetabling/main.py          → genera horario válido desde input JSON
                                   salida: output/JSON/salida-N.json + HTML
2. algoritmoCRO/CROTimetabling.py → carga salida-N como semilla
                                    aplica CRO para minimizar PE (maximizar Z = uso de salones)
                                    salida: output/JSON/salida-optimizada-N.json + HTML
```

## Componentes

| Componente | Rol |
|---|---|
| [`algoritmoCRO/`](algoritmoCRO/CONTEXT.md) | Algoritmo CRO genérico (Molecula, reacciones, operadores, loop) |
| [`timetabling/`](timetabling/CONTEXT.md) | Generador constructivo de horarios + evaluador de restricciones |

## Estructura de directorios

```
cro2timetabling/
├── algoritmoCRO/
│   ├── CROTimetabling.py      ← entry point de optimización
│   ├── lib/                   ← cro.py, molecula.py, reacciones.py, operadores.py
│   └── tests/
├── timetabling/
│   ├── main.py                ← entry point de generación
│   ├── lib/                   ← timetabling.py, funciones.py, restricciones.py, output.py
│   ├── input/                 ← instancia-1.json … instancia-10.json
│   └── output/JSON/ + HTML/
├── assets/                    ← imágenes del README (diagramas, resultados)
└── README.md                  ← spec completa: restricciones, variables, resultados por instancia
```

## Restricciones modeladas

- **Duras (R1-R8):** horas por semana, sin conflictos profesor/salón/horario, disponibilidad
- **Suaves (R9-R12):** un salón por curso, misma hora entre días, días de descanso, maximizar uso de salones
- Función objetivo: `F(x) = (RD * K) + RS` | fitness: `f = 1/F(x)`

## Comandos

```bash
# Etapa 1 — generar horario válido
cd timetabling && python main.py

# Etapa 2 — optimizar con CRO
cd algoritmoCRO && python CROTimetabling.py
```

## Historial y decisiones

- Proyecto de investigación académica (Ivan Medina). Publicado en GitHub como `CRO2Timetabling`.
- 10 instancias de prueba (de 1 curso/salón hasta 50 cursos/salones). Tiempos de ejecución de 0s a 3.8h.
- CRO demostró mejora respecto a la heurística constructiva en instancias medianas (≤20 cursos).

## Deuda técnica

- `main.py` de timetabling es un archivo de experimentos con todo comentado — no es un CLI usable.
- `instancia` hardcodeada en `CROTimetabling.py` (línea `instancia=10`).
- `output/JSON/` y `output/HTML/` deben crearse manualmente.

## Reglas de oro

- Siempre ejecutar desde el directorio del componente (`algoritmoCRO/` o `timetabling/`) — los paths relativos dependen del `cwd`.
- Etapa 1 antes de Etapa 2: CRO requiere la semilla JSON de timetabling.
