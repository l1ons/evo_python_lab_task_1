def direction(facing, turn):
    direction_list = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'] # Имеем список направлений

    steps = int(turn / 45) # Вичисляем количесвтво шагов
    num_facing = direction_list.index(facing) # Определяем положение исходного направления в списке
    num_end = int((num_facing + steps) % len(direction_list)) # Выичсляем итоговое положение направления в списке

    return direction_list[num_end]