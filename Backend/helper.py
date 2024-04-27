import re

# for yt serach
def extract_from_search(ytprompt):
  pattern= r'play\s+(.*?)\s+on\s+youtube'
  match= re.search(pattern, ytprompt, re.IGNORECASE)
  return match.group(1) if match else None

# for whatsapp search
def remove_words(input_phrase,extra_words):
  words=input_phrase.split()

  exact_phrase=[word for word in words if word.lower() not in extra_words]
  result_phrase=' '.join(exact_phrase)
  return result_phrase

