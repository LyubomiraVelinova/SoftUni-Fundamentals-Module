n = int(input())

list_of_positives = []
list_of_negatives = []

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        list_of_positives.append(current_number)
    else:
        list_of_negatives.append(current_number)
print(list_of_positives)
print(list_of_negatives)
print(f"Count of positives: {len(list_of_positives)}. Sum of negatives: {sum(list_of_negatives)}")