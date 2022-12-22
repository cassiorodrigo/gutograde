from certificate import Certificado


def run():
    student: str or None = None
    while student != "Me deixa em paz":
        std = str(input("Student name: "))
        grade = str(input("Student name: "))
        app = str(input("Student name: "))
        new_cert = Certificado(std, grade, app)
        print(new_cert.generate_final_cert())
