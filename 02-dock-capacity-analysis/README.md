# Dock Capacity Analysis

A Python analysis of daily shipping dock utilization that compares **peak days vs the average** to support a staffing decision.

> Data in this project is made up for learning purposes.

## Business problem

The shipping supervisor says the dock is "fine on average", but trucks keep waiting on some days. Management is considering adding a second shift and wants data first.

This analysis answers:

- How full was the dock each day?
- Which days went over capacity, and by how much?
- Is demand flat or spiky, and what kind of fix does that suggest?

## Supply chain concept

**Capacity** is the most work an operation can handle in a period. Here, the dock can load **50 pallets per day**.

Planning capacity using only the **average** day hides the problem: busy days and slow days cancel out in the average, but unused capacity on a slow day cannot be saved for a busy one. Capacity has to be judged **day by day**, and especially on the **peak** day.

## Formulas

| Metric | Formula |
|---|---|
| Total pallets | Sum of all daily pallets |
| Average per day | Total pallets ÷ Number of days |
| Daily utilization % | Pallets that day ÷ Capacity × 100 |
| Average utilization % | Average per day ÷ Capacity × 100 |
| Over-capacity days | Count of days where Pallets > Capacity |
| Overflow pallets | Sum of (Pallets − Capacity) on over-capacity days |
| Peak-to-average ratio | Peak day ÷ Average per day |

**Daily status**

| Utilization | Status |
|---|---|
| Above 100% | 🔴 Over capacity |
| 90% to 100% | 🟡 Near capacity |
| Below 90% | 🟢 Ok |

## Inputs

| Input | Value |
|---|---|
| Pallets shipped per day (14 days) | 38, 42, 45, 40, 52, 30, 18, 41, 47, 55, 44, 36, 22, 20 |
| Dock capacity | 50 pallets/day |

## Sample output

```
==============================
DOCK CAPACITY - LAST 14 DAYS
==============================
Day 1: 38 pallets · 76.0% 🟢 Ok
Day 2: 42 pallets · 84.0% 🟢 Ok
Day 3: 45 pallets · 90.0% 🟡 Near capacity
Day 4: 40 pallets · 80.0% 🟢 Ok
Day 5: 52 pallets · 104.0% 🔴 Over capacity
Day 6: 30 pallets · 60.0% 🟢 Ok
Day 7: 18 pallets · 36.0% 🟢 Ok
Day 8: 41 pallets · 82.0% 🟢 Ok
Day 9: 47 pallets · 94.0% 🟡 Near capacity
Day 10: 55 pallets · 110.0% 🔴 Over capacity
Day 11: 44 pallets · 88.0% 🟢 Ok
Day 12: 36 pallets · 72.0% 🟢 Ok
Day 13: 22 pallets · 44.0% 🟢 Ok
Day 14: 20 pallets · 40.0% 🟢 Ok
------------------------------
Total pallets: 530
Average per day: 37.9
Peak day: 55
Lowest day: 18
Average utilization: 75.7%
Over-capacity days: 2
Overflow pallets: 7
Peak-to-average ratio: 1.45
==============================
```

## What the numbers say

- **Average utilization is 75.7%**, so "on average" the dock is healthy
- But **2 days went over 100%** and **2 more were at 90%+**: 4 out of 14 days were under stress
- Only **7 pallets** overflowed in total
- A **peak-to-average ratio of 1.45** means demand is spiky on a few days, not high every day

**Recommendation:** a full second shift would sit idle most of the time. Flexible capacity on peak days (temporary crew or overtime), or smoothing orders across the week, fixes the problem at a lower cost.

## What-if scenario: expand the dock to 60 pallets/day

| Result | Capacity 50 | Capacity 60 |
|---|---|---|
| Over-capacity days | 2 | 0 |
| Overflow pallets | 7 | 0 |
| Busiest day (Day 10) | 110.0% 🔴 | 91.7% 🟡 |
| Average utilization | 75.7% | 63.1% |

Expanding capacity removes all overflow, but average utilization drops to 63%, meaning more idle capacity on normal days.

## Python concepts used

- `for` loops with accumulators (total, counters)
- Finding the highest and lowest values with a loop (no `max()` / `min()`)
- `range()` with `len()` to turn list positions into business day numbers
- `if / elif / else` for status rules
- A single capacity variable, so the what-if scenario is a one-number change

## How to run

```bash
python3 dock_capacity_analysis.py
```

Change `dock_capacity` at the top of the file to test other scenarios.