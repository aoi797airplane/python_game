import random

from numer0n.views import console


DEFAULT_GAME_NAME = "Numer0n"


class Game(object):

    def __init__(self, game_name=DEFAULT_GAME_NAME, user_name='', speak_color='green'):
        self.game_name = game_name
        self.user_name = user_name
        self.speak_color = speak_color

    def welcome(self):
        """Return the first words to user and ask name."""
        while True:
            template = console.get_template('welcome.txt', self.speak_color)
            user_name = input(template.substitute({
                'game_name': self.game_name}))

            if user_name:
                self.user_name = user_name.title()
                break


class numer0n(Game):

    def __init__(self, game_name=DEFAULT_GAME_NAME, answer_number=[0], difficulty_digit=3, counter=0, expected_number=[0]):
        super().__init__(game_name=game_name)
        self.answer_number = answer_number
        self.difficulty_digit = difficulty_digit
        self.counter = counter
        self.expected_number_list = expected_number

    def _welcome_decorator(func):
        """Decorator to say a greeting if you don't know user's name yet."""
        def wrapper(self):
            if not self.user_name:
                self.welcome()
            return func(self)
        return wrapper

    @_welcome_decorator
    def make_answer_number(self):
        """Make answer number at random."""
        while self.answer_number[0] == 0:
            number_list = list(range(0, 10))
            random.shuffle(number_list)
            self.answer_number = number_list[:3]

    @_welcome_decorator
    def ask_users_expectation(self):
        self.counter += 1
        template = console.get_template('ask_number.txt', self.speak_color)
        expected_number = input(template.substitute({
            'user_name': self.user_name,
            'difficulty_digit': self.difficulty_digit
        }))
        self.expected_number_list = [int(x) for x in expected_number]

    @_welcome_decorator
    def response_to_user(self):
        while True:
            if self.answer_number == self.expected_number_list:
                break
            eat = 0
            bite = len(set(self.answer_number) & set(self.expected_number_list))
            for i in range(0, self.difficulty_digit):
                if self.answer_number[i] == self.expected_number_list[i]:
                    eat += 1
            bite = bite - eat
            template = console.get_template('response.txt')
            print(template.substitute({
                'eat': eat,
                'bite': bite
            }))
            self.ask_users_expectation()
        pass

    def show_result(self):
        template = console.get_template('results.txt', self.speak_color)
        print(template.substitute({
            'user_name': self.user_name,
            'counter': self.counter
        }))