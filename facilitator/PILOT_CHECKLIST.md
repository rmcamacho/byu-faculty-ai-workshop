# Participant Pilot Checklist

Use one faculty member's own computer and authorized accounts. Do not send their credentials, profile, gradebook or screenshots of real student records to the facilitator. No invitation or external message has been sent by this repository.

Record OS, Node version, Codex version, plugin version and pass/fail observations. Avoid recording login identifiers or authentication details.

1. Download the public ZIP without GitHub sign-in; extract and open the folder.
2. Run `python3 scripts/check_answers.py` (Windows: `py -3 scripts/check_answers.py`) if Python is available; expect PASS.
3. Follow tutorial/1_SETUP.md in a fresh Codex session; verify all three skills load.
4. Record which path the participant chose (desktop app or CLI). Open the browser as tutorial/1_SETUP.md describes and sign in manually. For the desktop app, record whether Codex used the built-in browser without being told; for the CLI, whether Chrome opened on the intended computer.
5. Copy Ryan's template into a new development course. Confirm all eight assessments, point totals, Start Here attachment and Lecture 10 access. Check dates separately because LS can remap them.
6. Ask the assistant to read the assignment inventory without edits. Confirm it reports your copy's title and Development status.
7. Run outreach analysis; expect DEMO-01/02/03/07 below 67%, DEMO-08 in D+ and the three exclusions treated correctly.
8. Run the teaching prompt. Confirm denominator handling and that proposals leave original slides unchanged.
9. Preview the Homework 3.3 deadline edit (tutorial/2_LEARNING_SUITE.md, Exercise 3). If you elect to apply it, approve the exact target and new value, then verify the reopened result. Restore the recorded original only if you explicitly choose to.
10. Optionally run Parts A and B of tutorial/3_KUALI.md and tutorial/4_WORKDAY.md and compare with answers/.
11. In the CLI, stop the dedicated browser. Record any unresolved problem in plain language.

Pilot completion requires actual observations for these steps. Automated source/unit tests and the owner's working LS session do not substitute for this pilot.
