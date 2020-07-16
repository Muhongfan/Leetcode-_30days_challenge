"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.



Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
"""


def angleClock(self, hour: int, minutes: int) -> float:
    minute_unit = 360 / 60
    hour_unit = 360 / 12
    fine_tune_hour_unit = (360 / 12) / 60
    # calculate which angle the minute is
    minute_angle = minute_unit * minutes
    # calculate which angle the hour is
    hour_angle = hour_unit * hour
    if hour_angle == 360:
        hour_angle = 0
    hour_angle += fine_tune_hour_unit * minutes
    # find out both angles between them
    angle_a = hour_angle - minute_angle
    if angle_a < 0:
        angle_a = 360 + angle_a
    angle_b = minute_angle - hour_angle
    if angle_b < 0:
        angle_b = 360 + angle_b
    # take the minimum as the answer
    return min(angle_a, angle_b)

#demo solu
def angleClock(self, hour, minutes):
    minute_angle = (minutes) * 6
    hour_offset = (hour % 12) * 30
    hour_angle = hour_offset + (minutes / 60) * (360 / 12)
    delta = abs(minute_angle - hour_angle)
    if delta > 180:
        delta = 360 - delta
    return delta
