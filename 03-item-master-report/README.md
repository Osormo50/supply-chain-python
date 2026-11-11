# Item Master Report

A Python report built on **item master data** that shows inventory value, stock risk and supplier risk for every SKU, plus a **where-used** check for a supplier disruption.

> Data in this project is made up for learning purposes.

## Business problem

Planning needs a quick view of every SKU in the item master to answer:

- How much money is sitting in inventory?
- Which SKUs will run out before a new order can arrive?
- Which SKUs depend on a single supplier?
- If one supplier stops shipping, which SKUs are affected?

## Supply chain concepts

**Item master:** the record an ERP keeps for every SKU (description, cost, stock, demand, lead time, suppliers). Here it's stored as a Python dictionary, with the SKU as the key.

**Single-source risk:** a SKU with only one supplier has no backup if that supplier has a problem.

**Where-used:** for one supplier, the list of SKUs that depend on it. It's the first report planning runs when a supplier has a disruption.

## Formulas

| Value | Formula |
|---|---|
| Inventory value | On hand × Unit cost |
| Days of supply | On hand ÷ Daily demand |
| Number of suppliers | Count of suppliers in the SKU's list |
| Total inventory value | Sum of inventory value for all SKUs |

**Rules**

| Check | Condition | Result |
|---|---|---|
| Stock status | Days of supply < SKU's lead time | 🔴 At risk |
| | otherwise | 🟢 Ok |
| Supplier risk | Exactly 1 supplier | ⚠️ Single source |

## Inputs

| SKU | Description | Unit cost | On hand | Daily demand | Lead time (days) | Suppliers |
|---|---|---|---|---|---|---|
| LBL-5160 | Address labels | 8.50 | 1150 | 100 | 5 | Domtar, 3M Paper |
| LBL-8160 | Mailing labels | 12.00 | 150 | 50 | 7 | Domtar |
| TAB-1100 | Index tabs | 4.25 | 900 | 30 | 10 | Sappi, 3M Paper, Domtar |
| LBL-5163 | Shipping labels | 10.00 | 400 | 40 | 6 | 3M Paper |

## Sample output

```
==============================
ITEM MASTER REPORT
==============================
LBL-5160 · Address Labels
Value: $9775.0 · Days of supply: 11.5 (lead time 5) 🟢 Ok
Suppliers: 2
------------------------------
LBL-8160 · Mailing Labels
Value: $1800.0 · Days of supply: 3.0 (lead time 7) 🔴 At risk
Suppliers: 1 ⚠️ Single source
------------------------------
TAB-1100 · Index tabs
Value: $3825.0 · Days of supply: 30.0 (lead time 10) 🟢 Ok
Suppliers: 3
------------------------------
LBL-5163 · Shipping Labels
Value: $4000.0 · Days of supply: 10.0 (lead time 6) 🟢 Ok
Suppliers: 1 ⚠️ Single source
------------------------------
Total inventory value: $19400.0
SKUs in item master: 4
==============================
Domtar supplies:
LBL-5160
LBL-8160
TAB-1100
==============================
```

## What the numbers say

Scenario: Domtar announces it can't ship for 3 weeks.

| SKU | Uses Domtar? | Other suppliers? | Days of supply | Priority |
|---|---|---|---|---|
| LBL-8160 | Yes | **No** | **3.0** | 🚨 Act today |
| LBL-5160 | Yes | Yes (3M Paper) | 11.5 | Shift orders to 3M Paper |
| TAB-1100 | Yes | Yes (Sappi, 3M Paper) | 30.0 | Low risk |
| LBL-5163 | No | — | 10.0 | Not affected |

**LBL-8160** is the critical item: it depends only on Domtar and has 3 days of stock. Combining the where-used list with the single-source flag tells planning exactly which SKU to rescue first.

## Python concepts used

- Nested dictionaries (SKU → item record → supplier list)
- Looking up, editing and adding records by key
- Looping through a dictionary
- `len()` on lists and dictionaries
- `in` to check whether a supplier is in a SKU's list
- Functions for report formatting

## How to run

```bash
python3 item_master_report.py
```

Change values in `item_master`, or add a new SKU, and run it again to see the report update.
