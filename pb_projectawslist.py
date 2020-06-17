
def lambda_handler(context,event):


    AWS_services = [
    ' S3.'
    ' EC2 ',
    ' Lambda.',
    ' Glacier.'
    ' SNS.',
    ' CloudFront.',
    ' EBS [Elastic Block Store',
    ' Kinesis.'
    ]

    #Create a list of awsv services
    # these are the list that show specific servies .




    item = 0
    item = '#'.join (AWS_services)
    print(item)
    for item in AWS_services:

        # Near_extinc = []

        if  item in ' S3.':
            print('This is one of the AWS services')
        elif item == 'S3.':
            print('please refere to another service')

            first_letters = ['A','B','C']
            output_names = [AWS_services for AWS_services in AWS_services if (AWS_services[0] in first_letters)]
            output_names
            [' S3.'
            ' EC2 ',
            ' Lambda.',
            ' Glacier.'
            ' SNS.',
            ' CloudFront.',
            ' EBS [Elastic Block Store',
            ' Kinesis.']

            AWS_services.sort()
            AWS_services.append(item) if item not in AWS_services else None
            print(item)
