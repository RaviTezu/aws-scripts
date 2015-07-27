***aws-scripts:***
===
A Collection of Scripts(Mostly Python) for managing various AWS resources.

**AWSDyn-Inv(Python):**
- Extension to ec2.py script which can be used for creating Dynamic Inventory of your AWS ec2 instances. 
- This script is written with the intention of using the generated dyn-inv file for running various ansible play-books.

*Note: Feel free to get in touch with me or create issues in case of any problems/help*

**CloudWatch(Python):**
- Uses boto python module to get the rds instance metrics.
- I have written this to push the CloudWatch metrics to Zabbix. For Zabbix Template, see this: https://github.com/RaviTezu/zabbix_templates

**Ephemeral-Finder(Bash):**
- This script can be used to - Determining if any ephemeral storages are attached to an EC2 instance or not.
- For more informtaion on Ephemeral storage: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html
