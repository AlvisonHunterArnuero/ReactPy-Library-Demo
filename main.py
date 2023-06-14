from reactpy import component, html, run


@component
def DataList(items, filter_by_level=None, sort_by_level=False):
    if filter_by_level is not None:
        items = [i for i in items if i["level"] <= filter_by_level]
    if sort_by_level:
        items = sorted(items, key=lambda i: i["level"])
    list_item_elements = [html.li(i["name"], " | ", i["level"]) for i in items]
    return html.ul(list_item_elements)


@component
def TodoList():
    language_lst = [
        {"name": "Python", "level": 0},
        {"name": "JavaScript", "level": 0},
        {"name": "TypeScript", "level": 2},
        {"name": "Golang", "level": 1},
        {"name": "Visual Basic For Applications", "level": 2},
        {"name": "Fox Pro", "level": 2},
        {"name": "C Sharp", "level": 1},
        {"name": "C plus plus", "level": 1},
    ]
    return html.section(
        html.h1("Known Languages List"),
        DataList(language_lst, filter_by_level=2, sort_by_level=True),
    )


run(TodoList)