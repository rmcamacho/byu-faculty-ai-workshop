"""Independently validate workshop answers from the distributed CSVs; no network."""
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
import csv
import json
import math

root = Path(__file__).resolve().parents[1]
def read(name):
    with (root / 'data' / (name + '.csv')).open(newline='') as f:
        return list(csv.DictReader(f))

students = read('students')
assignments = {r['assignment_id']: r for r in read('assignments')}
results = read('assessment_results')
questions = read('question_results')
mapping = {(r['assignment_id'], r['item']): r for r in read('question_map')}
expected = {r['student_id']: r for r in read('expected_student_summary')}
snapshot = datetime.fromisoformat(json.loads((root / 'manifest.json').read_text())['snapshot'])
assert len(students) == 24 and len(assignments) == 8 and len(results) == 192
assert len({(r['student_id'],r['assignment_id']) for r in results}) == len(results)
assert len({(r['student_id'],r['assignment_id'],r['item']) for r in questions}) == len(questions) == 552
assert all(s['email'].endswith('@example.invalid') for s in students)
flags, watch = [], []
for student in students:
    sid = student['student_id']
    earned = possible = 0
    rows = [r for r in results if r['student_id'] == sid]
    assert len(rows) == 8
    for r in rows:
        maximum = float(assignments[r['assignment_id']]['points_possible'])
        assert float(r['points_possible']) == maximum
        if r['status'] == 'graded':
            score = float(r['earned_points'])
            assert 0 <= score <= maximum
            earned += score
            possible += maximum
        elif r['status'] == 'missing':
            assert datetime.fromisoformat(r['effective_due_at']) < snapshot
            assert r['earned_points'] == ''
            possible += maximum
        else:
            assert r['status'] in ('excused', 'extension_not_due', 'submitted_ungraded')
            assert r['earned_points'] == ''
            if r['status'] == 'extension_not_due':
                assert datetime.fromisoformat(r['effective_due_at']) > snapshot
    percent = earned / possible * 100
    e = expected[sid]
    assert math.isclose(earned, float(e['earned']), abs_tol=.0001)
    assert possible == float(e['possible'])
    assert math.isclose(percent, float(e['percent']), abs_tol=.0001)
    if percent < 67: flags.append(sid)
    elif percent < 70: watch.append(sid)
assert flags == ['DEMO-01', 'DEMO-02', 'DEMO-03', 'DEMO-07']
assert watch == ['DEMO-08']
aggregates = defaultdict(lambda: [0, 0, 0, set()])
raw_scores = defaultdict(float)
status_counts = Counter()
for r in questions:
    m = mapping[(r['assignment_id'], r['item'])]
    assert r['concept'] == m['concept']
    assert float(r['max_points']) == float(m['max_points'])
    status_counts[r['status']] += 1
    if r['status'] != 'graded':
        assert r['earned_points'] == ''
        continue
    score = float(r['earned_points'])
    assert 0 <= score <= float(m['max_points'])
    raw_scores[(r['student_id'], r['assignment_id'])] += score
    a = aggregates[(r['assignment_id'], m['concept'])]
    a[0] += score
    a[1] += float(m['max_points'])
    a[2] += 1
    a[3].add(r['student_id'])
for r in results:
    if r['status'] == 'graded' and r['assignment_id'] in ('HW3.3', 'UQ3'):
        raw = raw_scores[(r['student_id'],r['assignment_id'])]
        scaled = raw if r['assignment_id'] == 'HW3.3' else raw * 100 / 15
        assert math.isclose(scaled,float(r['earned_points']),abs_tol=.0001)
for e in read('expected_concept_summary'):
    a = aggregates[(e['assignment_id'],e['concept'])]
    assert a[0] == float(e['earned']) and a[1] == float(e['possible'])
    assert a[2] == int(e['graded_parts'])
    assert math.isclose(100*a[0]/a[1],float(e['percent']),abs_tol=.0001)
assert aggregates[('HW3.3','Node voltage')][:2] == [71,154]
assert aggregates[('HW3.3','Supernodes')][:2] == [46,88]
assert aggregates[('UQ3','Node voltage')][:2] == [32,46]
# Check the new worked circuit and reversed-polarity exit ticket, in V/kOhm/mA.
for va,vb,voltage in [(11/3,2/3,3),(5/3,14/3,-3)]:
    assert math.isclose(va/2+vb/4,2)
    assert math.isclose(va-vb,voltage)
print('PASS: joins, statuses, deadlines, denominators, four candidates, D+ watch, concept evidence, quiz scaling and both circuit solutions.')
