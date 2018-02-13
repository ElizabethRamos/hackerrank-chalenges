
#Challenge:

#Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
#and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

meal_cost = gets.strip.to_f
tip_percent = gets.strip.to_i
tax_percent = gets.strip.to_i

def total_meal_cost
  tip = meal_cost * tip_percent / 100
  tax = meal_cost * tax_percent / 100
  total_cost = meal_cost + tip + tax
  @total_cost = total_cost.round

  puts "The total meal cost is #{@total_cost} dollars."
end
