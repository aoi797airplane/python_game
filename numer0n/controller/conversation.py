from numer0n.modules import game


def numer0n_conversations():
    """Function of the conversation between the game and the user."""
    numer0n_conversation = game.numer0n()
    numer0n_conversation.welcome()
    numer0n_conversation.make_answer_number()
    numer0n_conversation.ask_users_expectation()
    numer0n_conversation.response_to_user()
    numer0n_conversation.show_result()


