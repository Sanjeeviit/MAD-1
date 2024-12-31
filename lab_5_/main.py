from app import db, Course, app    
with app.app_context():
    courses = [
        Course(course_id=1,course_code="CSE01", course_name= "MAD1", course_description="Mod app Dev"),
        Course(course_id=2,course_code="CSE02", course_name= "DBMS", course_description="Data base Management"),
        Course(course_id=3,course_code="CSE03", course_name= "PDSA", course_description="Python Data"),
        Course(course_id=4,course_code="BSE11", course_name= "BDM", course_description="Business dev")
    ]
    
    db.session.add_all(courses)
    db.session.commit()