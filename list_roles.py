from file_handler import FileHandler
import boto3


if __name__ == '__main__':

    collum_title = ["ROLE_NAME"]
    row_list = []


    boto3.setup_default_session (profile_name='profile_name', region_name='')
    client = boto3.client ('iam')
    roles = []

    response = client.list_roles ()
    roles.extend (response['Roles'])
    while 'Marker' in response.keys ():
        response = client.list_roles (Marker=response['Marker'])
        roles.extend (response['Roles'])
    print ('roles found: ' + str (len (roles)))
    for role in roles:
        role_name = role['RoleName']
        role_arn = role['Arn']
        print ("RoleName:",role_name + " - " + "Arn:",role_arn)
        response = client.get_role(RoleName=role_name)
        print(response)
        row = [str(role_name)]
        row1 = [str(role_arn)]
        row_list.append(row)

    file_handler = FileHandler()
    file_handler.create_csv('role', collum_title)
    file_handler.save_csv('role', row_list)


