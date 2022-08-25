

# Mapr

## Overview
Registers users and their locations and organizes them. Display users and their location on an interactive map. Sort users by social groups.

## Functionality
- Allow users to join groups
- Users can signup/login
    - Store users initial location on signup
- Allow users to set their profile to private
- Show a map of given users (group)

#### Libraries
- Django
- JavaScript

## Data Model
User
- username
- password
- location (ForeignKey)
- groups (ManytoMany)
- private

Location
- latitude
- longitude
- timezone (nullable)

Group
- name
- private
- events (default=None)

Event
- tbd

