def get_grade_test(score):
    if 2 <= score < 3:
        return "Fail"
    if 3 <= score < 3.5:
        return "Poor"
    if 3.5 <= score < 4.5:
        return "Good"
    if 4.5 <= score < 5.5:
        return "Very Good"
    if 5.5 <= score <= 6:
        return "Excellent"


score = float(input())
print(get_grade_test(score))
