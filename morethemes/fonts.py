import os
from matplotlib import font_manager

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))


def set_family_from_file(file):
    font_path = os.path.join(PACKAGE_DIR, "fonts", file)
    if not os.path.isfile(font_path):
        raise ValueError(f"Font file not found: {font_path}")
    font_prop = font_manager.FontProperties(fname=font_path)
    font_manager.fontManager.addfont(font_path)
    return font_prop.get_name()
