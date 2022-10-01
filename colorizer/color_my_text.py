import random

WEIRD_COLOR_DICT = {
    "advisor_highlight": '[COLOR_ADVISOR_HIGHLIGHT_TEXT]',
    "alt_highlight": '[COLOR_ALT_HIGHLIGHT_TEXT]',
    "building": '[COLOR_BUILDING_TEXT]',
    "city_blue": '[COLOR_CITY_BLUE]',
    "city_brown": '[COLOR_CITY_BROWN]',
    "city_green": '[COLOR_CITY_GREEN]',
    "city_grey": '[COLOR_CITY_GREY]',
    "culture_stored": '[COLOR_CULTURE_STORED]',
    "font_green": '[COLOR_FONT_GREEN]',
    "great_people": '[COLOR_GREAT_PEOPLE_STORED]',
    "highlight": '[COLOR_HIGHLIGHT_TEXT]',
    "menu_blue": '[COLOR_MENU_BLUE]',
    "negative": '[COLOR_NEGATIVE_TEXT]',
    "positive": '[COLOR_POSITIVE_TEXT]',
    "popup_text": '[COLOR_POPUP_TEXT]',
    "production": '[COLOR_YIELD_PRODUCTION]',
    "project_text": '[COLOR_PROJECT_TEXT]',
    "research": '[COLOR_RESEARCH_STORED]',
    "selected_text": '[COLOR_SELECTED_TEXT]',
    "tech": '[COLOR_TECH_TEXT]',
    "unit": '[COLOR_UNIT_TEXT]',
    "warning": '[COLOR_WARNING_TEXT]',
    "water": '[COLOR_WATER_TEXT]',
    "xp_blue": '[COLOR_XP_BLUE]',
    "yield_food": '[COLOR_YIELD_FOOD]',
    "yield_gold": '[COLOR_YIELD_GOLD]',

}

NORMAL_COLOR_DICT = {
    "black": '[COLOR_BLACK]',
    "blue": '[COLOR_BLUE]',
    "brown": '[COLOR_BROWN_TEXT]',
    "cyan": '[COLOR_CYAN]',
    "green": '[COLOR_GREEN]',
    "grey": '[COLOR_GREY]',
    "light_grey": '[COLOR_LIGHT_GREY]',
    "dark_grey": '[COLOR_DARK_GREY]',
    "red": '[COLOR_FONT_RED]',
    "magenta": '[COLOR_MAGENTA]',
    "yellow": '[COLOR_YELLOW]',
    "white": '[COLOR_WHITE]',
}

COLOR_LIST = NORMAL_COLOR_DICT.update(WEIRD_COLOR_DICT)

class CivVTextColorEr:
    def __init__(self, color_list=None):
        if color_list is None:
            color_list = COLOR_LIST
        self.color_list = color_list

    def random_colors(self, some_string):
        some_string = input("Input text to colour:\n")
        print(random.choice(self.color_list) + some_string + "[/COLOR]")
