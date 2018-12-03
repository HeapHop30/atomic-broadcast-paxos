#!/usr/bin/env python
from utils import *
from classes import *


def client(network, p_id):
    print('-> client ', id)
    client = Client(ip=network['clients']['ip'],
                    port=network['clients']['port'],
                    p_id=int(p_id),
                    network=network)

    client.run()
    print('client done.')


def proposer(network, p_id):
    print('-> proposer', id)
    proposer = Proposer(ip=network['proposers']['ip'],
                        port=network['proposers']['port'],
                        p_id=int(p_id),
                        network=network)

    proposer.max_num_acceptors = 3      # for now is hardcoded
    if proposer.p_id == 0:
        proposer.leader = True


def acceptor(network, p_id):
    print('-> acceptor', id)
    acceptor = Acceptor(ip=network['acceptors']['ip'],
                        port=network['acceptors']['port'],
                        p_id=int(p_id),
                        network=network)

    acceptor.start()


def learner(network, p_id):
    print('-> learner ', id)
    learner = Learner(ip=network['learners']['ip'],
                      port=network['learners']['port'],
                      p_id=int(p_id),
                      network=network)

    learner.start()


if __name__ == '__main__':
    CONFIG_FILE = sys.argv[1]
    role = sys.argv[2]
    p_id = int(sys.argv[3])

    config, MAX_NUM_ACCEPTORS = import_config(CONFIG_FILE)
    network = create_network(config)

    if role == 'acceptor':
        rolefunc = acceptor
    elif role == 'proposer':
        rolefunc = proposer
    elif role == 'learner':
        rolefunc = learner
    elif role == 'client':
        rolefunc = client
    rolefunc(network, p_id)
