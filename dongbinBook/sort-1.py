# 성적이 낮은 순서로 학생 출력하기

# 나의 풀이
n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key= lambda x: x[1])

print(" ".join(map(lambda x: x[0], students)))


# 해설
n = int(input())

array = []
for i in range(n):
    input_data = input().split()

    array.append(input_data[0], int(input_data[1]))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')