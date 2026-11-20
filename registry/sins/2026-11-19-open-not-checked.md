# Sin record – said a document was open without checking
Date: 2026-11-19
Fault: Agent – Claude Code
Classes: E (silent failure)
Register row: [CLH-2026-11-19-06](../OBSERVATIONS.md)

## Evidence
Twice I said the document was open in Word without checking that a visible window showed it. Word processes left without a window (render instances) likely took the file, so the operator could not find it and had to ask three times.

## Required response rules
- After opening a file for the operator, check that a visible window with the file's name is in front before saying it is open; if not, open it in a new visible instance.
