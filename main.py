import random as r

class Card:
  def __init__(self,suite,rank):
    self.suite = suite
    self.rank = rank

  def get_rank(self):
    values = {"Ace":14,"King":13,"Queen":12, "Jack":11, "Ten":10, "Nine":9, "Eight":8, "Seven":7, "Six":6, "Five":5, "Four":4, "Three":3, "Two":2}
    return values[self.rank]

  def __str__(self):
    return f"{self.rank} of {self.suite}"

class Deck:
  def __init__(self):
    self.suites = ["Hearts","Spades","Clubs", "Diamonds"]
    self.ranks = ["Ace","King","Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two"]
    self.total_cards = list()
    for suite in self.suites:
      for rank in self.ranks:
        self.total_cards.append(Card(suite,rank))
  def shuffle_cards(self):
    r.shuffle(self.total_cards)
    
class Player:
  def __init__(self,name):
    self.name = name
    self.cards = list()
    #top is 0 and bottom is -1
  def play_card(self):
    temp = self.cards[0]
    self.cards.pop(0)
    return temp
  def recieve_cards(self,cards):
    for card in cards:
      self.cards.insert(-1, card)
  def __str__(self):
    return f"{self.name} has {len(self.cards)} cards left"

class Game:
  def __init__(self, player_1_name, player_2_name):
    self.player_1 = Player(player_1_name)
    self.player_2 = Player(player_2_name)

    self.deck = Deck()
    self.deck.shuffle_cards()
    
    for index, card in enumerate(self.deck.total_cards):
      if index % 2: 
        self.player_2.recieve_cards([card])
      else:
        self.player_1.recieve_cards([card])

  def play_game(self):
    not_finished = True
    turns = 0 
    while not_finished:
      turns += 1
      print(f"---TURN {turns-1}---")
      if len(self.player_1.cards) <= 0 or len(self.player_2.cards) <= 0:
        print("---VICTORY---")
        if len(self.player_1.cards) <= 0:
          print(f"{self.player_2.name} has won!")
          print(f"STATS:\n{str(self.player_1)}\n{str(self.player_2)}")
          print(f"game duration: {turns-1} turns")
          return None
        else:
          print(f"{self.player_2.name} has won!")
          print(f"STATS:\n{str(self.player_1)}\n{str(self.player_2)}")
          print(f"game duration: {turns-1} turns")
          return None
      card_1 = self.player_1.play_card()
      print(f"card played by {self.player_1.name}: {str(card_1)}")
      card_2 = self.player_2.play_card()
      print(f"card played by {self.player_2.name}: {str(card_2)}")
      if card_1.get_rank() > card_2.get_rank():
        self.player_1.recieve_cards([card_1,card_2])
        print(str(self.player_1))
        print(str(self.player_2))
      elif card_1.get_rank() < card_2.get_rank():
        self.player_2.recieve_cards([card_1,card_2])
        print(str(self.player_1))
        print(str(self.player_2))
      else:
        print("\nA war has started!")
        war = True
        stake = list()
        stake.append(card_1)
        stake.append(card_2)
        
        while war:
          if len(self.player_1.cards) <= 3 or len(self.player_2.cards) <= 3:
            print("---VICTORY---")
            if len(self.player_1.cards) <= 3:
              print(f"{self.player_2.name} has won!")
              print(f"STATS:\n{str(self.player_2)}\n{self.player_1.name} has 0 cards left")
              print(f"game duration: {turns-1} turns")

            else:
              print(f"STATS:\n{self.player_1.name} has WON!\n{self.player_2.name} has 52 cards left\n{self.player_1.name} has 0 cards left")
              print(f"game duration: {turns-1} turns")
              print("won at WAR")
              return None
          
          for card in range(3):
            stake.append(self.player_1.play_card())
            stake.append(self.player_2.play_card())
            

          card_1a = self.player_1.play_card()
          card_2a = self.player_2.play_card()
          stake.append(card_1a)
          stake.append(card_2a)
          if card_1a.get_rank() > card_2a.get_rank():
            self.player_1.recieve_cards(stake)
            print("The war has ENDED")
            war = False
          elif card_2a.get_rank() > card_1a.get_rank():
            self.player_2.recieve_cards(stake)
            print("The war has ENDED")

            war = False
          print(str(card_1a),str(card_2a))


war = Game("george","jeff")
print(war.play_game())

