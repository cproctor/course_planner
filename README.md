# Course Planner

## What it is

Course Planner is a tool for planning graduate school coursework over several years 
so that it satisfies many different requirements--I found that a spreadsheet was
not quite sufficient for seeing the effect of changes. It doesn't look nice and
it's not particularly user-friendly, but I found it very helpful in thinking through
my next several years of coursework.

## Installation

Works on OS X, probably Linux. Maybe not Windows. From Terminal:
 
- Navigate to a directory where you want to install Course Planner
- `git clone https://github.com/cproctor/course_planner.git`
- `cd course_planner`
- `sudo pip install django`
- (enter your password)
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

Now you should be able to open a web browser and navigate to http://localhost:8000.

## Usage

There are two primary views: Calendar and Requirements. Calendar shows your course plan 
broken down by quarter, in separate strands by the requirements the courses satisfy. 
Requirements lists each requirement and the courses you have scheduled to satisfy the 
requirement. As you add and change your courseload, the views will update and run checks
to make sure you have met your requirements and stayed within your unit caps. 

Changes are made through the admin interface, which requires you to log in. (This is why 
you created a user during installation.) I suggest starting by defining the quarters 
you want to plan (ex: 15-16 Autumn; 15-16 Winter; 15-16 Spring; etc.). Then start adding 
courses you have already taken. Then define your program's requirements. For example here 
are my program requirements:

- Stanford: PhD Units (135 of 135 units)
- GSE: Research Methods Core (4 of 4 courses)
- GSE: Proseminar (3 of 3 courses)
- DAPS: Core (4 of 4 courses)
- LSTD: Proseminar (9 of 9 courses)
- LSTD: Research Methodology (2 of 2 courses)
- LSTD: Design Skills (2 of 2 courses)
- LSTD: Learning (2 of 2 courses)
- LSTD: Perspective on Technology (1 of 1 courses)
- LSTD: Topical Content Area (1 of 1 courses)
- CS: Units (Distinct from PhD) (47 of 45 units)
- CS: Foundations (5 of 5 courses)
- CS: Significant Implementation (1 of 1 courses)
- CS: HCI Depth (28 of 27 units)
- CS: Breadth (3 of 3 courses)

Now you are ready to start adding future courses you plan to take. As you add and edit 
courses, you will see your requirements and unit caps updating. Once you find some 
combination that satisfies all your requirements, you've got a graduate study plan!
