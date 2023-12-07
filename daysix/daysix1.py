from collections import namedtuple


Race = namedtuple('Race','time, distance')
races = [Race(59, 543), Race(68, 1020), Race(82, 1664), Race(74, 1022)]
test_races = [Race(7, 9), Race(15, 40), Race(30, 200)]
second_race = [Race(59688274, 543102016641022)]
total_possible_wins = 1

for race in second_race:
    count = 0
    wins = 0
    while count <= race.time:
        run = (race.time - count) * (1 * count)
        # print(f'Current Race Time is {race.time} and distance of {race.distance}')
        count += 1
        if run > race.distance:
            # print(f'WIN -- Elapsed run time {race.time - count} won the race with a distance of {run}')
            wins += 1
        # else:
            # print(f'LOSS -- Count {count-1} won the race with a distance of {run}')
    # print(f'wins for {race.time} are {wins}.')
    total_possible_wins *= wins

print(f'Total wins are: {total_possible_wins}.')
