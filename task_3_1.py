from flask import Flask


app = Flask(__name__)


def get_intersection(first_interval, second_interval):
    first_interval_start, first_interval_end = first_interval[0], first_interval[1]
    second_interval_start, second_interval_end = second_interval[0], second_interval[1]
    latest_start = max(first_interval_start, second_interval_start)
    earliest_end = min(first_interval_end, second_interval_end)
    if latest_start <= earliest_end:
        intersection = [latest_start, earliest_end]
    else:
        intersection = [0, 0]
    return intersection


@app.route('/')
def appearance():
    intervals = {
                 'lesson': [1594663200, 1594666800],
                 'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                 'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
                 }
    pupil_time_intervals = [list(i) for i in list(zip(*[iter(intervals['pupil'])] * 2))]
    tutor_time_intervals = [list(i) for i in list(zip(*[iter(intervals['tutor'])] * 2))]
    lesson_time_intervals = [intervals['lesson']]
    intersection_pupil_tutor = []
    for i in pupil_time_intervals:
        for j in tutor_time_intervals:
            intersection_pupil_tutor.append(get_intersection(i, j))
    common_time_intervals = [get_intersection(i, lesson_time_intervals[0]) for i in intersection_pupil_tutor]
    result_intervals = []
    for start, end in common_time_intervals:
        for i in range(start, end):
            if i not in result_intervals:
                result_intervals.append(i)
    common_time_appearance = len(result_intervals)
    return f'Общее время присутствия учителя и ученика на уроке:\n{common_time_appearance}'


if __name__ == '__main__':
    app.run()

