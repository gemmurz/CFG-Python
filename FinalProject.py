import requests
import random
import sys

my_score = 0
opponents_score = 0

def random_character():
    character_number = random.randint(0, 24)
    url = 'https://hp-api.onrender.com/api/characters'
    response = requests.get(url)
    character_list = response.json()
    character = character_list[character_number]
    return {
        'name': character['name'],
        'species': character['species'],
        'house': character['house'],
        'student': character['hogwartsStudent'],
        'gender': character['gender'],
    }


def welcome():
    print(r"""""
                                             _ __
            ___                             | '  \
       ___  \ /  ___         ,'\_           | .-. \        /|
       \ /  | |,'__ \  ,'\_  |   \          | | | |      ,' |_   /|
     _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ '-. .-',' |_   _
    // | |  | |____| | | |\_|| |__    //    |     | ,'_`. | | '-. .-',' `. ,'\_
    \\_| |_,' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|   \
     `-. .-'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_|
       | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---'| |
       | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| |
       /_\  | |           //_____//       .||`      `._,' | |   | | \ `-' /| |
            /_\           `------'        \ |              `.\  | |  `._,' /_\
                                           \|     T O P          `.\
                                               T R U M P S
        """"")
    deal = input("Would you like to play? y/n ")

    if deal == 'n':
        print('Come and play again soon!')

def run():

    global my_score, opponents_score

    my_character = random_character()
    print('You have been given {}'.format(my_character['name']))

    opponent_character = random_character()
    print('Your opponent was given {}'.format(opponent_character['name']))

    stat_choice = input('Which stat do you want to use? (species, house, gender or student)')

    my_stat = my_character[stat_choice]
    opponents_stat = opponent_character[stat_choice]

    if stat_choice == 'species':
        if my_stat == 'human' and opponents_stat == 'human':
            print(
                'You are both human, you draw! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            print('Your score is still {}', my_score)
            print('Your opponents score is still {}', opponents_score)
        elif my_stat == 'human' and opponents_stat == 'ghost':
            print('You Win! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'human' and opponents_stat == 'half-giant':
            print(
                'You lose! You are a Human and your opponent is a extremely large and hairy Humanoid. Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!'.format(
                    opponents_stat))
            opponents_score = opponents_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'human' and opponents_stat == 'centaur':
            print(
                'You lose! Your opponent wins! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!'.format(
                    opponents_stat))
            opponents_score = opponents_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'human' and opponents_stat == 'cat':
            print(
                'You win, your opponent wins! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'human' and opponents_stat == 'werewolf':
            print(
                'You lose, your opponent wins! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            opponents_score = opponents_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'ghost' and opponents_stat == 'human':
            print('You win! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'half-giant' and opponents_stat == 'human':
            print(
                'You lose! You are an extremely large Humanoid, and your opponent is Human. Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            opponents_score = opponents_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'half-giant' and opponents_stat == 'ghost':
            print(
                'You win! You are an extremely large Humanoid, and your opponent is a Ghost. Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'half-giant' and opponents_stat == 'centaur':
            print(
                'You win because centaurs are wise and peaceful! Your opponent wins! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'half-giant' and opponents_stat == 'cat':
            print(
                'You win as an extremely large Humanoid! Your opponent wins! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == 'half-giant' and opponents_stat == 'werewolf':
            print(
                'You win as an extremely large Humanoid! Your opponent wins! Newt Scamander helped to develop this game, creatures and Fantastic Beasts win!')
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        else:
            print('We could not determine one of the species... Are one of you a Boggart?')
            play_again()

    if stat_choice == 'house':
        if my_stat == 'Gryffindor':
            if opponents_stat == 'Slytherin':
                print(
                    'You win! Slytherin lose. Gryffindor won the House Cup last year.'.format(my_stat, opponents_stat))
                my_score = my_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Hufflepuff':
                print(
                    'You win! Hufflepuff lose. Gryffindor won the House Cup last year.'.format(my_stat, opponents_stat))
                my_score = my_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Ravenclaw':
                print('You win! Ravenclaw lose. Gryffindor won the House Cup last year'.format(my_stat))
                my_score = my_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Gryffindor':
                print('Draw! You both win! You are both from Gryffindor.')
            else:
                print(
                    'We could not find your opponents House and the Sorting Hat is on Annual Leave, please play again.')
        if my_stat == 'Slytherin':
            if opponents_stat == 'Ravenclaw':
                print('You win! Slytherin are tougher than Ravenclaw... ha ha ha!.'.format(my_stat, opponents_stat))
                my_score = my_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Hufflepuff':
                print('You win! Slytherin are tougher than Hufflepuff... they smell funny!.'.format(my_stat,
                                                                                                    opponents_stat))
                my_score = my_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Gryffindor':
                print('You lose! Your opponent wins! Gryffindor won the House Cup last year.'.format(my_stat,
                                                                                                     opponents_stat))
                opponents_score = opponents_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Slytherin':
                print('You Draw! You are in the same house.'.format(my_stat, opponents_stat))
                print('Your score is still {}', my_score)
                print('Your opponents score is still {}', opponents_score)
            else:
                print(
                    'We could not find your opponents House and the Sorting Hat is on Annual Leave, please play again.')
        if my_stat == 'Hufflepuff':
            if opponents_stat == 'Gryffindor':
                print('You lose! Your opponent wins! Gryffindor won the House Cup last year.'.format(my_stat,
                                                                                                     opponents_stat))
                opponents_score = opponents_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Ravenclaw':
                print('You win! Hufflepuff are better than Ravenclaw.'.format(my_stat, opponents_stat))
                my_score = my_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Slytherin':
                print('You lose! They may be mean, but Slytherin are pretty tough!.'.format(my_stat, opponents_stat))
                opponents_score = opponents_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Hufflepuff':
                print(
                    'Draw! You both lose! You are both from Hufflepuff. Gryffindor won the House Cup last year.'.format(
                        my_stat, opponents_stat))
                print('Your score is still {}', my_score)
                print('Your opponents score is still {}', opponents_score)
            else:
                print(
                    'We could not find your opponents House and the Sorting Hat is on Annual Leave, please play again.')
        if my_stat == 'Ravenclaw':
            if opponents_stat == 'Gryffindor':
                print('You lose! Your opponent wins! Gryffindor won the House Cup last year.'.format(my_stat,
                                                                                                     opponents_stat))
                opponents_score = opponents_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Hufflepuff':
                print('You lose! All the other houses keep beating you!'.format(my_stat, opponents_stat))
                opponents_score = opponents_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)
            elif opponents_stat == 'Slytherin':
                print('You lose! All the other houses keep beating you!'.format(my_stat, opponents_stat))
                opponents_score = opponents_score + 1
                print('Your score is ', my_score)
                print('Your opponents score is ', opponents_score)

            elif opponents_stat == 'Ravenclaw':
                print('You Draw! You are both from Ravenclaw. Gryffindor won the House Cup last year.'.format(my_stat,
                                                                                                              opponents_stat))
                print('Your score is still {}', my_score)
                print('Your opponents score is still {}', opponents_score)
        else:
            print('We could not find your opponents House and the Sorting Hat is on Annual Leave, please play again.')

    if stat_choice == 'student':
        if my_stat and opponents_stat == True:
            print("You draw! You are both student.".format(my_stat, opponents_stat))
            print('Your score is still {}', my_score)
            print('Your opponents score is still {}', opponents_score)
        elif my_stat and opponents_stat == False:
            print("You draw! You are both staff.".format(my_stat, opponents_stat))
            print('Your score is still {}', my_score)
            print('Your opponents score is still {}', opponents_score)
        elif my_stat == True and opponents_stat == False:
            print('You lose! You are just a student!'.format(my_stat, opponents_stat))
            opponents_score = opponents_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif my_stat == False and opponents_stat == True:
            print('You win! Hufflepuff are better than Ravenclaw.'.format(my_stat, opponents_stat))
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        else:
            print('One of you are not staff or a student, please play again.')

    if stat_choice == 'gender':
        if my_stat == 'female' and opponents_stat == 'female':
            print("You draw! You are both female.".format(my_stat, opponents_stat))
            print('Your score is still {}', my_score)
            print('Your opponents score is still {}', opponents_score)
        elif my_stat == 'male' and opponents_stat == 'male':
            print("You draw! You are both male.".format(my_stat, opponents_stat))
            print('Your score is still {}', my_score)
            print('Your opponents score is still {}', opponents_score)
        elif my_stat == 'female' and opponents_stat == 'male':
            print('You win.... women rule the world!!'.format(my_stat, opponents_stat))
            my_score = my_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        elif opponents_stat == 'female' and my_stat == 'male':
            print('You lose! Women rule the world!' .format(my_stat, opponents_stat))
            opponents_score = opponents_score + 1
            print('Your score is ', my_score)
            print('Your opponents score is ', opponents_score)
        else:
            print('Perhaps you are gender neutral, please play again.')


def play_again():

    again = input("Do you want to play again? y/n"

                  )

    if again == 'y':
        play_new_game()
    elif again == 'n':
        print('Thank you for playing. Your final score is ' , my_score)
        print('Your opponents final score is' , opponents_score)
        sys.exit(0)

    else:
        play_again()


def play_new_game():
    run()
    play_again()


welcome()
run()
play_again()