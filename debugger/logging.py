import logging

logging.basicConfig(filename="app.log",level=logging.DEBUG)


log=logging.getLogger()

log.info("Olá")
log.critical("Erro grave")
log.error("Erro")
log.debug("Erro grave")
log.warning("Erro grave")
log.level