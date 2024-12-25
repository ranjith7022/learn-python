from functools import reduce


def paginator(page_length):
    def paginate(document):
        words = document.split()

        def add_word_to_pages(pages, word):
            if not pages:
                pages = [word]
                return pages
            current_page = pages[-1]
            if(len(current_page)+len(word)+1 > page_length):
                pages.append(word)
            else:
                current_page +=" "+ word
                pages[-1] = current_page
            return pages

        return reduce(add_word_to_pages, words, [])

    return paginate
