

KNOWN_DB_CLASSES = ('msaccess',
                    'msolap',
                    'bigquery',
                    'asterncluster',
                    'bigsql',
                    'aurora',
                    'awshadoophive',
                    'dataengine',
                    'DataStax',
                    'db2',
                    'essbase',
                    'exasolution',
                    'excel',
                    'excel-direct',
                    'excel-reader',
                    'firebird',
                    'powerpivot',
                    'genericodbc',
                    'google-analytics',
                    'googlecloudsql',
                    'google-sheets',
                    'greenplum',
                    'saphana',
                    'hadoophive',
                    'hortonworkshadoophive',
                    'maprhadoophive',
                    'marklogic',
                    'memsql',
                    'mysql',
                    'netezza',
                    'oracle',
                    'paraccel',
                    'postgres',
                    'progressopenedge',
                    'redshift',
                    'snowflake',
                    'spark',
                    'splunk',
                    'kognitio',
                    'sqlserver',
                    'salesforce',
                    'sapbw',
                    'sybasease',
                    'sybaseiq',
                    'tbio',
                    'teradata',
                    'vectorwise',
                    'vertica',
                    'denormalized-cube',
                    'csv',
                    'textscan',
                    'webdata',
                    'webdata-direct',
                    'cubeextract')


def is_valid_dbclass(dbclass):
    return dbclass in KNOWN_DB_CLASSES
