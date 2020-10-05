from redis import Redis
from time import sleep

def message_handler(message):
	msg = message['data'].decode('utf-8')
	print(msg)


def main(**kwargs):
	r = Redis(host='redis', port=6379, db=0)
	p = r.pubsub()
	print(r.get('HELLO'))
	p.subscribe(**{ 'test_channel': message_handler })
	thread = p.run_in_thread(sleep_time=0.001)

main()
