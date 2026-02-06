# Compute transit times, periods, epochs
def next_transit(mid_time, period_days, start_time):
    n = int((start_time - mid_time) / period_days)
    return mid_time + (n + 1) * period_days
