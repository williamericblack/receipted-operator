---
name: receipt
description: Write a receipt for work just completed, in the Receipted Operator ledger shape. Use whenever a job, task, or work order is being marked COMPLETED, or when someone asks "is this done?"
---
When the user marks work complete or asks for a receipt:
1. Read `templates/receipt.md` in this plugin.
2. Fill every field from what was ACTUALLY produced. For each artifact, state its path or URL and compute its sha256 if it is a local file.
3. The verdict is never VERIFIED unless `/verify` has been run against a manifest naming those artifacts. Until then the verdict is PARTIAL or UNVERIFIABLE.
4. Write the "Not claimed" line. A receipt that claims everything is worth nothing.
5. Save the receipt next to the work (e.g. `receipts/RECEIPT_<id>_<date>.md`) and tell the user the path.
Never mark a status COMPLETED without a receipt path. If the user insists, write the receipt with verdict UNVERIFIABLE and say so.
