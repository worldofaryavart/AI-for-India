from extract_url import get_url
from text_extraction import get_text
from text_summarisation import summarise

def generate(prompt:str):

    search_results = get_url(prompt)

    text = ""

    for result in search_results:
        text += get_text(result)

    summarised_text = summarise(text)

    final_answer = f"Here's what I found: \n{summarised_text}"

    return final_answer
