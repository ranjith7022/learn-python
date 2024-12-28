from functools import reduce


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


# don't touch above this line


def create_html_table(data_rows):
    row = map(lambda x : accumulate_data_cells(x),data_rows)
    
    row = "".join(map(lambda x : tag_row(x),row))
    
        
    def create_table_headers(headers):
        head = map(lambda x : accumulate_headers(x),headers)
        head = "".join(map(lambda x : tag_header(x),headers))
        head = tag_row(head)
        head = tag_table(head + row)
        return head
        
        
       

    return create_table_headers
