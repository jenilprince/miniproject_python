student_data={
    'Name': 'Bob',
    'Subjects': {
        "English": 87,
        "Science": 98,
        "Maths": 89,
        "History": 82
    }
}
def avrg(a,b,c,d):
    return (a+b+c+d)/4
print(avrg(student_data["Subjects"]["English"],student_data["Subjects"]["Science"],student_data["Subjects"]["Maths"],student_data["Subjects"]["History"]))

