# Goals


## Student model
- name: CharField
- letter_grade: CharField
- number_grade: FloatField
- assignments: ManyToManyField

student.assignments

## Assignment Model
- title: CharField
- description: CharField
- date_assigned: DateField
- date_due: DateField

assignments.student.set #auto pop from 