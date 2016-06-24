from timetable.subject import Subject


def test_create_subject(f_session):
    name = 'DB'
    category_id = 1111
    subject = Subject(name=name, category_id=category_id)
    f_session.add(subject)
    f_session.commit()
    find_subject = f_session.query(Subject) \
                            .filter(Subject.name == name) \
                            .first()
    assert find_subject
