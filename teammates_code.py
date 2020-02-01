#Volume
user_input = input("What would you like to convert?: ")
#tsp to tbsp
if user_input == "Teaspoon":
  tsp = int(input("Enter teaspoon amount: "))
  tbsp_convertFrom_tsp = (tsp / 2)
  print (str(tbsp_convertFrom_tsp )+ " Tablespoons")

#tbsp to cups
if user_input == "Tablespoon":
  tbsp = int(input("Enter tablespoon amount: "))
  cup_convertFrom_tbsp = (tbsp / 8)
  print (str(cup_convertFrom_tbsp)+ " Cups")

#cups to pints
if user_input == "Cups":
  cups = int(input("Enter cup amount: "))
  pint_convertFrom_cups = (cups / 2)
  print (str(pint_convertFrom_cups)+ " Pints")

#pints to quarts
if user_input == "Pint":
  pint = int(input("Enter pint amount: "))
  quart_convertFrom_pint =(pint / 2)
  print (str(quart_convertFrom_pint)+ " Quarts")

#quarts to gallons
if user_input == "Quart":
  quart = int(input("Enter quart amount: "))
  gallon_convertFrom_quart = (quart / 4)
  print (str(input(gallon_convertFrom_quart)+ " Gallons"))

if user_input == "Milligram":
  milligram = int(input("Enter milligram amount: ")) #user input for var memory as int
  kilogram_convert_from_milligram = (milligram / 1000000) #straight division for float value in var
  kilogram = kilogram_convert_from_milligram #var that contains the answer from the division formula
  print ("You should buy " + str(kilogram) + " kilograms") # prints the variable with some added comments

if user_input == "Grams":
  gram = int(input("Enter gram amount: ")) #user input for var memory as int
  pound_convertFrom_gram = (gram / 454) #straight division for float value
  pounds = pound_convertFrom_gram #var that contains answer from previous line
  rounded_pounds= round(pounds,2)  #rnds the answer
  print ("You should buy " + str(rounded_pounds) + " pounds") #prints the var with some added comments



