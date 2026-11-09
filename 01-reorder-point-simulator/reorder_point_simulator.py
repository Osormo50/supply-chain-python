#Reorder Point Simulator
#FR-02
def border_function():
  print("=" * 30)

def divider_function():
  print("-" * 30)

#FR-01
on_hand = 1020
daily_demand = 60
lead_time = 5
safety_stock = 120
order_quantity = 600

#FR-03
reorder_point = daily_demand * lead_time + safety_stock

#FR-04: Phase 1, count down to the reorder point (while loop)
border_function()
print("REORDER POINT SIMULATOR")
border_function()
print(f"Reorder Point: {reorder_point} boxes")
divider_function()

day = 0
stock = on_hand
while stock > reorder_point:
  day +=1
  stock -= daily_demand
  print(f"Day {day}: {stock} boxes")


divider_function()
print(f"Day {day}: Reorder Point Reached. PO for {order_quantity} boxes placed")
divider_function()

lead_time_new = lead_time

#FR-05: Phase 2
while lead_time_new > 0:
  day += 1
  lead_time_new -= 1
  stock -= daily_demand
  if lead_time_new == 0:
    print(f"Day {day}: {stock} boxes · trucks arrives today")
  else:
    print(f"Day {day}: {stock} boxes · truck arrives in {lead_time_new} days")

divider_function()

stock_when_truck_arrives = stock
print(f"Stock when truck arrived: {stock} boxes")
stock_after_receiving = stock_when_truck_arrives + order_quantity
print(f"Stock after receiving PO: {stock_after_receiving} boxes")
used_ss = ""
if stock_when_truck_arrives < safety_stock:
  used_ss = "Yes"
else:
  used_ss = "No"
print(f"Safety stock used: {used_ss}")
divider_function()


begining_stock = on_hand
day_po_calculation = 0

while begining_stock > 0:
  begining_stock -=daily_demand
  day_po_calculation += 1

print(f"Without the PO, stock runs out on day: {day_po_calculation}")
border_function()


