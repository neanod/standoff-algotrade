import pyautogui as pg


if __name__ == "__main__":
    raise ValueError(f"{__file__} is a dependency and cannot be started directly")


def click(x: int, y: int, /, *, return_after_click: bool = False) -> None:
    """
    Clicks to given position.
    Args:
        x: horisontal position left to right
        y: vertical position up to down
        return_after_click: returns cursor to prevous position
    """
    old_x: int
    old_y: int
    if return_after_click:
        old_x, old_y = pg.position()
    pg.click(x=x, y=y)
    if not return_after_click:
        return
    pg.dragTo(old_x, old_y)