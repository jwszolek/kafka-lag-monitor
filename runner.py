import kafka
import os
import jsonpickle
import subprocess
import optparse
import json
import datetime



def main():
	parser = optparse.OptionParser(description="Kafka monitor tool")
	parser.add_option('-b', '--borkers', dest='brokers', help='broker lists')
	parser.add_option('-o', '--output', dest='output', help='output file')

	opts, args = parser.parse_args()
	outputJson = ""

	p = subprocess.Popen("klag -b %s --format json-discrete" % (opts.brokers), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
	 	consumerGroup = jsonpickle.decode(line)
	 	
		# print consumerGroup['group']
		consumer = kafka.KafkaConsumer(group_id=consumerGroup['group'],bootstrap_servers=opts.brokers.split(','))
		outputJson+="\"%s\":%s," % (consumerGroup['group'],json.dumps(list(consumer.topics())))
		#print jsonpickle.decode(lstTest)

	retval = p.wait()
	outputJson = "{"+outputJson[:-1]+"}"
	command = "klag -b %s --partitions --format json-discrete --groups '%s'" % (opts.brokers,outputJson) 

	lagOutput = ""
	p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		now = datetime.datetime.now()
		date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
		time = str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)
		line = line[:-2] + ",\"date\":\"%s\", \"time\":\"%s\"}\n" % (date, time)
		lagOutput += line
	retval = p.wait()

	with open(opts.output, "a") as myfile:
		myfile.write(lagOutput)

def addToList(oldset, newset):
	return list(oldset | newset)



if __name__ == "__main__":
	main()
