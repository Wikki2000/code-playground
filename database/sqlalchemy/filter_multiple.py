from sqlalchemy import or_

user = session.query(User).filter(or_(
    User.email == login_input, User.username == login_input
)).first()

