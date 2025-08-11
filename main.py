from character import Tank, Rogue, Wizard, Paladin

# Crear personajes
players = []
class_types = {"1": Tank, "2": Rogue, "3": Wizard, "4": Paladin}

print("--- CREACIÓN DE PERSONAJES ---")
num_players = int(input("¿Cuántos jugadores? (2-4): "))

for i in range(num_players):
    print(f"\nJugador {i+1}:")
    name = input("Nombre: ")
    
    print("Clases disponibles:")
    print("1: Tank (Alta vida, defensa media, daño bajo)")
    print("2: Rogue (Vida baja, alta evasión, daño crítico alto)")
    print("3: Wizard (Vida muy baja, daño mágico alto)")
    print("4: Paladin (Vida media, balanceado, habilidades de curación)")
    
    class_choice = input("Elige clase (1-4): ")
    player_class = class_types.get(class_choice, Tank)
    players.append(player_class(name))

# Selección de habilidades
print("\n--- SELECCIÓN DE HABILIDADES ---")
for player in players:
    print(f"\n{player.name} ({player.class_name}):")
    for j, ability in enumerate(player.available_abilities):
        print(f"{j}: {ability.name} - {ability.description}")
    
    choice = int(input("Elige una habilidad: "))
    player.choose_ability_by_index(choice)

# Combate
print("\n--- COMIENZA EL COMBATE ---")
n_turns = int(input("Número de turnos: "))

for turn in range(1, n_turns + 1):
    print(f"\n--- TURNO {turn} ---")
    
    for player in players:
        if not player.is_alive():
            continue
            
        player.process_effects()
        print(f"\n{player.name} ({player.class_name}) - HP: {player.hp}/{player.max_hp}")
        
        # Mostrar objetivos vivos
        targets = [p for p in players if p != player and p.is_alive()]
        if not targets:
            continue
            
        print("Objetivos:")
        for idx, target in enumerate(targets):
            print(f"{idx}: {target.name} ({target.class_name}) - HP: {target.hp}/{target.max_hp}")
        
        action = input(f"{player.name}: [A]tacar o [H]abilidad? ").upper()
        
        if action == "A":
            target_idx = int(input("Índice del objetivo: "))
            player.attack(targets[target_idx])
        elif action == "H":
            target_idx = int(input("Índice del objetivo: "))
            player.use_chosen_ability(targets[target_idx])
    
    # Verificar si queda un solo jugador vivo
    alive_players = [p for p in players if p.is_alive()]
    if len(alive_players) <= 1:
        break

# Resultados finales
print("\n--- RESULTADOS FINALES ---")
for player in players:
    print(f"\n{player.name} ({player.class_name}):")
    if player.is_alive():
        print("ESTADO: Vivo")
    else:
        print("ESTADO: Derrotado")
    
    print(f"Daño total: {player.stats['damage_dealt']}")
    print(f"Curación total: {player.stats['healing_done']}")
    print(f"Habilidades usadas: {player.stats['abilities_used']}")
    print(f"Turnos vivo: {player.stats['turns_alive']}")
    print(f"Paradas realizadas: {player.stats['times_parried']}")

# Anunciar ganador
alive_players = [p for p in players if p.is_alive()]
if alive_players:
    if len(alive_players) == 1:
        print(f"\n¡{alive_players[0].name} es el ganador!")
    else:
        print("\n¡Empate!")
else:
    print("\n¡Todos los jugadores han sido derrotados!")