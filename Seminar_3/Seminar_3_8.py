hike = {
    'Aaz': ("спички", "спальник", "дрова", "топор"),
    'Skeeve': ("спальник", "спички", "вода", "еда"),
    'Tananda': ("вода", "спички", "косметика", "топор"),
}

all_things = set()
for things in hike.values():
    #for thing in set(things):
    #  all_things.add(thing)
    all_things.update(things)

print(f'Полный список вещей {all_things}')

unique_things = {}
for master_friend, master_things in hike.items():
    for slave_friends, slave_things in hike.items():
        if master_friend != slave_friends:
            if master_friend not in unique_things:
                unique_things[master_friend] = set(master_things) - set(slave_things)
            else:
                unique_things[master_friend] -= set(slave_things)

print(f'Список уникальных вещей {unique_things}')

double_things = set(all_things)
for things in unique_things.values():
    double_things -= things

print(f'Список дублирующихся вещей {double_things}')

for friend, things in hike.items():
    print(f'у {friend} отсутствуют {double_things - set(things)}')
    print(f'второй вариант: {friend} - {(set(things) ^ double_things) - set(unique_things[friend])}')
