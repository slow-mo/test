import os
import scraperwiki

os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'

scraperwiki.sql.save(unique_keys=['id'], data={'id': 1, 'value': 100}, table_name='main')
