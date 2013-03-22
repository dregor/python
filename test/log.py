import logging as Log,sys
log = Log.getLogger('log')
Log.basicConfig( level = Log.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(process)d - %(processName)s - %(message)s' )
#log.addHandler( Log.StreamHandler() )
log.info('Запуск распаковки ')
