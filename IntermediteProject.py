def calculate_highest_in_maths(student_list):

    highest_score_in_Maths = 0
    highest_score_in_Maths_name = ''

    for student in student_list:
        if (student.get("Maths") > highest_score_in_Maths):
            highest_score_in_Maths = student.get("Maths")
            highest_score_in_Maths_name = student.get('name')

    print(f"The Highest scorer in Maths Function is {highest_score_in_Maths} by {highest_score_in_Maths_name}")


student_1 = {

    "kannada": 45,
    "Maths": 75,
    "Social": 74,
    "name": "Abhi"
}

student_2 = {

    "kannada": 98,
    "Maths": 74,
    "Social": 74,
    "name": "Bhanu"
}

student_3 = {

    "kannada": 95,
    "Maths": 00,
    "Social": 64,
    "name": "chethan"
}

student_list = [student_1, student_2, student_3]

calculate_highest_in_maths (student_list)
