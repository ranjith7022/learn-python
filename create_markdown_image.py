def create_markdown_image(alt_text):
    result = ""
    result += f"![{alt_text}]"
    def add_url(url):
        nonlocal result
        result += f"({url.replace('(','%28').replace(')','%29')}"
        # result += f"({url.replace('(', \"%28\").replace(')', \"%29\")}"

        def add_title(title = ""):
            nonlocal result
            if title == "":
                result += ")"
                return result
            result += f" \"{title}\")"
            return result
        return add_title
    return add_url

# print(create_markdown_image("hi")("hello")("title"))
