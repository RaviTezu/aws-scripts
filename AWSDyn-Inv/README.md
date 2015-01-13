***This script uses ec2.py https://raw.githubusercontent.com/ansible/ansible/devel/plugins/inventory/ec2.py and I've modified it, in a way to use it as a inventory for ansible***

For generating AWS Credentials:
===============================
1. Go to the IAM console.
2. From the navigation menu, click Users.
3. Select your IAM user name.
4. Click User Actions, and then click Manage Access Keys.
5. Click Create Access Key.
6. Your keys will look something like this:
   Access key ID example: AKIAIOSFODNN7EXAMPLE
   Secret access key example: wJalrbXUasdFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
7. Click Download Credentials, and store the keys in a secure location.
8. Your secret key will no longer be available through the AWS Management Console; you will have the only copy. Keep it confidential in order to protect your account, and never email it. Do not share it outside your organization, even if an inquiry appears to come from AWS or Amazon.com. No one who legitimately represents Amazon will ever ask you for your secret key.
9. For more info. See: http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html

Running ec2.py:
==============
1. You need to export the access Credentials first. Run `source ec2-ansible-creds.sh`
2. You may need to modify the ec2.ini before running this or leave it as it is. 
2. Run `./ec2.py`
3. Running the above command will create a new file "dyn-inv". dyn-inv file can be used as a inventory for running ansible commands.
4. This is basically used to create a dynamic inventory for running ansible playooks. 
   Example: ansible-playbook <playbook-name> {production|stage|developement|all} -i dyn-inv

*Note: Feel free to open issues in case of any problems/help*
