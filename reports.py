import sqlite3


class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    # Using lambda (anonymous Python function) to create the results--don't need create_student anymore...
    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Name
            from Student s
            join Cohort c on s.Cohort_Id = c.Id
            order by s.Cohort_Id
            """)

            all_students = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            # for student in all_students:
            #     print(
            #         f'{student.first_name} {student.last_name} is in {student.cohort}')

            for student in all_students:
                print(student)


reports = StudentExerciseReports()
reports.all_students()

# ------------------------
# Instructions-->Display all cohorts.
print("----------------------")
print("All Cohorts:")


class Cohort():

    def __init__(self, cohort):
        self.cohort = cohort

    def __repr__(self):
        return f'{self.cohort}'


class StudentCohortReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    def all_cohorts(self):
        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Cohort(row[0])

            db_cursor = conn.cursor()

            db_cursor.execute("""SELECT c.Name
            FROM Cohort c""")

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)


cohorts = StudentCohortReports()
cohorts.all_cohorts()
print("----------------------")
# ------------------------
# Instructions-->Display all exercises.
print("All Exercises:")


class Exercise():

    def __init__(self, exercise):
        self.exercise = exercise

    def __repr__(self):
        return f'{self.exercise}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    def all_exercises(self):
        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row: Exercise(row[0])

            db_cursor = conn.cursor()

            db_cursor.execute("""SELECT e.Name_of_Exercise
            FROM Exercise e""")

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)


exercises = StudentExerciseReports()
exercises.all_exercises()
# ------------------------
# Instructions-->Display only exercises in Python
print("----------------------")
print("Only Python Exercises:")


class Python_Exercise():

    def __init__(self, exercise):
        self.exercise = exercise

    def __repr__(self):
        return f('{self.exercise}')


class StudentPythonExerciseReports:

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    def all_python_exercises(self):
        """Retrieve only python exercises"""

        with sqlite3.connect(self.db_path) as conn:

            conn.row_factory = lambda cursor, row:  Exercise(row[0])

            db_cursor = conn.cursor()

            db_cursor.execute("""SELECT e.Name_of_Exercise
            FROM Exercise e
            WHERE Coding_Language = "Python"
            """)

            all_python_exercises = db_cursor.fetchall()

            for each_exercise in all_python_exercises:
                print(each_exercise)


python_exercises = StudentPythonExerciseReports()
python_exercises.all_python_exercises()

# ------------------------
# Instructions-->Output a report in your terminal that lists all students and the exerices each is assigned. Use a dictionary to track each exercise. Remember that the key should be the exercise id and the value should be the entire exercise object
print("----------------------")
print("Shows which students are working on each exercise:")


class Python_Exercise():

    def __init__(self, exercise):
        self.exercise = exercise

    def __repr__(self):
        return f('{self.exercise}')


class StudentPythonExerciseReports:

    def __init__(self):
        self.db_path = "/Users/Owner/workspace/practices/joypr0912sqlcreatestudentdb/studentexercises.db"

    def all_python_exercises(self):
        """Retrieve only python exercises"""

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:

            # conn.row_factory = lambda cursor, row:  Exercise(row[0])

            db_cursor = conn.cursor()

            db_cursor.execute("""SELECT e.id,
            e.Name_of_Exercise,
            s.Id AS StudentId,
            s.First_Name,
            s.Last_Name
            from Exercise e
            join Student_Exercise se on se.Exercise_Id = e.Id
            join Student s on s.Id = se.Student_Id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)

                for student in students:
                    print(f'\t* {student}')

python_exercises = StudentPythonExerciseReports()
python_exercises.all_python_exercises()
