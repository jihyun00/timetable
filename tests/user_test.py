from timetable.user import User


def test_create_user(f_session):
    password = 'abc'
    email = 'abc@naver.com'
    user = User(password=password, email=email)
    f_session.add(user)
    f_session.commit()
    find_user = f_session.query(User) \
                         .filter(User.email == email) \
                         .first()
    assert find_user
    assert find_user.password == password
    assert find_user.email == email
