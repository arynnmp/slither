from datetime import time

class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self,address,menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  
  def available_menus(self,time):
    available_items = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_items.append(menu)
    return available_items

class Menu:
  def __init__(self,name,items,start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{n} menu is available from {s} to {e}".format(n=self.name,s=self.start_time,e=self.end_time)
  
  def calculate_bill(self,purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill


brunch = Menu(
  "brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, time(11,00), time(16,00)
)

early_bird = Menu(
  "early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, time(15,00), time (18,00)
)

dinner = Menu(
  "dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, time(17,00), time(23,00)
)

kids = Menu(
  "kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, time(11,00), time(21,00) 
)

#print(kids)

#bill1 = brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])
#print(bill)

#bill2 = early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)'])
#print(bill2)

flagship_store = Franchise(
  "1232 West End Road", [brunch,early_bird,dinner,kids]
)

new_installment = Franchise(
  "12 East Mulberry Street", [brunch,early_bird,dinner,kids]
)

#print(flagship_store.available_menus(time(12,00)))

#print(new_installment.available_menus(time(17,00)))

basta_fazoolin = Business(
  "Basta Fazoolin' with my Heart", [flagship_store, new_installment]
)

#arepa

arepas = Menu(
  "arepas", {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}, time(10,00), time(20,00)
)

arepas_place = Franchise(
  "189 Fitzgerald Avenue", [arepas]
)

take_arepa = Business(
  "Take a' Arepa", [arepas_place]
)

#print(take_arepa.franchises[0].menus[0])

  


