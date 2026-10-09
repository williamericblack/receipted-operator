# Receipted Operator

A free Claude Code plugin that verifies AI agent work: receipts, a truthful status set, and an independent verifier that returns **FALSE_DONE** when an agent claims a task is complete and the artifact isn't there.

For anyone running AI agents who has been burned by green checkmarks that checked nothing.

**What it gives you**
- A decision doctrine: default-go rules, hard gates, and two permanent lines (email and money never automate).
- A truthful status set: `PROPOSED → AWAITING_APPROVAL → QUEUED → RUNNING → COMPLETED → VERIFIED`, plus `FAILED`, `BLOCKED_INFRASTRUCTURE`, `UNVERIFIED`. Never DONE without a receipt.
- A receipt ledger shape you can drop into Notion, a spreadsheet, or a folder.
- An independent verifier (`verify/verify.py`, standard library only) that checks claimed artifacts against a manifest and returns **FALSE_DONE** when a completion claim has nothing behind it.
- A brief template that forces an observable outcome and a demonstrated-failure done-test.

**Install (Claude Code)**
```
/plugin marketplace add datumline/receipted-operator
/plugin install receipted-operator@datumline
```

**Skills**
- `/receipt` – write a receipt in the ledger shape for the work just done.
- `/verify` – run the verifier against a manifest and report VERIFIED / FAILED / FALSE_DONE.
- `/brief` – turn a request into an outcome-plus-falsification brief.
- `/session-open` – write a timestamped, attributed session record before new work.

**The one rule this plugin is built on:** the thing that audits the work must not share code, process, or state with the thing that did the work. `verify/verify.py` imports nothing from your runtime. That is why it can call your runtime a liar.

**Proof it works (do this once):** mark any job COMPLETED with no artifact, run `/verify`. You should see `FALSE_DONE`. If you see green, the plugin is broken and you should not trust it.

Not a security audit. Not a compliance certification. A tool you run on your own work. Composes with cryptographic tool-call receipts (e.g. protect-mcp) which sign *that a call happened*; this verifies *that the job produced its artifact*.

## Going further

- **[Receipted Operator Pro](https://datumlinehq.gumroad.com/l/receipted-operator-pro)**: this plugin plus Audit Trail and the Governance Gate Kit, which are not in this repository.
- **[Datumline methods](https://datumline.github.io/receipted-operator/)**: working kits for agent governance, audit trails, decomposition, decorrelated ideation, deal assessment, portfolio estimates and real-estate calculations. Every kit ships scripts whose tests fail when the method is broken.
- **[Store](https://datumlinehq.gumroad.com)**

Datumline LLC · MIT license · v0.1.1
