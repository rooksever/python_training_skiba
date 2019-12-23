from model.group import Group

def test_edit_first_group(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name = "test", header="test", footer="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="qqqqqqqqqq", header="aaaaaaaaaa", footer="zzzzzzzz")
    app.group.edit_first_group(group)
    group.id = old_groups[0].id
    assert len(old_groups) == app.group.count_groups()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


