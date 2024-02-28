# 1 - Masala
class Student:

    def __init__(self, full_name, id, course, birth_date, phone):
        self.full_name = full_name
        self.student_id = id
        self.course = course
        self.birth_date = birth_date
        self.phone = phone

    def __str__(self):
        return f"{self.full_name} (ID: {self.student_id}) - Course: {self.course}"

    def __repr__(self):
        return f"Student(full_name={self.full_name}, student_id={self.student_id}, course={self.course}, " \
               f"birth_date={self.birth_date}, phone={self.phone})"

    def __bool__(self):
        birth_year = int(self.birth_date[-4:])
        return birth_year > 2010


toxir_toxirov = Student("Toxir Toxirov", 1245, "Python", "01.08.2007", "+998991234567")
toxir_sobirov = Student("Toxir Sobirov", 3644, "Design", "01.08.2010", "+998991234588")
jalil_toxirov = Student("Jalil Toxirov", 5625, "C#", "01.08.2014", "+998991234599")
toxir_jalilov = Student("Toxir Jalilov", 4586, "Python", "01.08.2012", "+998991234511")

print(toxir_toxirov)
print(toxir_sobirov)

print(repr(jalil_toxirov))
print(repr(toxir_jalilov))

print(bool(toxir_toxirov))
print(bool(toxir_sobirov))
print(bool(jalil_toxirov))
print(bool(toxir_jalilov))

#=================================================================

# 2 - Masala










