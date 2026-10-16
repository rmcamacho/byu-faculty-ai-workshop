# Learning Suite Exercise 1: Worked Answer

Prompt: [tutorial/2_LEARNING_SUITE.md](../tutorial/2_LEARNING_SUITE.md).

## Worked answer

| Student | Earned / possible | Percent | Follow-up |
|---|---:|---:|---|
| DEMO-01 | 132.4540 / 283 | 46.80% | HW3.1, HW3.3 and UQ2 missing |
| DEMO-02 | 96.9114 / 283 | 34.24% | Broad low performance, no missing submissions |
| DEMO-03 | 139.3356 / 283 | 49.24% | HW3.3 0/11; inspect node-voltage work |
| DEMO-07 | 149.9029 / 283 | 52.97% | UQ3 missing |

All four are E in this demo scale. DEMO-08 is D+ at 68.26%, reported separately rather than included below 67%. DEMO-09 is 81.65% overall with a useful improving pattern: early HW1.1/HW1.2/UQ1 were low, while UQ3 is 100/100.

Do not add DEMO-04, 05 or 06 to the missing-work queue. DEMO-04 has UQ2 awaiting grading (151.2722/183 = 82.66%, provisional); DEMO-05's HW3.3 extension is not due until October 19 (229.5482/272 = 84.39%); DEMO-06's HW1.2 is excused (212.8510/260 = 81.87%). These are distinct states.

## What the invented wrong answers add

The three questions in [diagnostic_checks.csv](../data/diagnostic_checks.csv) are original follow-up checks, not copied LS assessment questions. [diagnostic_responses.csv](../data/diagnostic_responses.csv) contains the invented submitted answers and working. Join these files on `check_id` and students on `student_id`. None of this diagnostic work changes a grade. DEMO-01 and DEMO-07 did not submit these optional checks; do not add them to the overdue-work queue or infer why they did not respond.

Check each question independently before interpreting a response:

| Check | Correct reasoning | Planted wrong answer and working | Pattern among respondents |
|---|---|---|---|
| BRANCH-01 | The resistor connects 8 V to 3 V through 1 kOhm: `(8 - 3)/1 = 5 mA` from a to b. | `8 mA`, using `I_ab = Va/R`. The work omits the voltage at the other end. | 8/22 use this pattern; 14/22 answer correctly; 2/24 did not submit. |
| POLARITY-01 | The source is positive at p: `Vp - Vn = 4 V`. With `Vn = 2 V`, `Vp = 6 V`. | `-2 V`, from `Vn - Vp = 4 V`. The source constraint is reversed. | 10/22 use this pattern; 12/22 answer correctly; 2/24 did not submit. |
| BOUNDARY-01 | The external resistor currents total `3 + 1 = 4 mA`. The 1 mA from a to b stays inside the combined boundary. | `5 mA`, adding the internal 1 mA to the external currents. | 6/22 use this pattern; 16/22 answer correctly; 2/24 did not submit. |

These are deliberately planted patterns in a fictional cohort, not estimates of how common these errors are among real students. A useful presentation sentence is: "Ten of the 22 fictional respondents reversed the polarity equation. This student's answer and working suggest that the source constraint is a useful place to check together." Do not say that many real students make this mistake without independent evidence.

DEMO-02 shows the branch-voltage and boundary patterns but answers the polarity check correctly. DEMO-03 shows all three patterns. Choose one manageable next step in each email rather than listing every error. The evidence is stronger than a zero alone, but it still does not show whether the student would explain the idea differently in conversation or whether it caused an error on a different assessment.

## Draft messages

Checkpoint 3 requests two missing-work messages (DEMO-01 and DEMO-07) and two diagnostic coaching messages (DEMO-02 and DEMO-03). Only the coaching messages cite diagnostic answers; the missing-work messages build on scored strengths and ask the student to check the record. Save participant drafts to `local/exercise-1/messages.md`, separate from this worked answer.

**DEMO-01 — Build on what is working**

Hi Demo Student 01,

You earned full credit on the node-voltage and DAC parts of Unit Quiz 3, so there is good work here to build on. Homework 3.1, Homework 3.3 and Unit Quiz 2 are marked missing. Could you check whether that record is accurate? Let's open Homework 3.3 together during office hours and choose one manageable next step after checking what the course policy permits. You do not need a finished solution before asking for help.

RMC

**DEMO-02 — One voltage difference to check together**

Hi Demo Student 02,

You've kept up with all eight submissions, and your polarity-check equation was correct. On the separate resistor check, you wrote `I = 8/1 = 8 mA`. Your answer suggests we should check which voltage belongs across the resistor. Its ends are at 8 V and 3 V, so the voltage across it is their difference: 5 V. Let's label both ends of one resistor in Homework 3.3 Q1–Q2 together before writing its current expression. Bring whatever work you have; we can start there.

RMC

**DEMO-03 — A source-polarity check before more algebra**

Hi Demo Student 03,

Your Thevenin-equivalence parts in Unit Quiz 3 were successful. On the separate polarity check, your `-2 V` answer came from `Vn - Vp = 4 V`. Your answer suggests we should check the source constraint together. The positive terminal is at p, so p is 4 V higher than n: `Vp - Vn = 4 V`, giving 6 V. Try marking the higher-potential terminal first, then let's revisit one source constraint in Homework 3.3's supernode block Q8–Q10. We can take it one equation at a time.

RMC

**DEMO-07 — Check the record and build from a successful part**

Hi Demo Student 07,

Unit Quiz 3 is marked missing. Could you check whether that status is accurate? You earned credit on several node-voltage parts and on Homework 3.3 Q10–Q11. Let's build from that work while we discuss the quiz options under the course policy. During office hours, we can compare your setup for Q8–Q9 with your successful Q10 work and choose one next practice step. Bring your setup even if it is unfinished, so we can see where to focus.

RMC

## Discussion

These are fictional drafts, not messages to real students. Use the response and work excerpt to explain a possible next step, not to diagnose the person or infer motivation, disability or circumstances. The original diagnostic answer may suggest what to check on HW3.3; it does not establish what went wrong on a copied LS question. Do not promise an extension or grade outcome. If helpful for node voltage or supernodes, offer the fictional Demo TA - Circuits session Tuesday, 1–2 p.m. Mountain in Demo room. Those details are invented, not Ryan's actual staffing schedule.
