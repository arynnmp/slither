#Enter Package Weight Here
weight = 41.5
print("Package weight: " + str(weight))

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight >6 and weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Ground Shipping: $" + str(cost_ground))

#Ground Shipping Premium
premium_ground = 125
print("Ground Shipping Premium: $" + str(premium_ground))

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight >6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25
print("Drone Shipping: $" + str(cost_drone))
