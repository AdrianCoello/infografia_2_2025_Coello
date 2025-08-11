# 🎮 Juego de Combate por Turnos - RPG

## 🌟 Características principales
- ✅ 4 clases únicas con habilidades especiales
- ✅ Sistema de combate por turnos estratégico
- ✅ Habilidades con efectos inmediatos y persistentes
- ✅ Estadísticas detalladas de desempeño
- ✅ Soporte para 2-4 jugadores
- ✅ Personalización completa de personajes

## 🚀 Instalación y ejecución

### Requisitos previos
- Python 3.8 o superior

### Pasos para ejecutar el juego
1. Clona el repositorio o descarga los archivos:
```bash
git clone https://github.com/tu-usuario/turn-based-combat.git
cd turn-based-combat
```

2. Ejecuta el archivo principal:
```bash
python main.py
```

## 🧙‍♂️ Clases disponibles

| Clase     | Vida | Daño | Parry | Crítico | Características                     |
|-----------|------|------|-------|---------|-------------------------------------|
| **Tank**  | 500  | 8    | 30%   | 10%     | Alta resistencia, habilidades defensivas |
| **Rogue** | 100  | 10   | 10%   | 40%     | Alto daño crítico, ataques sigilosos |
| **Wizard**| 80   | 15   | 5%    | 30%     | Daño mágico masivo, efectos poderosos |
| **Paladin**| 300 | 9    | 20%   | 15%     | Balanceado, habilidades de curación |

## 🔮 Habilidades por clase

### 🛡️ Tank
1. **Golpe de Escudo**  
   - Daño inmediato: 12  
   - Descripción: Golpe contundente con el escudo que reduce el daño recibido

2. **Fortaleza**  
   - Curación inmediata: 20 HP  
   - Curación por turno: 5 HP durante 3 turnos  
   - Usos máximos: 2  
   - Descripción: Aumenta la defensa mientras recupera salud

### 🗡️ Rogue
1. **Puñalada**  
   - Daño inmediato: 25  
   - Usos máximos: 3  
   - Descripción: Ataque preciso con alta probabilidad de crítico

2. **Veneno**  
   - Daño por turno: 8 durante 4 turnos  
   - Usos máximos: 2  
   - Descripción: Envenena al objetivo causando daño continuo

### 🔥 Wizard
1. **Bola de Fuego**  
   - Daño inmediato: 30  
   - Usos máximos: 2  
   - Descripción: Explosión de fuego que causa daño masivo

2. **Tormenta de Hielo**  
   - Daño inmediato: 10  
   - Daño por turno: 7 durante 3 turnos  
   - Descripción: Congela al objetivo causando daño inmediato y continuo

### ✨ Paladin
1. **Golpe Sagrado**  
   - Daño inmediato: 15  
   - Descripción: Ataque bendecido que causa daño moderado

2. **Bendición Divina**  
   - Curación inmediata: 25 HP  
   - Curación por turno: 8 HP durante 2 turnos  
   - Usos máximos: 3  
   - Descripción: Curación poderosa con efectos persistentes

## 🎯 Cómo jugar

### 1. Creación de personajes
- Ingresa el número de jugadores (2-4)
- Para cada jugador:
  - Asigna un nombre único
  - Selecciona una clase (Tank, Rogue, Wizard o Paladin)
  - Elige una habilidad inicial

### 2. Fase de combate
- En cada turno:
  - Se procesan automáticamente los efectos persistentes (venenos, curas, etc.)
  - Cada jugador vivo puede:
    - **Atacar**: Realiza un ataque básico a un objetivo
    - **Usar habilidad**: Activa tu habilidad elegida contra un objetivo
- El combate continúa hasta que:
  - Queda un solo jugador en pie
  - Todos los jugadores son derrotados
  - Se completan todos los turnos

### 3. Resultados finales
Al final del combate se muestran:
- Estado de cada jugador (Vivo/Derrotado)
- Estadísticas detalladas:
  - Daño total infligido
  - Curación total recibida
  - Habilidades usadas
  - Turnos sobrevividos
  - Paradas exitosas

## 📊 Ejemplo de juego

```plaintext
--- CREACIÓN DE PERSONAJES ---
¿Cuántos jugadores? (2-4): 3

Jugador 1:
Nombre: Ramón
Clases disponibles:
1: Tank (Alta vida, defensa media, daño bajo)
2: Rogue (Vida baja, alta evasión, daño crítico alto)
3: Wizard (Vida muy baja, daño mágico alto)
4: Paladin (Vida media, balanceado, habilidades de curación)
Elige clase (1-4): 1

Jugador 2:
Nombre: Elena
Elige clase (1-4): 3

Jugador 3:
Nombre: Carlos
Elige clase (1-4): 4

--- SELECCIÓN DE HABILIDADES ---

Ramón (Tank):
0: Golpe de Escudo - Daño moderado y reduce daño recibido
1: Fortaleza - Aumenta defensa y recupera HP
Elige una habilidad: 1
Ramón eligió: Fortaleza

... (selección de habilidades para otros jugadores)

--- COMIENZA EL COMBATE ---
Número de turnos: 5

--- TURNO 1 ---

Ramón (Tank) - HP: 500/500
Objetivos:
0: Elena (Wizard) - HP: 80/80
1: Carlos (Paladin) - HP: 300/300
Ramón: [A]tacar o [H]abilidad? H
Índice del objetivo: 0
Ramón usó Fortaleza - Recuperó 20 HP
Ramón se recuperará 5 por 3 turnos

... (combate continúa)

--- RESULTADOS FINALES ---

Ramón (Tank):
ESTADO: Vivo
Daño total: 120
Curación total: 35
Habilidades usadas: 2
Turnos vivo: 5
Paradas realizadas: 3

¡Ramón es el ganador!
```

## 🛠️ Estructura de archivos
```
turn-based-combat/
├── main.py          # Punto de entrada principal
├── character.py     # Definición de personajes y clases
└── abilities.py     # Sistema de habilidades
```
