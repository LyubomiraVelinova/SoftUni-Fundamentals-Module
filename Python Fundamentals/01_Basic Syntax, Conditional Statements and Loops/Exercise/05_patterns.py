GROW = 1
SHRINK = -1

desired_size = int(input())
direction = GROW
current_size = 0

while current_size <= desired_size and (current_size > 0 or direction == GROW):
    if desired_size == current_size:
        direction = SHRINK
    current_size += direction
    print("*" * current_size)
