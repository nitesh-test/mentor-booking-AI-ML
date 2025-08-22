import csv
import random
from pathlib import Path

def generate_dataset():
    random.seed(42)
    data_dir = Path(__file__).resolve().parents[1] / 'data'
    data_dir.mkdir(exist_ok=True)
    subtopics = ['Factoring', 'Roots', 'Vertex', 'Discriminant', 'Graphing']
    question_rows = []
    metadata_rows = []
    question_info = []  # (qid, correct_answer, subtopic)
    for i in range(1, 51):
        qid = f'Q{i}'
        subtopic = subtopics[(i - 1) // 10]
        difficulty = 'Easy' if i <= 25 else 'Medium'
        marks = 1 if difficulty == 'Easy' else 2
        if subtopic == 'Factoring':
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            s = a + b
            content = f'If (x - {a})(x - {b}) = 0, what is the sum of roots?'
            options = [str(s), str(s + 1), str(s - 1), str(s + 2)]
            correct = 'A'
        elif subtopic == 'Roots':
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            prod = a * b
            content = f'Given x^2 - {(a + b)}x + {prod} = 0, what is the product of roots?'
            options = [str(prod), str(prod + 1), str(prod - 1), str(prod + 2)]
            correct = 'A'
        elif subtopic == 'Vertex':
            h = random.randint(-5, 5)
            k = random.randint(-5, 5)
            content = f'For y = (x - {h})^2 + {k}, what is the x-coordinate of the vertex?'
            options = [str(h), str(h + 1), str(h - 1), str(h + 2)]
            correct = 'A'
        elif subtopic == 'Discriminant':
            bcoeff = random.randint(1, 10)
            ccoeff = random.randint(-5, 5)
            disc = bcoeff * bcoeff - 4 * ccoeff
            content = f'What is the discriminant of x^2 + {bcoeff}x + {ccoeff} = 0?'
            options = [str(disc), str(disc + 1), str(disc - 1), str(disc + 2)]
            correct = 'A'
        else:  # Graphing
            acoeff = random.choice([-2, -1, 1, 2])
            direction = 'up' if acoeff > 0 else 'down'
            content = f'For y = {acoeff}x^2, which direction does the parabola open?'
            options = ['up', 'down', 'left', 'right']
            correct = 'A' if direction == 'up' else 'B'
        question_rows.append([qid, content, correct, *options])
        metadata_rows.append([qid, 'Quadratic Equations', subtopic, difficulty, marks, 'MCQ'])
        question_info.append((qid, correct, subtopic))
    with (data_dir / 'questions.csv').open('w', newline='') as fq:
        writer = csv.writer(fq)
        writer.writerow(['question_id', 'content', 'correct_answer', 'option_a', 'option_b', 'option_c', 'option_d'])
        writer.writerows(question_rows)
    with (data_dir / 'question_metadata.csv').open('w', newline='') as fm:
        writer = csv.writer(fm)
        writer.writerow(['question_id', 'topic', 'sub_topics', 'difficulty', 'marks', 'question_type'])
        writer.writerows(metadata_rows)
    with (data_dir / 'student_responses.csv').open('w', newline='') as fr:
        writer = csv.writer(fr)
        writer.writerow(['student_id', 'question_id', 'student_response', 'correct_answer', 'time_taken_sec', 'is_correct'])
        for s in range(1, 51):
            sid = f'S{s}'
            # deterministic strong/weak for reproducibility
            strong = subtopics[(s - 1) % len(subtopics)]
            weak = subtopics[(s) % len(subtopics)]
            if s == 1:
                strong, weak = 'Roots', 'Discriminant'
            for qid, correct, topic in question_info:
                if topic == strong:
                    prob = 0.95
                elif topic == weak:
                    prob = 0.2
                else:
                    prob = 0.6
                is_corr = random.random() < prob
                if is_corr:
                    resp = correct
                else:
                    options = ['A', 'B', 'C', 'D']
                    options.remove(correct)
                    resp = random.choice(options)
                time_taken = random.randint(20, 60)
                writer.writerow([sid, qid, resp, correct, time_taken, str(is_corr)])

if __name__ == '__main__':
    generate_dataset()
