#FR-01: Load
pallet_shipped_per_day = [38,42,45,40, 52,30, 18,41,47,55,44,36,22,20]
dock_capacity = 50

#FR-02: Total Pallets
total_pallets = 0

for pallet in pallet_shipped_per_day:
  total_pallets += pallet

print(total_pallets)

#FR-03: Average per Day
average_per_day = round(total_pallets/len(pallet_shipped_per_day),1)
average_per_day_raw = total_pallets/len(pallet_shipped_per_day)
print(average_per_day)

#FR-04: Peak Day
peak_day = 0
for day in pallet_shipped_per_day:
  if day > peak_day:
    peak_day = day

print(peak_day)

#FR-05: Lowest Day
lowest_day = pallet_shipped_per_day[0]
print(lowest_day)

for day in pallet_shipped_per_day:
  if day < lowest_day:
    lowest_day = day

print(lowest_day)

#FR-06: Daily Utilization and Status

day_number = 0
daily_utilization_cal = 0
status_utilization = ""
over_capacity = 0
overflow_pallets = 0

print("=" * 30 + "\n" + f"DOCK CAPACITY - LAST {len(pallet_shipped_per_day)} DAYS \n" + "=" * 30 )

for day in range(0,len(pallet_shipped_per_day)):
  day_number = day + 1
  daily_utilization_cal = round((pallet_shipped_per_day[day] / dock_capacity) * 100,1)
  status_utilization = ""
  if daily_utilization_cal < 90:
    status_utilization = "🟢 Ok"
  elif daily_utilization_cal >= 90 and daily_utilization_cal <=100:
    status_utilization = "🟡 Near Capacity"
  else:
    status_utilization = "🔴 Over Capacity"

  if pallet_shipped_per_day[day] > dock_capacity:
    over_capacity += 1
    overflow_pallets += pallet_shipped_per_day[day] - dock_capacity

  print(f"Day {day_number}: {pallet_shipped_per_day[day]} pallets · {daily_utilization_cal}% {status_utilization}")

#FR-08: Summary Metrics
average_utilization = round(total_pallets/len(pallet_shipped_per_day) / dock_capacity * 100,1)

peak_to_average = round(peak_day/average_per_day_raw,2)

print("-"*30 + "\n" + f"Total pallets: {total_pallets} \nAverage per day: {average_per_day} \nPeak Day: {peak_day} \nLowest day: {lowest_day} \nAverage Utilization: {average_utilization}% \nOver-capacity days: {over_capacity} \nOverflow pallets: {overflow_pallets} \nPeak-to-average ratio: {peak_to_average}\n" +"="*30 )

