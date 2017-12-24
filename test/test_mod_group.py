from model.group import Group
import random

def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name=" "))
    old_groups = db.get_group_list()
    group_modify = random.choice(old_groups)
    group = Group(name="modified", header="qwerty1")
    group.id = group_modify.id
    app.group.modify_group_by_id(group_modify.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group_modify)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_modify_first_group_header(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="CCC"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
# def test_modify_first_group_footer(app):
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(footer="DDD"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
