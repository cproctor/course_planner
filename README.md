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
- `sudo pip install django pyaml`
- (enter your password)
- `python manage.py migrate`
- `python manage.py loaddata stanford_gse_daps_lstd.yaml`
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
you created a user during installation.) You will have already loaded definitions of academic
quarters and requirements, but you may need to change these to meet your needs. Once you
have done so, you can start adding courses you have taken. As you add and edit 
courses, you will see your requirements and unit caps updating. Once you find some 
combination that satisfies all your requirements, you've got a graduate study plan!
