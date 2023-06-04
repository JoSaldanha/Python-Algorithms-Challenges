def study_schedule(permanence_period, target_time):
    count = 0

    if not isinstance(target_time, int):
        return None
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        elif period[0] <= target_time <= period[1]:
            count += 1
    return count
    raise NotImplementedError
