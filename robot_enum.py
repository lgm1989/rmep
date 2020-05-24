from enum import IntEnum


class switch_enum():
    on = "on"
    off = "off"


class mode_enum(IntEnum):
    free = 0
    gimbal_lead = 1
    chassis_lead = 2


class chassis_push_attr_enum(IntEnum):
    position = 0
    attitude = 1
    status = 2


class gimbal_push_attr_enum():
    attitude = "attitude"


class armor_event_attr_enum():
    hit = "hit"


class sound_event_attr_enum():
    applause = "applause"


class led_comp_enum():
    all = "all"
    top_all = "top_all"
    top_right = "top_right"
    top_left = "top_left"
    bottom_all = "bottom_all"
    bottom_front = "bottom_front"
    bottom_back = "bottom_back"
    bottom_left = "bottom_left"
    bottom_right = "bottom_right"


class led_effect_enum():
    solid = "solid"
    off = "off"
    pulse = "pulse"
    blink = "blink"
    scrolling = "scrolling"


class line_color_enum(IntEnum):
    red = 0
    blue = 1
    green = 2


class marker_color_enum(IntEnum):
    red = 0
    blue = 1


class ai_push_attr_enum():
    person = 0
    gesture = 1
    line = 2
    marker = 3
    robot = 4


class ai_pose_id_enum(IntEnum):
    e4 = 4
    e5 = 5
    e6 = 6


class ai_marker_id_enum():
    stop = 1
    turn_left = 4
    turn_right = 5
    go_ahead = 6
    red_heard = 8
    one = 10
    two = 12
    three = 15


class camera_ev_enum():
    default = "default"
    small = "small"
    medium = "medium"
    large = "large"
