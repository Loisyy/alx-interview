#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.'''
    total_boxes = len(boxes)
    available_keys = set()
    unlocked_boxes = []
    current_box = 0

    while current_box < total_boxes:
        previous_box = current_box
        unlocked_boxes.append(current_box)
        available_keys.update(boxes[current_box])
        
        for key in available_keys:
            if key != 0 and key < total_boxes and key not in unlocked_boxes:
                current_box = key
                break
        
        if previous_box != current_box:
            continue
        else:
            break

    for box in range(total_boxes):
        if box not in unlocked_boxes and box != 0:
            return False
            
    return True
