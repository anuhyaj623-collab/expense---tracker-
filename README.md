# Expense Tracker

A Python-based personal expense tracker that analyzes spending from CSV data and generates category summaries and visual reports.

## Project Overview
This project demonstrates data ingestion, transformation, and reporting using core Python — no external libraries required.

## Features
- Loads and parses expense data from CSV
- Summarizes total spending by category
- Generates a text-based bar chart visualization
- Clean, formatted console output

## Project Structure
expense-tracker/
expenses.csv        # Raw expense data
analyze.py          # Category summary report
chart.py            # Text-based spending chart
README.md           # Project documentation

## How to Run

### Summary report
python analyze.py

### Spending chart
python chart.py

## Sample Output
===================================
   EXPENSE SUMMARY
===================================
  Entertainment    $   43.99
  Food             $  360.80
  Health           $   52.40
  Transport        $   87.50
  Utilities        $  175.00
-----------------------------------
  TOTAL            $  719.69
===================================

## Tech Stack
- Python 3.x
- CSV module (standard library)
- Collections module (standard library)
- Git + GitHub for version control

## Future Improvements
- Monthly spending breakdown (see issue #2)
- Export summary to text file (see issue #3)
- Extend dataset to 6 months (see issue #4)

## Author
Anuhya Juvvanthula
Data Engineering | Data Analytics | Business Intelligence
