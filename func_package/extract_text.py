### 長い文章から一部分を抽出
## 1/2
# 前半1/2を抽出
def extract_former_half(paragraph):
    """
    Extract the first half part of the passed paragraph.
    Return the strings as the extracted part.
    """
    end_index = len(paragraph)//2
    extracted_text = paragraph[:end_index]
    return extracted_text


# 後半1/2を抽出
def extract_latter_half(paragraph):
    """
    Extract the last of a thirds part of the passed paragraph.
    Return the strings as the extracted part.
    """
    start_index = len(paragraph)//2
    end_index = len(paragraph)
    extracted_text = paragraph[start_index:end_index]
    return extracted_text


## 1/3
# 文章から最初の1/3のみ抽出
def extract_first_thirds(paragraph):
    """
    Extract the 1/3 first part of the passed paragraph.
    Return the strings as the extracted part.
    """

    end_index = len(paragraph)//3
    extracted_text = paragraph[:end_index]
    return extracted_text


# 文章から中央部分1/3のみ抽出
def extract_middle_thirds(paragraph):
    """
    Extract the 1/3 middle part of the passed paragraph.
    Return the strings as the extracted part.
    """

    start_index = len(paragraph)//3
    end_index = len(paragraph)//3*2
    extracted_text = paragraph[start_index:end_index]
    return extracted_text


# 文章から最後の1/3のみ抽出
def extract_last_thirds(paragraph):
    """
    Extract the 1/3 last part of the passed paragraph.
    Return the strings as the extracted part.
    """
    start_index = len(paragraph)//3*2
    end_index = len(paragraph)
    extracted_text = paragraph[start_index:end_index]
    return extracted_text

