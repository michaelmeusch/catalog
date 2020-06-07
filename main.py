

import boto3
from account_access import *
from static_params import *



def lambda_handler(event, context):
    #
    # animal_list = [
    #     'adbark',
    #     'penguin',
    #     'zebra'
    # ]
    #
    # for item in animal_list:
    #     print(item)
    #     if item == 'penguin':
    #         print ('I love Penguins.')
    #     elif item == 'zebra':
    #         print ('I love Zebras')
    #     else:
    #         print ('This in not a penguin')
    # print('I finished my for loop')


    endangered_bird = [
        'Albatros',
        'Kiwi bird',
        'Wood pecker',
        'Penguin',
        'Cardinal',
        'Bob White',
        'Dog bird'
        ]
        #Create a list of endangered birds and birds near extinction
    # these are the list that show speices and threat levels.
    Near_extinc = ['Albatros','Kiwi bird'],
    On_ESP_List = ['Albatros','Kiwi bird','Wood pecker'],
    habitat_low = ['Wood pecker','Bob White','Dog Bird']
    for item in endangered_bird:
            print (item)
            if item in Near_extinc:
                print ('These birds are near extinction.')
            if item in On_ESP_List:
                print ('These birds are on the endangered species list.')
            else:
                print('These birds are A Ok')
            if item in Near_extinc:
                print ('These birds are being monitored yearly')
            else:
                print ('These birds are in healthy numbers')
            if item in habitat_low:
                else:
                print ('These birds are being monitered in thier habitats')
    # print out list in Alphebitcal order.

    for item in sorted(endangered_bird):
        print(item)












    # for item in endangered_bird:
    #     print (item)
    #     if item == 'Albatros':
    #         print ('This is a rare and endangered bird.')
    #     else:
    #         print ('This species is not near extinction.')
    #     if item == 'kiwi bird':
    #         print ('This bird is near extinction')
    #     else: ('This bird is not near extinction')
    #     if item == 'wood pecker':
    #         print ('This bird is low in habitat.')
    #     elif item == 'penguin':
    #         print ('This species in not applicable')
    # print ('I completed the assigned task')



    # # I'm difinining a list of people to the birthday party_list.
    # birthday_party = [
    #     'Sammy',
    #     'Kyle',
    #     'Sarah',
    #     'Karen'
    #     ]
    #
    # # This is the list of the people who rsvp
    # party_list = ['Sammy','Kyle','Sarah']
    # # I'm going to loop through everyone that is invited to the party
    # for item in birthday_party:
    #     print (item)
    #     # Evaluate RSVP status
    #     if item in party_list:
    #         print ('Thanks for the RSVP.')
    #     # If no rsvp then remind
    #     else:
    #         print ('Ive noticed you havent RSVP for the party yet!')
    #




    #     elif item == 'Kyle':
    #         print ('Thanks for the RSVP.')
    #
    #     elif item == 'Sarah':
    #         print ('Thanks for the RSVP.')
    #
    #     elif item == 'Karen':
    #
    #         print ('Ive noticed you havent RSVP for the party yet!')
    #
    #
    # print ('These are the final guest list for the party!')
    #









'''
    # creating a session for IAM User Removal
    session = create_session(acct_compliance, role)
    client_iam = session.client('iam')

    account_list = [
        acct_audit,
        acct_tools,
        acct_demo,
        # acct_nonprod,
        # acct_transit,
        acct_compliance #hub
    ]


    item = 0
    for account in account_list:
        print(str(item))
        print (account)
        item += 1

        list_users_results = list_users (account, role)
        # session = create_session(account, role)
        # client_iam = session.client('iam')
        #
        # users = client_iam.list_users()['Users']
        # print(str(users))
        # for user in users:
        #     print (user['UserName'])

# input and output static_params
def list_users (account_number, role):
    session = create_session(account_number, role)
    client_iam = session.client('iam')

    users = client_iam.list_users()['Users']

    for user in users:
        print (user['UserName'])

        for user in users['Users']:
            print("UserName: {0}\nCreateDate: {1}\n"
            format(user['UserName'], user['CreateDate']))


# PEER-REVIEW: you were missing the ":" at the end of your functions first line
# def create_user(account_name, role)
def create_user(account_name, role):
    # Path='string',
    UserName='Bigbubba'
    session = create_session(UserName, role)

    # PEER-REVIEW:  commented out next line of code because you can use the client until you create (the line after this line)
    #user = client_iam.list_users()['Users']

    # PEER-REVIEW:  use all lower case and underscores when defining variables
    #Client_iam = session.client('iam')
    client_iam = session.client('iam')

    # PEER-REVIEW: add your new method for creating a user after this line, using
    #   the client you created above "client_iam" (need to look up how to create a user in Boto3)
     response = client.create_user(UserName='Bigbubba')
)

     print(response)
    # PEER-REVIEW: this loop for printing IAM users was only applicable for the list_users method's result
    # replace it with something that will indicate whether you were successful when creating the new user
    for user in users:
        print ('user successfully created.')


    # this function will delete any user.
def delete_user (iam, account_name, role):
    # Path='string',
    UserName='Bigbubba'



    delete_users = iam.delete()(UserName='Bigbubba')
)

     print(response)
    # PEER-REVIEW: this loop for printing IAM users was only applicable for the list_users method's result
    # replace it with something that will indicate whether you were successful when creating the new user
    for user in users:
        print ('user successfully deleted.')

    account_list = [
        acct_audit,
        acct_tools,
        acct_demo,
        # acct_nonprod,
        # acct_transit,
        acct_compliance #hub
    ]

    # This function will delete users from all accounts.
    item = 0
    for account in account_list:
        print(str(item))
        print (account)
        item += 1

        delete_in_all_acc = delete_user(iam, account, role)
        # session = create_session(account, role)
        # client_iam = session.client('iam')
        #
        # users = client_iam.list_users()['Users']
        # print(str(users))
        # for user in users:
        #     print (user['UserName'])







{
    'Users':
        {
            'Path': 'string',
            'UserName': 'Bigbubba',
            'UserId': 'string',
            'Arn': 'string',
            'CreateDate': datetime(2015, 1, 1),
            'PasswordLastUsed': datetime(2015, 1, 1),
            'PermissionsBoundary': {
                'PermissionsBoundaryType': 'PermissionsBoundaryPolicy',
                'PermissionsBoundaryArn': 'string'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
    ],
    'IsTruncated': True|False,
    'Marker': 'string'
}
'''
