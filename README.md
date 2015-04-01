***aws-scripts:***
===
A Collection of Scripts(Mostly Python) for managing various AWS resources.

# AWSDyn-Inv:
- Extension to ec2.py script which can be used for creating Dynamic Inventory of your AWS ec2 instances. 
- This script is written with the intention of using the generated dyn-inv file for running various ansible play-books.

*Note: Feel free to get in touch or create issues in case of any problems/help*

#CloudWatch:
- Uses boto python module to get the rds instance metrics.
- I have written this to push the CloudWatch metrics to Zabbix. For Zabbix Template, see this: https://github.com/RaviTezu/zabbix_templates

