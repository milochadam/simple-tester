class Question:
    def __init__(self, q=None, a=None, **kwargs):
        self._question = q
        self._answer = a
        other = kwargs.get('question')
        if other:
            self._question = other.get_question()
            self._answer = other.get_answer()

        self.inverted = kwargs.get('inverted', False)
        if self.inverted:
            self._question, self._answer = self._answer, self._question

    def get_question(self):
        return self._question

    def get_answer(self):
        return self._answer

    def __str__(self):
        return f'{self._question} - {self._answer}'
