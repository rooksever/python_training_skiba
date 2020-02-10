from model.group import Group

def test_edit_first_group(app, db, check_ui):
    if app.group.count_groups() == 0:
        app.group.create(Group(name = "test", header="test", footer="test"))
    old_groups = db.get_group_list()
    group = Group(name="qqqqqqqqqq", header="aaaaaaaaaa", footer="zzzzzzzz")
    app.group.edit_first_group(group)
    group.id = old_groups[0].id
    assert len(old_groups) == app.group.count_groups()
    new_groups = db.get_group_list()
    old_groups[0] = group
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


