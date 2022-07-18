"""
input
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

output
26.50


"""



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

    if query_name in student_marks:
        a = sum(student_marks[query_name])/len(student_marks[query_name])
    print("{:.2f}".format(a))