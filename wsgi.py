import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate

from App.models import User
from App.models import Administrator
from App.models import AssignStaff
from App.models import CreateCourses
from App.models import CreateStaff
from App.models import ViewCourseStaff
from App.models import Lecture
from App.models import TeachingAssistant
from App.models import Tutor
from App.models import AdminAssignment
from App.models import AdminCreateStaff
from App.models import AdminViewCourseStaff


from App.main import create_app
from App.controllers import ( 
    create_adminAssignment,
    create_adminCreateCourses,
    create_adminCreateStaff,
    create_admin,
    adminViewCourseStaff,
    assignStaffMember,
    create_newCourse,
    get_all_courses_json,
    create_staff,
    get_all_staff_json,
    initialize,
    initializeAdmin,
    initializeNewCourse,
    initializeNewStaff,
    initializeLecturer,
    initializeTA,
    initializeTutor,
    initializeAdminAssignment,
    initializeAdminCreateStaff,
    initializeView,
    initializeAdminCreateCourses,
    create_lecturer,
    create_TA,
    create_tutor,
    create_View,
    get_staff_by_ID,
    get_user,
    get_all_staff,
    get_all_staffMembers_json,
    createCourse
 )

from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

'''
Generic Commands
'''

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
    create_newCourse("COMP 1600", "Computing Concepts")
    create_newCourse("COMP 2611", "Data Structures")
    create_newCourse("COMP 1601", "Programming I")
    create_newCourse("COMP 1602", "Programming II")
    create_newCourse("COMP 1602", "Programming III")


    create_staff("201", "Quin", "Uno", "lecture")
    create_staff("202", "Will", "Ian", "lecture")
    create_staff("303", "Elle", "Oly", "teacher assistant")
    create_staff("304", "Rose", "Poppy", "teacher assistant")
    create_staff("505", "Tanner", "Anne", "tutor")
    create_staff("506", "Yanny", "Sam", "tutor")

    
    create_lecturer("101", "COMP 1600")
    create_lecturer("102", "COMP 1602")

    create_TA("601", "COMP 1600")
    create_TA("602", "COMP 1602")

    create_tutor("801", "COMP 1600")
    create_tutor("802", "COMP 1602")
    

    assignStaffMember("1", "201", "COMP 1600", "lecture", "FST 113")
    assignStaffMember("2", "202", "COMP 1602", "lecture", "FST 114")
    assignStaffMember("3", "303", "COMP 1600", "teacher assistant", "C1")
    assignStaffMember("4", "304", "COMP 1602", "teacher assistant", "JFK")
    assignStaffMember("5", "505", "COMP 1600", "tutor", "C2")
    assignStaffMember("6", "506", "COMP 1602", "tutor", "C3")
'''




'''
CreateCourses Commands
'''
createCourses_cli = AppGroup('CreateCourses', help='CreateCourses object commands')

#flask createCourses createCourse
@createCourses_cli.command("createCourse", help="Used to create courses")
@click.argument("courseID", default="COMP 3613")
@click.argument("courseName", default="Software Engineering")
def create_newCourse_command(courseid, coursename):
    newCourse = create_newCourse(courseid, coursename)
    print(newCourse)

app.cli.add_command(createCourses_cli)


#flask createCourses initializeNewCourse
@createCourses_cli.command("initializeNewCourse", help="Initilizes a course")
#@click.option("--courseID", default="1234", help = "adminID")
#@click.option("--courseName", default="Math", help = "courseName")
def initializeNewCourse_command():
    initializeNewCourse()
    db.drop_all()
    db.create_all()
    #create_newCourse('456', 'courseName')

#flask createCourses createNewCourse
@createCourses_cli.command("createNewCourse", help="create a course")
@click.option("--courseID", default="1234", help = "courseID")
@click.option("--courseName", default="Math", help = "courseName")
def create_newCourse_command(courseid, coursename):
    create_newCourse(courseid, coursename)
    print(f'{courseid}   {coursename} created!') #testing


##############################################################################################################################


'''
ViewCourseStaff Commands
'''
viewCourseStaff_cli = AppGroup('ViewCourseStaff', help='ViewCourseStaff object commands')

#flask viewCourseStaff displayAllCourseStaff 
@viewCourseStaff_cli.command("displayAllCourseStaff", help="display course staff in the database")
def get_all_staffMembers_json_command():
    get_all_staffMembers_json()
    print(get_all_staffMembers_json())

app.cli.add_command(viewCourseStaff_cli)


##############################################################################################################################


'''
Administrator
'''
administrator_cli = AppGroup('Administrator', help='Administrator object commands')

#flask administrator viewCourseStaff
@administrator_cli.command("viewCourseStaff", help="Allows admin to view course staff")
@click.argument("courseName", default="Software Engineering")
@click.argument("courseID", default="COMP 3613")
def createCourse_command(coursename, courseid):
    newCourse = createCourse(coursename, courseid)
    print(newCourse)


#flask administrator initializeAdmin
@administrator_cli.command("initializeAdmin", help="initialize administrator")
@click.option("--adminID", default="123", help = "adminID")
@click.option("--staffID", default="654", help = "staffID")
@click.option("--fName", default="Sam", help = "fName")
@click.option("--lName", default="Apple", help = "lName")
def initializeAdmin_command(adminid, staffid, fname, lname):
    initializeAdmin()
    db.drop_all()
    db.create_all()
    #create_admin(adminid, staffid, fname, lname)
    #print(f'{adminid}   {staffid}   {fname} {lname} created!')


#flask administrator create_admin 
@administrator_cli.command("create_admin", help="Creates an administrator")
@click.option("--adminID", default="1", help = "adminID")
@click.option("--staffID", default="2", help = "staffID")
@click.option("--fName", default="First", help = "fName")
@click.option("--lName", default="Last", help = "lName")
def create_admin_command(adminid, staffid, fname, lname):
    create_admin(adminid, staffid, fname, lname)
    print(f'{adminid}   {staffid}   {fname} {lname} created!')

#flask administrator createCourse
@administrator_cli.command("createCourse", help="Allows admin to create courses")
@click.option("--courseName", default="Software Engineering ", help = "courseName")
@click.option("--courseID", default="COMP 3613", help = "courseID")
def createCourse_command(coursename, courseid):
    createCourse(coursename, courseid)

    print(f'{coursename}   {courseid} created!')



app.cli.add_command(administrator_cli)


##############################################################################################################################


assignStaff_cli = AppGroup('AssignStaff', help='assignStaff object commands')

#flask assignStaff assignStaff
@assignStaff_cli.command("assignStaff", help="Used to assignStaff")


@click.argument("courseID", default="COMP 3613")
@click.argument("courseName", default="Software Engineering")
def create_newCourse_command(courseid, coursename):
    newCourse = create_newCourse(courseid, coursename)
    print(newCourse)

app.cli.add_command(createCourses_cli)


##############################################################################################################################

#createCourses

createCourses_cli = AppGroup('createCourses', help='CreateCourses object commands')

#flask createCourses initializeNewCourse
@createCourses_cli.command("initializeNewCourse", help="Initilizes a course")
#@click.option("--courseID", default="1234", help = "adminID")
#@click.option("--courseName", default="Math", help = "courseName")
def initializeNewCourse_command():
    initializeNewCourse()
    db.drop_all()
    db.create_all()
    #create_newCourse('456', 'courseName')

#flask createCourses createNewCourse
@createCourses_cli.command("createNewCourse", help="create a course")
@click.option("--courseID", default="1234", help = "courseID")
@click.option("--courseName", default="Math", help = "courseName")
def create_newCourse_command(courseid, coursename):
    create_newCourse(courseid, coursename)
    print(f'{courseid}   {coursename} created!') #testing


'''
def get_all_courses_json():
    c = CreateCourses.query.all()
    if not c:
        return []
    c = [courses.get_json() for courses in c]
    return c
'''

app.cli.add_command(createCourses_cli)




#Administrator Commands

#flask administrator initializeAdmin
#example to override the default "flask administrator initializeAdmin --adminID 456 --staffID 789 --fName John --lName Doe"


'''
#createCourses

createCourses_cli = AppGroup('createCourses', help='CreateCourses object commands')

#flask createCourses initializeNewCourse
@createCourses_cli.command("initializeNewCourse", help="Initilizes a course")
#@click.option("--courseID", default="1234", help = "adminID")
#@click.option("--courseName", default="Math", help = "courseName")
def initializeNewCourse_command():
    initializeNewCourse()
    db.drop_all()
    db.create_all()
    #create_newCourse('456', 'courseName')

#flask createCourses createNewCourse
@createCourses_cli.command("createNewCourse", help="create a course")
@click.option("--courseID", default="1234", help = "courseID")
@click.option("--courseName", default="Math", help = "courseName")
def create_newCourse_command(courseid, coursename):
    create_newCourse(courseid, coursename)
    print(f'{courseid}   {coursename} created!') #testing



def get_all_courses_json():
    c = CreateCourses.query.all()
    if not c:
        return []
    c = [courses.get_json() for courses in c]
    return c

app.cli.add_command(createCourses_cli)
'''

'''
#CreateStaff

def get_all_staff_json():
    members = CreateStaff.query.all()
    if not members:
        return []
    members = [staff.get_json() for staff in members]
    return members
'''

'''
#viewCourseStaff

def get_all_staffMembers_json():
    staffMembers = ViewCourseStaff.query.all()
    if not staffMembers:
        return []
    staffMembers= [staff.get_json() for staff in staffMembers]
    return staffMembers

##############################################################################################################################


#AssignStaff

administrator_cli = AppGroup('administrator', help='Administrator object commands')

app.cli.add_command(administrator_cli) # add the group to the cli
#flask assignStaff
def assignStaffMember(assignmentID, staffID, courseID, position, courseLocation):
    assignment = AssignStaff(assignmentID = assignmentID, staffID = staffID, courseID = courseID, position = position, courseLocation = courseLocation)
    db.session.add(assignment)
    db.session.commit()
    return assignment




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

'''

'''
# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
#Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)




'''
'''
#AdminAssignment

def create_adminAssignment(adminAssignmentID, adminID, assignmentID):
    newAdminAssign = AdminAssignment(adminAssignmentID = adminAssignmentID, adminID = adminID, assignmentID = assignmentID)
    db.session.add(newAdminAssign)
    db.session.commit()
    return newAdminAssign
'''

'''


'''



'''
# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
#Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
'''