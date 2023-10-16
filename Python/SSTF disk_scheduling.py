import numpy as np

def sstf_disk_scheduling(requests, start_position):
    total_head_movement = 0
    current_position = start_position
    sorted_requests = sorted(requests)

    while sorted_requests:
        # Find the closest request in terms of seek time
        closest_request = min(sorted_requests, key=lambda req: abs(req - current_position))
        total_head_movement += abs(current_position - closest_request)
        current_position = closest_request
        sorted_requests.remove(current_position)

    return total_head_movement

# Example usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
start_position = 53

total_movement = sstf_disk_scheduling(requests, start_position)
print(f"Total head movement: {total_movement} cylinders")
