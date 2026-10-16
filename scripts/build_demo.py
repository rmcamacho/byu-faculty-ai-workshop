"""Build reproducible, entirely fictional workshop data; never contacts Learning Suite."""
from pathlib import Path
import csv
import json
import random
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)
RNG = random.Random(20261016)
COURSE = 'https://learningsuite.byu.edu/.dr2r/cid-qn1ynCTVWQDe'

def write_csv(name, rows):
    with (DATA / name).open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

assignments = [
    ('HW1.1', 'Homework 1.1 (Voltage, Current, Power, and Sign Conventions)', 12, '2026-09-18', 'Lecture 1'),
    ('HW1.2', "Homework 1.2 (Ohm's Law and Kirchhoff's Laws)", 23, '2026-09-18', 'Lecture 2'),
    ('HW2.4', 'Homework 2.4 (Resistor Networks, Voltage and Current Division)', 8, '2026-09-25', 'Lecture 7'),
    ('HW3.1', 'Homework 3.1 (Source Transformations, Thevenin Equivalence, Maximum Power Transfer)', 9, '2026-10-02', 'Lecture 8'),
    ('HW3.3', 'Homework 3.3 (Node Voltage and Supernodes)', 11, '2026-10-02', 'Lecture 10'),
    ('UQ1', 'Unit Quiz 1', 20, '2026-09-18', 'Unit 1'),
    ('UQ2', 'Unit Quiz 2', 100, '2026-09-25', 'Unit 2'),
    ('UQ3', 'Unit Quiz 3', 100, '2026-10-02', 'Lectures 8-11'),
]
write_csv('assignments.csv', [dict(assignment_id=a, title=t, points_possible=p,
    due_at=d+'T23:59:00-06:00', lecture_reference=l, synthetic_results=True)
    for a,t,p,d,l in assignments])
students = [dict(student_id=f'DEMO-{i:02}', display_name=f'Demo Student {i:02}',
    email=f'student{i:02}@example.invalid', fictional=True) for i in range(1,25)]
write_csv('students.csv', students)

# Question/part numbering and maxima were read from the copied LS assessments.
# No question text, diagrams, answer keys or actual student responses are exported.
parts = []
for n in range(1,12):
    block = 'Node Voltage Method' if n<=2 else 'Node Voltage Round 2' if n<=7 else 'Supernodes' if n<=10 else 'Supernodes Round 2'
    parts.append(dict(assignment_id='HW3.3', item=f'Q{n}', block=block,
        concept='Node voltage' if n<=7 else 'Supernodes', max_points=1,
        lecture_reference='Lecture 10', source=COURSE+'/exam/questions/id-ogfV'))
for n in range(1,13):
    block, concept, points, lecture = (
        ('Norton Equivalence', 'Source equivalence', 2, 'Lecture 8') if n<=2 else
        ('Thevenin Equivalence', 'Source equivalence', 1, 'Lecture 8') if n<=4 else
        ('Batteries', 'Battery models', 1, 'Lecture 9') if n<=8 else
        ('Node Voltage', 'Node voltage', 2, 'Lecture 10') if n==9 else
        ('DAC (Voltage Mode)', 'DAC', 1, 'Lecture 11') if n==10 else
        ('R-2R ladder voltage mode', 'DAC', 1, 'Lecture 11'))
    parts.append(dict(assignment_id='UQ3', item=f'Part{n}', block=block,
        concept=concept, max_points=points, lecture_reference=lecture,
        source=COURSE+'/exam/questions/id-H6m9'))
write_csv('question_map.csv', parts)
assert sum(p['max_points'] for p in parts if p['assignment_id']=='HW3.3') == 11
assert sum(p['max_points'] for p in parts if p['assignment_id']=='UQ3') == 15

results, detail = [], []
for i, student in enumerate(students, 1):
    for j,(aid,title,maximum,due,lecture) in enumerate(assignments):
        status = 'graded'
        if (i==1 and aid in ('UQ2','HW3.1','HW3.3')) or (i==7 and aid=='UQ3'):
            status = 'missing'
        elif i==4 and aid=='UQ2': status='submitted_ungraded'
        elif i==5 and aid=='HW3.3': status='extension_not_due'
        elif i==6 and aid=='HW1.2': status='excused'
        effective_due = '2026-10-19T23:59:00-06:00' if status=='extension_not_due' else due+'T23:59:00-06:00'
        base = {1:.83,2:.44,3:.62,4:.88,5:.84,6:.88,7:.85,8:.68}.get(i, .78+(i%5)*.035)
        if i==9: base=.45 if aid in ('HW1.1','HW1.2','UQ1') else .91
        raw = None
        mapped = [p for p in parts if p['assignment_id']==aid]
        if mapped:
            raw=0
            for p in mapped:
                probability=base
                # Deliberate recurring cohort difficulty on node voltage/supernodes.
                if p['concept'] in ('Node voltage','Supernodes'):
                    probability -= .32 if i>=10 else .22
                if i==3 and p['concept'] in ('Node voltage','Supernodes'): probability=.05
                got = p['max_points'] if RNG.random()<max(.02,probability) else 0
                if status!='graded': got=''
                else: raw+=got
                detail.append(dict(student_id=student['student_id'], assignment_id=aid,
                    item=p['item'], concept=p['concept'], earned_points=got,
                    max_points=p['max_points'], status=status, fictional=True))
            score = round(raw/15*100,4) if aid=='UQ3' else raw
        else:
            score=round(max(0,min(1,base+RNG.uniform(-.07,.07)))*maximum,4)
        if status!='graded': score=''
        results.append(dict(student_id=student['student_id'], assignment_id=aid,
            status=status, earned_points=score, points_possible=maximum,
            effective_due_at=effective_due, fictional=True))
write_csv('assessment_results.csv', results)
write_csv('question_results.csv', detail)
write_csv('demo_ta_hours.csv', [dict(ta='Demo TA - Circuits', day='Tuesday',
    start='13:00',end='14:00',timezone='America/Denver', location='Demo room (fictional)',
    topics='Node voltage; supernodes; source equivalence', fictional=True)])
write_csv('approved_demo_changes.csv', [
    dict(student_id='DEMO-05',assignment_id='HW3.3',kind='deadline_extension',
         value='2026-10-19T23:59:00-06:00',status='fictional approval; dataset only'),
    dict(student_id='DEMO-10',assignment_id='UQ3',kind='time_limit_minutes',
         value='90',status='fictional approval; preview only; no LS student exists')])

scale=[('A',93),('A-',90),('B+',87),('B',83),('B-',80),('C+',77),('C',73),('C-',70),('D+',67),('D',63),('D-',60),('E',0)]
summary=[]
for s in students:
    rows=[r for r in results if r['student_id']==s['student_id']]
    included=[r for r in rows if r['status'] in ('graded','missing')]
    numerator=sum(float(r['earned_points'] or 0) for r in included)
    denominator=sum(r['points_possible'] for r in included)
    pct=100*numerator/denominator
    grade=next(g for g,cutoff in scale if pct>=cutoff)
    summary.append(dict(student_id=s['student_id'], percent=round(pct,4),grade=grade,
        earned=round(numerator,4),possible=denominator,
        outreach_candidate=pct<67, d_plus_watch=67<=pct<70,
        missing='; '.join(r['assignment_id'] for r in rows if r['status']=='missing'),
        incomplete_evidence=any(r['status']=='submitted_ungraded' for r in rows)))
write_csv('expected_student_summary.csv',summary)

concepts=defaultdict(lambda:[0,0,0])
for r in detail:
    if r['status']=='graded':
        x=concepts[(r['assignment_id'],r['concept'])]
        x[0]+=r['earned_points']; x[1]+=r['max_points'];x[2]+=1
write_csv('expected_concept_summary.csv',[dict(assignment_id=a,concept=c,
    earned=v[0],possible=v[1],percent=round(100*v[0]/v[1],4),graded_parts=v[2])
    for (a,c),v in concepts.items()])

manifest=dict(title='Faculty LS Demo — Synthetic Student Results',
    version='2026-10-11-v1',snapshot='2026-10-16T10:00:00-06:00',course_url=COURSE+'/home',
    synthetic=True,student_count=len(students),assessment_count=len(assignments),
    source='Assignment names, maxima, copied due dates, grade scale and selected question structure verified in the development course October 11. All student identities, results, statuses, TA hours and approvals are invented.',
    grading='Demo subset: total points, no drops. Missing overdue work is zero; excused, extension_not_due and submitted_ungraded are excluded from numerator and denominator. UQ3 raw 15 points scale to 100. Full possible total 283.',
    outreach='D or below means D/D-/E: percent <67. D+ (67 to <70) is a separate watch band. This is an explicit demo interpretation, not a university-wide threshold.',
    limitations=['Development courses have no enrolled students or working student gradebook; CSV files are content attachments, not native enrollments or recorded grades.',
        'Source syllabus describes full-course weighted categories and dropped scores; that policy does NOT govern this reduced demo dataset.',
        'Only HW3.3 and UQ3 have problem-level data; do not invent missed questions for other assignments.',
        'Copied lecture links still point to original Google decks. Read them for proposals; do not edit originals during demos.',
        'Native student-specific exceptions and real gradebook analysis require supported test enrollments elsewhere; demonstrate proposed changes locally.',
        'Course questions and source decks are not included in this public repository; do not redistribute copyrighted questions or solutions without permission.'],
    support_source='https://softwaresupport.byu.edu/learning-suite/instructor/setup-and-basics/course-setup')
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')

# Integrity checks cover joins, score scaling, missing-state semantics and denominators.
assert len(results)==192 and len(detail)==552
assert len({(r['student_id'],r['assignment_id']) for r in results})==192
for r in results:
    assert r['student_id'] in {s['student_id'] for s in students}
    if r['status']=='graded': assert 0<=r['earned_points']<=r['points_possible']
    else: assert r['earned_points']==''
    qs=[q for q in detail if q['student_id']==r['student_id'] and q['assignment_id']==r['assignment_id']]
    if qs and r['status']=='graded':
        total=sum(q['earned_points'] for q in qs)
        expected=round(total/15*100,4) if r['assignment_id']=='UQ3' else total
        assert expected==r['earned_points']
assert next(s for s in summary if s['student_id']=='DEMO-04')['possible']==183
assert next(s for s in summary if s['student_id']=='DEMO-05')['possible']==272
assert next(s for s in summary if s['student_id']=='DEMO-06')['possible']==260
assert all(s['email'].endswith('@example.invalid') for s in students)

print(json.dumps(dict(students=len(students),assessments=len(assignments),question_rows=len(detail),
    outreach_candidates=[s['student_id'] for s in summary if s['outreach_candidate']],checks='passed'),indent=2))
