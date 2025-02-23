class Card:
    
    def __init__(self, suit, value, image):
        self.image = image
        self.suit = suit
        self.value = value
        
    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
            
    def __str__(self):
        return f"{self.value} of {self.suit}"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value
    

