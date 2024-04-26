import re




def extract_from_search(ytprompt):
  pattern= r'play\s+(.*?)\s+on\s+youtube'
  match= re.search(pattern, ytprompt, re.IGNORECASE)
  return match.group(1) if match else None