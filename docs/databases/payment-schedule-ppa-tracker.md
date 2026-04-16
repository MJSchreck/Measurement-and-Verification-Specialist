# Payment Schedule & PPA Tracker

> **Source:** Notion Database `b86edd25ed2a4ac5b08c5effff0d5085`
> **Data Source:** `collection://c0382b91-b403-4396-a7a8-19e54744a677`
> **Snapshot Date:** April 16, 2026

---

## Schema

| Property | Type | Options / Format |
|---|---|---|
| Payment Description | Title | — |
| Contract | Select | NDER2 SF, NDER2 LA, NDER2 SD, LA ESPC, PJKK, McKinstry, UESC PG&E, UESC SDG&E |
| Payment Type | Select | Annual Debt Service, M&V, Utility Payment |
| Status | Select | Pending Invoice, Invoice Received, RR Created, Processing, Paid, Overdue |
| Amount | Number | Dollar |
| Principal | Number | Dollar |
| Interest | Number | Dollar |
| Due Date | Date | — |
| PPA Deadline | Date | — |
| Days to PPA | Number | — |
| Invoice Number | Text | — |
| RR Number | Text | — |
| CLIN | Text | — |
| Service Period | Text | — |

---

## Records

No records were returned from the data source search. The database schema is configured and ready for payment tracking entries. Payment records are managed through EASi and Pegasys integrations and populated as invoices are received and processed.
