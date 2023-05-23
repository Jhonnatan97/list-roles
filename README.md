### README

This repository contains a script that interacts with AWS Identity and Access Management (IAM) using the Boto3 library. The script retrieves a list of IAM roles from the AWS account and saves the role names and ARNs to a CSV file.

## Prerequisites

Before running the script, ensure you have the following:

1 - Python installed on your system.  
2 - Boto3 library installed. You can install it using the following command:  

> pip install boto3


## Getting Started


To use the script, follow these steps:

1 - Clone this repository to your local machine or download the script directly.  

2 - Ensure you have valid AWS credentials configured on your machine. You can set up AWS CLI credentials using the AWS CLI or by manually configuring the ~/.aws/credentials file.  

3 - Open the script file script.py in a text editor or integrated development environment (IDE) of your choice.  

4 - Modify the profile_name and region_name parameters in the line boto3.setup_default_session(profile_name='sso-bpp', region_name='') according to your AWS profile and desired region.  

5 - Save the modifications to the script file.

6 - Open a terminal or command prompt, navigate to the directory containing the script, and run the following command:  
> python script.py

7 - The script will retrieve the IAM roles from your AWS account and display the role names and ARNs in the terminal/command prompt.  

8 - The script will create a CSV file named role.csv and save the role names in the file.  


## File Structure

The repository contains the following files:  
* 'script.py': The main script file that retrieves IAM roles and saves them to a CSV file.  
* 'file_handler.py': A helper module that handles CSV file creation and saving.  


## Contributing

If you find any issues with the script or have suggestions for improvement, please feel free to open an issue or submit a pull request. Your contributions are welcome.  

