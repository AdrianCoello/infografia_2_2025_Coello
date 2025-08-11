from abilities import Ability  # Importación añadida
import random

class Character:
    def __init__(self, name, class_name, hp, base_damage, parry_prob, crit_prob):
        self.name = name
        self.class_name = class_name
        self.max_hp = hp
        self.hp = hp
        self.base_damage = base_damage
        self.parry_prob = parry_prob
        self.crit_prob = crit_prob
        self.available_abilities = []
        self.chosen_ability = None
        self.active_effects = []
        self.stats = {
            "damage_dealt": 0,
            "healing_done": 0,
            "abilities_used": 0,
            "turns_alive": 0,
            "times_parried": 0
        }

    def attack(self, target):
        is_crit = random.random() <= self.crit_prob
        damage = self.base_damage * (2 if is_crit else 1)

        if random.random() <= target.parry_prob:
            target.stats["times_parried"] += 1
            print(f"{target.name} paró el ataque!")
            return

        target.hp -= damage
        if target.hp < 0:
            target.hp = 0
            
        self.stats["damage_dealt"] += damage
        crit_msg = " (CRÍTICO!)" if is_crit else ""
        print(f"{self.name} atacó a {target.name} por {damage} daño{crit_msg}")
        
        if target.hp == 0:
            print(f"¡{target.name} ha sido derrotado!")

    def heal(self, amount):
        healed = min(amount, self.max_hp - self.hp)
        if healed > 0:
            self.hp += healed
            self.stats["healing_done"] += healed
            print(f"{self.name} se curó {healed} HP")

    def process_effects(self):
        self.stats["turns_alive"] += 1
        
        for eff in list(self.active_effects):
            if self.hp <= 0:
                break
                
            if eff["kind"] == "damage":
                self.hp -= eff["per_turn"]
                eff["source"].stats["damage_dealt"] += eff["per_turn"]
                print(f"{self.name} sufrió {eff['per_turn']} daño por {eff['name']}")
            elif eff["kind"] == "heal":
                self.heal(eff["per_turn"])
                
            eff["remaining"] -= 1
            if eff["remaining"] <= 0:
                self.active_effects.remove(eff)
                
        if self.hp <= 0:
            self.hp = 0
            print(f"¡{self.name} ha muerto!")

    def choose_ability_by_index(self, index):
        if 0 <= index < len(self.available_abilities):
            self.chosen_ability = self.available_abilities[index]
            print(f"{self.name} eligió: {self.chosen_ability.name}")

    def use_chosen_ability(self, target):
        if not self.chosen_ability:
            print("¡No has elegido una habilidad!")
            return False
            
        if not self.chosen_ability.can_use():
            print("¡No quedan usos de esta habilidad!")
            return False
            
        if self.chosen_ability.remaining_uses is not None:
            self.chosen_ability.remaining_uses -= 1
            
        # Efecto inmediato
        if self.chosen_ability.immediate:
            if self.chosen_ability.kind == "damage":
                target.hp -= self.chosen_ability.immediate
                if target.hp < 0:
                    target.hp = 0
                self.stats["damage_dealt"] += self.chosen_ability.immediate
                print(f"{self.name} usó {self.chosen_ability.name} - {target.name} perdió {self.chosen_ability.immediate} HP")
                
                if target.hp == 0:
                    print(f"¡{target.name} ha sido derrotado!")
            else:
                self.heal(self.chosen_ability.immediate)

        # Efecto continuo
        if self.chosen_ability.duration > 0 and self.chosen_ability.per_turn:
            effect = {
                "name": self.chosen_ability.name,
                "remaining": self.chosen_ability.duration,
                "per_turn": self.chosen_ability.per_turn,
                "kind": self.chosen_ability.kind,
                "source": self
            }
            
            if self.chosen_ability.kind == "damage":
                target.active_effects.append(effect)
                print(f"{target.name} sufrirá {self.chosen_ability.per_turn} por {self.chosen_ability.duration} turnos")
            else:
                self.active_effects.append(effect)
                print(f"{self.name} se recuperará {self.chosen_ability.per_turn} por {self.chosen_ability.duration} turnos")
        
        self.stats["abilities_used"] += 1
        return True

    def is_alive(self):
        return self.hp > 0


# Clases específicas de personajes
class Tank(Character):
    def __init__(self, name):
        super().__init__(name, "Tank", 500, 8, 0.3, 0.1)
        self.available_abilities = [
            Ability("Golpe de Escudo", "Daño moderado y reduce daño recibido", "damage", immediate=12),
            Ability("Fortaleza", "Aumenta defensa y recupera HP", "heal", immediate=20, per_turn=5, duration=3, max_uses=2)
        ]

class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, "Rogue", 100, 10, 0.1, 0.4)
        self.available_abilities = [
            Ability("Puñalada", "Alto daño crítico", "damage", immediate=25, max_uses=3),
            Ability("Veneno", "Daño continuo", "damage", per_turn=8, duration=4, max_uses=2)
        ]

class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, "Wizard", 80, 15, 0.05, 0.3)
        self.available_abilities = [
            Ability("Bola de Fuego", "Daño mágico alto", "damage", immediate=30, max_uses=2),
            Ability("Tormenta de Hielo", "Daño moderado continuo", "damage", per_turn=7, duration=3, immediate=10)
        ]

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, "Paladin", 300, 9, 0.2, 0.15)
        self.available_abilities = [
            Ability("Golpe Sagrado", "Daño y curación", "damage", immediate=15),
            Ability("Bendición Divina", "Curación potente", "heal", immediate=25, per_turn=8, duration=2, max_uses=3)
        ]