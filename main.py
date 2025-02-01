from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    match edit_type:

        case EditType.NEWLINE:
            value = document.split("\n")
            value.insert(edit['line_number']+1, '')
            return "\n".join(value)
        case EditType.INSERT:
            value = document.split("\n")
            value.insert(edit['line_number'], edit["insert_text"])
            #value.pop()
            return "\n".join(value)
        case EditType.DELETE:
            value = document.split("\n")
            value[edit["line_number"]] = value[edit["line_number"]
                                               ][:edit["start"]] + value[edit["line_number"]][edit["end"]:]  # +
            return "\n".join(value)
        case EditType.SUBSTITUTE:
            value = document.split("\n")
            value[edit["line_number"]] = value[edit["line_number"]][:edit["start"]] + \
                edit["insert_text"] + \
                value[edit["line_number"]][edit["end"]:]  # +
            return "\n".join(value)

        case _:
            raise Exception("Unknown edit type")
