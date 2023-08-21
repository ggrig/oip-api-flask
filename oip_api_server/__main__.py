#!/usr/bin/env python3

import connexion

from oip_api_server import encoder

import logging, logging.config

# set up logging
logging.config.fileConfig("oip_api_server/log.ini")
logger = logging.getLogger('sLogger')

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    logger.info('App starting...')    
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'OIP API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
