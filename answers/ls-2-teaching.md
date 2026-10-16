# Learning Suite Exercise 2: Worked Answer

Prompt: [tutorial/2_LEARNING_SUITE.md](../tutorial/2_LEARNING_SUITE.md).

## Evidence and interpretation

| Assessment and concept | Points | Percent | Students |
|---|---:|---:|---:|
| HW3.3 node voltage, Q1–Q7 | 71/154 | 46.10% | 22 |
| HW3.3 supernodes, Q8–Q11 | 46/88 | 52.27% | 22 |
| UQ3 node voltage, Part9 | 32/46 | 69.57% | 23 |
| UQ3 source equivalence, Parts1–4 | 115/138 | 83.33% | 23 |
| UQ3 battery models, Parts5–8 | 73/92 | 79.35% | 23 |
| UQ3 DAC, Parts10–12 | 54/69 | 78.26% | 23 |

HW3.3 excludes one missing submission and one extension not due; UQ3 excludes one missing submission. Graded parts are not independent students. UQ3's raw 15 points scale to 100 for the overall grade; concept calculations use raw item maxima. Different students, item counts and difficulty prevent calling the two percentages a measured learning gain. No UQ3 item is separately mapped to supernodes, so a repeated supernode deficit is not established.

## Changes grounded in Lecture 10

The October 11 text read of Lecture10-Node voltage identifies slide 11's “Fireworks Convention,” slide 18's linear-system code, slide 22's supernode explanation, and slide 40's summary. This is a text-based review; embedded circuit diagrams require visual review before adapting them.

After slide 11, add a one-minute sign check: “With v1=2 V, v2=5 V and R=1 kΩ, what is the current leaving node 1 toward node 2?” Correct answer: (2−5)/1 kΩ = −3 mA; the actual current enters node 1. Distractors +3 mA and 7 mA diagnose direction and sum-versus-difference errors only if students explain their choices.

On slide 22, replace the absolute claim that KCL cannot be written at the two nodes with: “KCL still applies at each node. The voltage-source current is an additional unknown; combining the two nodes eliminates that internal current. Add the source-voltage constraint to close the system.” This avoids implying that KCL stops being valid. A supernode approach is also possible when other internal elements are in parallel with the voltage source.

On slide 18, propose `np.linalg.solve(A, b)` and MATLAB `A\b` in place of explicitly forming inverses. Ask learners to check the equation residual afterward. These are proposed improvements; the original slides remain unchanged.

## Original worked example

Draw a 2 kΩ resistor from node A to ground, a 4 kΩ resistor from node B to ground, and an ideal 3 V source between A (+) and B (−). A 2 mA current source injects current from ground into A.

1. Circle A and B as one supernode.
2. Write external-current KCL: VA/2 kΩ + VB/4 kΩ = 2 mA.
3. Write the source constraint: VA − VB = 3 V.
4. Solve 2VA + VB = 8 and VA − VB = 3: VA = 11/3 V and VB = 2/3 V.
5. Check: 11/6 mA + 1/6 mA = 2 mA; the difference is 3 V.
6. The source current from A to B is 1/6 mA. Individual-node KCL works when this unknown is included.

This new example is independent of the source assessment questions. It illustrates the proposed scaffolding without reproducing an answer key.

## Three-minute activity and exit ticket

Give pairs the circuit above. For 45 seconds they circle the boundary and label source polarity; for 60 seconds they write the two equations without solving; for 45 seconds they exchange and diagnose a deliberately reversed constraint VB−VA=3; use 30 seconds for a class explanation.

Exit ticket: reverse only the voltage-source polarity. The constraint becomes VA−VB=−3, giving VA=5/3 V and VB=14/3 V. Ask for both equations and one numerical check. Use the explanations to decide whether another sign-convention example is needed.
