# 📊 CSV Row Expander — Duplicate Rows Based on Quantity for Data Merge

This Python script takes a `.csv` file (with a **Quantity** column) and outputs a new file where each row is **repeated** according to its quantity. Perfect for preparing Data Merge files in **Adobe InDesign** when certain records need to appear multiple times.

---

## ✅ Features

- 🔁 Expands rows based on the `Quantity` column
- ✂️ Automatically **removes** the Quantity column in output
- 🧠 Skips or defaults invalid/missing quantities to 1
- 📝 Keeps all original columns except `Quantity`
- 📄 Output ready for direct use in InDesign Data Merge
- 🔧 Easily customizable

---

## 📥 Input Example (`input.csv`)

Name,Price,Quantity
Hammer,100,5
Screwdriver,75,2
Wrench,80,1

----

## 📤 Output Example('output.csv')

Name,Price
Hammer,100
Hammer,100
Hammer,100
Hammer,100
Hammer,100
Screwdriver,75
Screwdriver,75
Wrench,80

---

## 🚀 How to Use

Make sure Python is installed on your system

Save your data file as input.csv (or update the script to match your filename)

Run the script:

The script will generate output.csv with expanded rows.

---

## 🧱 Requirements
Python 3.x

No external libraries required

---

## 👨‍💻Author

Created by Swirik