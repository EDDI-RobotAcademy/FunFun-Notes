
class Skill:
    def __init__(self, name, description, effect_type):
        self.name = name
        self.description = description
        self.effect_type = effect_type

    def apply(self, player, target=None):
        if self.effect_type == "eliminate":
            self.eliminate_target(target)
        elif self.effect_type == "steal_points":
            self.steal_points(player)
        # Add more skill effect types if necessary

    def eliminate_target(self, target):
        # Logic to eliminate the target
        print(f"Eliminating {target}")

    def steal_points(self, player):
        # Logic to steal points
        print(f"Stealing points for {player}")
