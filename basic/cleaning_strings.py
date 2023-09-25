#cleaning strings practice
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#split the commas
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)
print('\n')

#strip the whitespace in each list item
highlighted_poems_stripped = []
for poems in highlighted_poems_list:
  highlighted_poems_stripped.append(poems.strip())
print(highlighted_poems_stripped)
print('\n')

#create sublists for the items in each poem
highlighted_poems_details = []
for poems in highlighted_poems_stripped:
  highlighted_poems_details.append(poems.split(":"))
print(highlighted_poems_details)
print('\n')

#create new lists for each index of the sublists
titles = []
poets = []
dates = []
for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])


#writing loop to print out final statements
for i in range(0, len(highlighted_poems_details)):
   print("The poem {} was published by {} in {}.".format(titles[i],poets[i],dates[i]))
