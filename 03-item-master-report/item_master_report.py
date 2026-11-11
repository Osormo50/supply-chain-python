def divisions():
  print("="*30)

def section():
  print("-"*30)

item_master = {
    "LBL-5160": {
        "description":"Address Labels",
        "unit_cost": 8.50,
        "on_hand": 1200,
        "daily_demand": 100,
        "lead_time":5,
        "suppliers":["Domtar", "3M Paper"]
    },
    "LBL-8160": {
        "description":"Mailing Labels",
        "unit_cost": 12.00,
        "on_hand": 150,
        "daily_demand": 50,
        "lead_time": 7,
        "suppliers":['Domtar']
    },
    "TAB-1100": {
        "description":"Index tabs",
        "unit_cost": 4.25,
        "on_hand": 900,
        "daily_demand": 30,
        "lead_time": 10,
        "suppliers":['Sappi','3M Paper','Domtar']
    },
}

#Look up values
print(item_master["LBL-8160"]["on_hand"])
print(item_master["TAB-1100"]["suppliers"][1])

#Edit a Value
item_master["LBL-5160"]["on_hand"] = 1150

#Add a new SKU
item_master["LBL-5163"] = {
    "description":"Shipping Labels",
    "unit_cost" : 10.00,
    "on_hand" : 400,
    "daily_demand" : 40,
    "lead_time" : 6,
    "suppliers": ["3M Paper"]
}

print(item_master["LBL-5163"])

#Loop throught the Dictionary
totals = 0
sku_totals = len(item_master)
domtar_suppliers = []


divisions()
print("ITEM MASTER REPORT")
divisions()


for sku in item_master:
  sku_description = item_master[sku]["description"]
  sku_value = item_master[sku]["unit_cost" ] * item_master[sku]["on_hand"]
  sku_days_of_supply = round(item_master[sku]["on_hand"] / item_master[sku]["daily_demand"],1)
  sku_lead_time = item_master[sku]["lead_time"]
  sku_message = ""
  sku_suppliers = len(item_master[sku]["suppliers"])
  sku_suppliers_message = ""

  totals += sku_value
  
  if sku_days_of_supply < sku_lead_time:
    sku_message = "At Risk"
  else:
    sku_message = "Ok"

  if sku_suppliers == 1:
    sku_suppliers_message = "Single Source"

  if "Domtar" in item_master[sku]["suppliers"]:
    domtar_suppliers.append(sku)

  print(f"{sku} · {sku_description} \nValue: ${sku_value} · Days of supply: {sku_days_of_supply} (lead time {sku_lead_time}) {sku_message} \nSuppliers: {sku_suppliers} {sku_suppliers_message}")
  section()

print(f"Total inventory value: ${totals} \nSKUs in item master: {sku_totals}")
divisions()

print(f"Domtar Supplies: {domtar_suppliers}")

