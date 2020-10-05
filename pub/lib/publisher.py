from redis import Redis
from time import sleep

def main(**kwargs):
	r = Redis(host="redis", port=6379, db=0)
	r.set('HELLO','WORLD')
	print('HELLO')
	while True:
		r.publish('test_channel','ping!')
		sleep(1)

if __name__ == '__main__':
	main()
