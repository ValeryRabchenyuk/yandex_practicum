"""Ya.Contest try ID: 115902324."""
from typing import List


def robot_delivery(robot_weight: List[int], limit: int) -> int:
    """Main function."""
    sorted_robot_weight = sorted(robot_weight)
    count_platform = 0
    left = 0
    right = len(sorted_robot_weight) - 1
    while left <= right:
        if (left != right and
            sorted_robot_weight[left] + sorted_robot_weight[right] <= limit):
            left += 1
        right -= 1
        count_platform += 1
    return count_platform


if __name__ == '__main__':
    robot_weight = list(map(int, input().split()))
    limit = int(input())
    print(robot_delivery(robot_weight, limit))
