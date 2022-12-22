from aluno_model import Aluno
from string import Template


class Certificado:

    def __init__(self, name, grade, approved):
        """
        :param name: str of a name
        :param grade: int of a grade
        :param approved: str [Aprovado ou reprovado]
        """
        self.name = name
        self.grade = grade
        self.approved = approved
        self._generate_approved_obj()

    def _generate_approved_obj(self):
        if self.approved:
            Aluno.name = self.name
            Aluno.grade = self.grade
            Aluno.passed = self.approved

    def _generate_cert(self):
        template_string = f"Texto do certificado aqui" \
                                   f"O aluno {Aluno.name}" \
                                   f"concluiu o curso" \
                                   f"com grau {Aluno.grade}" \
                                   f"e com o resultado {Aluno.passed}"

        if Aluno.passed:
            return template_string
        return None

    def generate_final_cert(self):
        if Aluno.passed:
            return self._generate_cert()

