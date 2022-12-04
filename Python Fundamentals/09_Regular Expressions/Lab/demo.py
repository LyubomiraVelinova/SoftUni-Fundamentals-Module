# import re
#
# s = """The rain in Spain
# The rain in Spain"""
# search_pattern = r"^The.*Spain$"
# x = re.search(search_pattern, s, re.MULTILINE)
# print(x)

import re

text = "lorem1ipsum2dolor3sit4amet"
print(re.split(r"\d", text))
