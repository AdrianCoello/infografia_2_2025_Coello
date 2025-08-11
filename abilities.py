class Ability:
    def __init__(self, name, description, kind, immediate=0, per_turn=0, duration=0, max_uses=None):
        self.name = name
        self.description = description
        self.kind = kind
        self.immediate = immediate
        self.per_turn = per_turn
        self.duration = duration
        self.max_uses = max_uses
        self.remaining_uses = max_uses

    def can_use(self):
        return self.remaining_uses is None or self.remaining_uses > 0