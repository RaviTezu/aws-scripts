#!/bin/bash

# This script can be used to - Determining if any ephemeral storages are attached to an EC2 instance or not.

# AWS Metadata URL
echo "----------- START -----------"
METADATA_BASEURL="http://169.254.169.254/latest"

# Determing the drive naming convention
root_drive=`df -h | grep '/$' | awk '{print $1}'`
#echo "root drive: $root_drive"
if [ "$root_drive" == "/dev/xvda1" ]; then
  echo "Detected 'xvd' as drive naming convention.."
  CONVENTION='xvd'
else
  echo "Detected 'sd' as drive naming convention.."
  CONVENTION='sd'
fi

# Make a call to AWS Metadata URL to get the ephemeral drives
ephemeral_drives=`curl --silent $METADATA_BASEURL/meta-data/block-device-mapping/ | grep ephemeral`
ephemeral_count=`echo $ephemeral_drives | grep -v "^$" | wc -l`

# Print out the ephemeral drives
echo " "
if [ $ephemeral_count -eq 0 ]; then
  echo "No epehemeral storage are found on this host.."
  exit 0
else
  echo "Found below Epehemeral drives on `hostname`: "
  for ephe in $ephemeral_drives; do 
    device_name=`curl --silent $METADATA_BASEURL/meta-data/block-device-mapping/$ephe`
    device_conv_name=`echo $device_name | sed "s/sd/$CONVENTION/"`
    device_path="/dev/$device_conv_name"
    mounted_on=`df -h $device_path | tail -1 | awk '{print $6}'`
    echo "$device_path($device_name) -> $mounted_on"
  done
fi
echo "------------ END ------------"
