from timetable.category import Category


def test_create_category(f_session):
    name = 'Computer Engineering'
    parent_id = 1
    category = Category(name=name, parent_id=parent_id)
    f_session.add(category)
    f_session.commit()
    find_category = f_session.query(Category) \
                             .filter(Category.name == name) \
                             .first()
    assert find_category
