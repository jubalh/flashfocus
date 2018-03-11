from pytest import approx

from flashfocus.Xutil import *
from test.helpers import change_focus

def get_opacity(window_id):
    cookie = request_opacity(window_id)
    opacity = unpack_cookie(cookie)
    return opacity


def test_get_set_opacity(window):
    assert get_opacity(window) == 1
    set_opacity(window, 0.5)
    assert get_opacity(window) == approx(0.5, 0.00001)


def test_get_focused_window(window):
    change_focus(window)
    assert get_focused_window() == window