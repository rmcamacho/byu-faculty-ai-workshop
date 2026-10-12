# Agentic AI for Faculty with Learning Suite

A self-guided companion to the October 16, 2026 faculty lunch and learn. Start with [the workshop guide](tutorial/START_HERE.md), [connect Codex to LS](tutorial/SETUP.md), and [copy the development course](tutorial/COPY_COURSE.md). For presenting, use the [20-minute run of show](tutorial/PRESENTER_RUN_OF_SHOW.md).

Repository: https://github.com/rmcamacho/faculty-ls-demo

## Synthetic student support

All students, results, TA hours, approvals and contact details in this package are fictional. They are NOT anonymized or derived from any real student. The example.invalid addresses cannot deliver mail.

## What is live

The development course **Agentic AI Faculty Demo - Synthetic** contains five homework sets (1.1, 1.2, 2.4, 3.1 and 3.3), Unit Quizzes 1–3, the source syllabus, Lectures and Extra Course Help copied from Ryan's Fall 2026 combined 240/301 course. Copies are separate LS materials. Google Slides links still refer to original decks; propose revisions without editing those decks.

BYU documents that development courses do not have enrolled students or a working student gradebook. These files supply the fictional student results. They are course-content attachments, not native gradebook records, and must not be imported into a live course.

## Start here

1. Read manifest.json for provenance, grading rules and limitations.
2. Read data/students.csv, assignments.csv and assessment_results.csv.
3. For problem-level analysis, join question_results.csv to question_map.csv on assignment_id + item, and join students on student_id. Problem-level data exists only for Homework 3.3 and Unit Quiz 3.
4. Open the matching copied LS assignment and lecture links to inspect the real instructional material.
5. Compare your calculations with expected_student_summary.csv and expected_concept_summary.csv only after completing the exercise.

Snapshot: October 16, 2026 at 10 a.m. Mountain. All dates have an explicit offset. DEMO identifiers are local fictional identifiers, not BYU NetIDs.

## Grading rules for this demonstration

Use total points over this eight-assessment subset, with no dropped scores. Full possible total is 283. This is intentionally NOT the weighted grading policy in the source course syllabus. Do not call this a student's actual course grade.

Missing overdue work counts as zero. Excused, extension_not_due and submitted_ungraded work is excluded from both numerator and denominator. Flag pending grading as incomplete evidence. A scored zero is different from a missing submission. Unit Quiz 3 has 15 raw question points scaled to 100 gradebook points; Homework 3.3 is 11 unscaled points.

The copied grade scale has D+ at 67%, D at 63%, D- at 60%, and E below 60%. Interpret “D or below” as below 67% for this demo; list D+ students separately. If the university's actual outreach rule differs, confirm it before using the exercise on real records.

## Exercise 1: timely and specific outreach

Prompt: “Using this fictional dataset and its stated grading rules, identify students currently at D or below. Show the denominator, missing work, excluded work and evidence gaps. Distinguish incomplete work from demonstrated concept difficulty. Draft brief encouraging messages with specific assignments or question parts to review online. Use the fictional TA schedule only when relevant. Do not send anything. Sign student drafts RMC.”

Use DEMO-01 for missing-work discussion, DEMO-02 for broad difficulty, DEMO-03 for node-voltage difficulty, DEMO-09 for an improving trend. DEMO-04 has submitted work awaiting grading; DEMO-05 has a future approved deadline; DEMO-06 has an excused assignment. Never infer motivation, health, disability or life circumstances from scores.

## Exercise 2: improve teaching

Prompt: “Find recurring concept difficulties among graded submissions, keeping missing work separate. Compare HW3.3 with UQ3, cite exact mapped question/part labels, and show denominators. Open Lecture 10 via the copied LS Lectures page. Recommend a worked example, a misconception check and a short in-class activity based on what the slides actually contain. Treat scores as evidence to investigate, not proof of a teaching failure. Do not change the original slides.”

The dataset deliberately includes a node-voltage/supernode pattern. Aggregate scores for other assignments do not establish which questions were missed. The question map includes structure and maxima, not copyrighted question text, diagrams or answer keys.

## Exercise 3: administrative help

Prompt: “Compare copied assignment instructions with the syllabus AI policy and propose exact changes only if a discrepancy exists. Preview a course-wide deadline change in this development course. For approved_demo_changes.csv, prepare a per-student change preview but do not claim it was applied in LS: those fictional students are not enrolled.”

Any live demo edit should target this development course explicitly and be verified afterward. The synthetic approval file is exercise data, not authority to change a real student's record. Native accommodations cannot be demonstrated as completed without supported test enrollments.

## Rebuild and checks

Run `python3 build_demo.py` (Python standard library only). It deterministically regenerates 24 students, 192 assessment records, 552 question-part records, expected summaries and the ZIP. Assertions check joins, point ranges, scaling, excluded-work denominators and non-deliverable addresses. It never connects to LS.

Continue with tutorial/START_HERE.md and tutorial/COPY_COURSE.md. Detailed prompts, worked answers and a 20-minute presenter script are included. Run python3 scripts/check_answers.py to independently verify the calculations. The CLI setup guide pins the existing browser plugin; a participant-machine installation and second-faculty copy dry run remain to be tested. See tutorial/PARTICIPANT_PILOT.md.
