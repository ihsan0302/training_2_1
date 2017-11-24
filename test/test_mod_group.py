from model.group import Group

def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="BBB"))

def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="CCC"))

def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="DDD"))
