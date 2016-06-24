from timetable.timetable import Timetable


def test_create_timetable(f_session):
    user_id = 123
    semester = '2014-03-02'
    subject_id = 111
    timetable = Timetable(user_id=user_id,
                          semester=semester,
                          subject_id=subject_id)
    f_session.add(timetable)
    f_session.commit()
    find_timetable = f_session.query(Timetable) \
                              .filter(Timetable.user_id == user_id) \
                              .first()
    assert find_timetable
