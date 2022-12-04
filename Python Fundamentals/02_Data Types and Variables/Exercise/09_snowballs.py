import math
N_number_snowballs = int(input())

snowball_value = 0
best_snowball_snow = 0
best_snowball_time = 0
best_snowball_quality = 0

for each_snowball in range(N_number_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = math.ceil(snowball_snow / snowball_time) ** snowball_quality
    if current_snowball_value > snowball_value:
        snowball_value = current_snowball_value
        best_snowball_quality = snowball_quality
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time


print(f"{best_snowball_snow} : {best_snowball_time} = {snowball_value} ({best_snowball_quality})")
