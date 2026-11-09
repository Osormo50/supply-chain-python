# Reorder Point Simulator

A Python simulation that shows **when to place a purchase order** so the truck arrives before stock runs out, and what happens if demand is higher than planned.

> Data in this project is made up for learning purposes.

## Business problem

Buyers often place purchase orders "when stock looks low". Ordering too early creates excess inventory; ordering too late causes stockouts. This tool calculates the **reorder point** and simulates stock day by day to show:

- On which day the PO should be placed
- How much stock is left when the truck arrives
- Whether the safety stock was used
- When stock would run out if the PO was never placed

## Supply chain concept

The **reorder point (ROP)** is the stock level that triggers a new order:

```
Reorder point = (Daily demand × Lead time) + Safety stock
```

- **Daily demand × Lead time** = boxes sold while waiting for the truck
- **Safety stock** = buffer for higher demand or late deliveries

If demand behaves as planned, the truck arrives when stock is exactly at the safety stock level.

## Inputs

| Variable | Value |
|---|---|
| On hand | 1020 boxes |
| Daily demand | 60 boxes/day |
| Lead time | 5 days |
| Safety stock | 120 boxes |
| Order quantity | 600 boxes |

## How it works

1. **Phase 1:** a `while` loop consumes daily demand until stock reaches the reorder point, then places the PO
2. **Phase 2:** a `while` loop counts down the lead time until the truck arrives
3. **Receipt:** adds the order quantity and checks if safety stock was used
4. **What-if:** a separate `while` loop calculates the run-out day if no PO had been placed

## Sample output

```
==============================
REORDER POINT SIMULATION
==============================
Reorder point: 420 boxes
------------------------------
Day 1: 960 boxes
...
Day 10: 420 boxes
------------------------------
Day 10: Reorder point reached. PO for 600 boxes placed
------------------------------
Day 11: 360 boxes · truck arrives in 4 days
...
Day 15: 120 boxes · 🚚 truck arrives today
------------------------------
Stock when truck arrived: 120 boxes
Stock after receiving PO: 720 boxes
Safety stock used: No
------------------------------
Without the PO, stock runs out on day: 17
==============================
```

## What-if scenario: demand increases to 80/day

| Result | 60/day | 80/day |
|---|---|---|
| Reorder point | 420 | 520 |
| PO placed on | Day 10 | Day 7 |
| Stock when truck arrives | 120 | 60 |
| Safety stock used | No | **Yes** |
| Run-out day without PO | 17 | 13 |

**Insight:** at 80 boxes/day, stock drops from 540 to 460 in one day, passing the reorder point by 60 boxes before the daily check catches it. The truck arrives with only 60 boxes left, using half of the safety stock. This shows why safety stock is needed even when the reorder point is calculated correctly.

## Python concepts used

- Functions (`def`) for reusable report formatting
- `while` loops with conditions and countdowns
- `if / else` logic
- Variables as single sources of truth (change one input, the whole simulation updates)

## How to run

```bash
python3 reorder_point_simulator.py
```

Change `daily_demand` (or any input) at the top of the file to test other scenarios.
