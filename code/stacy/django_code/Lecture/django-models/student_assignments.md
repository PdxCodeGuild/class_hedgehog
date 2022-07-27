# Goals

## Student Model
name: CharField
letter_grade: CharField
number_grade: IntegetField
age: IntegerField
assignments: ManyToManyField

## Assignment Model
title: CharField
description: CharField
date_assigned: DateField
date_due: DateField
