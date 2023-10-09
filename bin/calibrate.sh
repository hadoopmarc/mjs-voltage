
# This script finds tasmota plugs on the local network and
# then run a calibrate python script with the plugs found
# as arguments

set -e

echo "192.34" | sed 's/[.]34/.0/'
echo "192.34" | sed 's/\(10\|178\|192\)[.]34/\1.0/'

prefix='\(10\|178\|192\)'
number='\([0-9]\{1,3\}\)'
subnetsize='\([1-9][0-9]\)'
echo "192.34/24" | sed "s/$prefix[.]$number\/$subnetsize/\1.0\/\3/"
echo "192.168.2.34/24" | sed "s/$prefix[.]$number[.]$number[.]$number\/$subnetsize/\1.\2.\3.0\/\5/"


#echo "192.168.2.34/24" | sed 's/\(10\|178\|192\)[.]34/\1.0/'

# ip addr | grep "inet " | awk '{print $2}' | sed 's/\(10|178|192\)[.]\([0-9]\{1,3\}\)[.]\([0-9]\{1,3\}\)[.]\([0-9]\{1,3\}\)[/]/.0\//'

# ip addr | grep "inet " | awk '{print $2}' | sed 's/\(10|178|192\)[.]\([0-9]\{1,3\}\)[.]\([0-9]\{1,3\}\)[.]\([0-9]\{1,3\}\)[/]/.0\//'

#sudo ls
#sudo -k  # revoke sudo again

