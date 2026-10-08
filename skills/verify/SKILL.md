---
name: verify
description: Independently verify that claimed work produced its artifacts. Runs verify/verify.py against a manifest and reports VERIFIED, FAILED, or FALSE_DONE. Use before accepting any COMPLETED claim.
---
1. Build a manifest JSON (see the docstring in `verify/verify.py`) naming the job, the claimed status, and every artifact the completion claim rests on, with at least one real check per artifact (min_bytes, must_contain, required_keys, sha256, or HTTP status).
2. Run: `python3 <plugin>/verify/verify.py manifest.json --json`
3. Report the verdict verbatim. FALSE_DONE means the claim is false: the status must be reverted to RUNNING or FAILED and the user told plainly.
4. Save the JSON receipt beside the work.
Do not write a manifest with an empty artifact list to get a green result; the verifier refuses that (UNVERIFIABLE) by design.
