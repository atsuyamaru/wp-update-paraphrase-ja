def translate_2en(translator, paragraph):
    """
    Execute Translation. Return EN text extracted from the object as a string.
    Pass the translator object as the 1st argument.
    Pass the paragraph as the 2nd argument.
    """
    response = translator.translate_text(paragraph, source_lang="JA", target_lang="EN-US")
    return response.text


def translate_2ja(translator, paragraph):
    """
    Execute Translation. Return JA text extracted from the object as a string.
    Pass the translator object as the 1st argument.
    Pass the paragraph as the 2nd argument.
    """
    response = translator.translate_text(paragraph, target_lang="JA")
    return response.text