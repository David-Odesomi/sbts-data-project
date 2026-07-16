# SBTS Data Project — Auto-Reporting Dashboard

A small internal project to turn a manually-updated spreadsheet into a
one-click summary and chart. Built as a learning project by the team below,
using real SQL/Python skills on real (or realistic) data instead of
LeetCode puzzles.

## Team

| Name | Role |
|------|------|
|      | Project lead |
|      | Data cleaning |
|      | Reporting / charts |
|      | (add more rows as needed) |

## What this project does

1. **Load** — reads the raw orders spreadsheet (`data/`)
2. **Clean** — fixes messy real-world data problems:
   - inconsistent text (`Paid` vs `paid` vs `PAID`)
   - numbers stored as text (`NGN 219,972`)
   - mixed date formats
   - duplicate rows
3. **Summarize** — produces a short written summary and (soon) a chart

## Folder structure

```
sbts-data-project/
├── data/
│   └── dummy_client_orders.csv     ← practice data (swap for real data later)
├── clean_and_report.py             ← the main script
├── output/
│   └── summary.txt                 ← generated each time the script runs
└── README.md                       ← this file
```

## How to run it

```bash
pip install pandas openpyxl
python3 clean_and_report.py
```

The summary prints to the screen and also saves to `output/summary.txt`.

## Status

- [x] Load + clean the data
- [x] Generate a text summary
- [ ] Add a chart
- [ ] Swap in real office data
- [ ] Automate it to run weekly

## Notes

- Dummy data is fake (generated for practice) — safe to share, no real client
  info in it.
- Once we're comfortable with the pipeline, we'll ask for a real spreadsheet
  to plug in.