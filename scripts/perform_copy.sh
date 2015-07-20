REDIS_SOURCE=/var/lib/redis/6379/dump.rdb
BACKUP_DIR=/backup

BACKUP_PREFIX="redis.dump.rdb"
DAY=`date '+%a'`
REDIS_DEST="$BACKUP_DIR/$BACKUP_PREFIX.$DAY"

cp $REDIS_SOURCE $REDIS_DEST