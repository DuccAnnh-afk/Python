import re

def parse_bai(text):
    pattern = r'Bài\s*(\d+):\s*(.*?)(?=Bài\s*\d+:|$)'
    return re.findall(pattern, text, re.DOTALL)