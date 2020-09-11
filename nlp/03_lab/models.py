class Game():
    def __init__(self, max_health, has_gun, enemies_amount):
        self.max_health = max_health
        self.has_gun = has_gun
        self.enemies_amount = enemies_amount
        self.actions = ["Attack", "Run", "Hide and Attack", "Do Nothing"]
