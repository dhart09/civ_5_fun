import random

all_colors = ['[COLOR_ADVISOR_HIGHLIGHT_TEXT]',
 '[COLOR_FONT_GREEN]', 
 '[COLOR_RESEARCH_STORED]', 
 '[COLOR_ALT_HIGHLIGHT_TEXT]', 
 '[COLOR_FONT_RED]', 
 '[COLOR_SELECTED_TEXT]', 
 '[COLOR_BLACK]', 
 '[COLOR_GREAT_PEOPLE_STORED]', 
 '[COLOR_TECH_TEXT]', 
 '[COLOR_BLUE]', 
 '[COLOR_GREEN]', 
 '[COLOR_UNIT_TEXT]', 
 '[COLOR_BROWN_TEXT]', 
 '[COLOR_GREY]', 
 '[COLOR_WARNING_TEXT]', 
 '[COLOR_BUILDING_TEXT]', 
 '[COLOR_HIGHLIGHT_TEXT]', 
 '[COLOR_WATER_TEXT]', 
 '[COLOR_CITY_BLUE]', 
 '[COLOR_LIGHT_GREY]', 
 '[COLOR_WHITE]', 
 '[COLOR_CITY_BROWN]', 
 '[COLOR_MAGENTA]', 
 '[COLOR_XP_BLUE]', 
 '[COLOR_CITY_GREEN]', 
 '[COLOR_MENU_BLUE]', 
 '[COLOR_YELLOW]', 
 '[COLOR_CITY_GREY]', 
 '[COLOR_NEGATIVE_TEXT]', 
 '[COLOR_YIELD_FOOD]', 
 '[COLOR_CULTURE_STORED]', 
 '[COLOR_POPUP_TEXT]', 
 '[COLOR_YIELD_GOLD]', 
 '[COLOR_CYAN]', 
 '[COLOR_POSITIVE_TEXT]', 
 '[COLOR_YIELD_PRODUCTION]', 
 '[COLOR_DARK_GREY]', 
 '[COLOR_PROJECT_TEXT]']



class CivVTextColorEr:
     def __init__(self, color_list=None):
          if color_list is None:
              color_list = all_colors
          self.color_list = color_list
 
     def random_colors(self, some_string):
          some_string = input("Input text to colour:\n")
          print(random.choice(self.color_list) + some_string + "[/COLOR]")
