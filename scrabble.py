#Let's play scrabble!
#Doesn't take into account bonus squares - sad face

#here's the letters and their point totals
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]

letters += [letter.lower for letter in letters]
points *= 2

letter_to_points = {letters:points for letters, points in zip(letters, points)}

#update each player name to be whatever you want
player_to_words = {"player1": [], "player2": [], "player3": [], "player4": []}

def play_word(player, word):
  (player_to_words[player]).append(word)

#play your words here
#---------------------------------------------------------
play_word("player1", "QUAY")
#---------------------------------------------------------

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

player_to_points = {}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
update_point_totals()

print("Player point totals:")
print(player_to_points)