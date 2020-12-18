#!/usr/bin/env bash

FLAG=0

function usage {
  cat <<EOF
Usage: $(basename "$0") [OPTION]...
  -t    Action type: <add|del>
  -f    Bind9 DNS zone file
  -n    hostname(without domain suffix)
  -h    display help

EOF
  exit 2
}

function log {
    msg=$1
    /bin/date +"[%Y/%m/%d %H:%M:%S]: $msg" >> $LOG
}

function take_sanpshot {
    # $1: dataset name

    #now=$(date +"%Y%m%d-%H%M")
    now=$(date +"%Y%m%d-%H%M%S")
    log "[take_snapshot] Snapshot: $ZFS_POOL/$1@$now"
    zfs snapshot $ZFS_POOL/$1@$now
}

function clean_snapshot {
    # $1: dataset name

    for snap in $(zfs list -t snap -H -p -s creation -o name | grep $ZFS_POOL/$1 | head -n -$KEEP_SNAPSHOT);do
        log "[INFO] clean snapshot: $snap"
        zfs destroy $snap
    done
}

function check_backup {
    # $1: dataset name
    # $2: latest snapshot

    latest_backup=$(ssh $ZFS_REMOTE_LOGIN zfs list -t snap -H -p -s creation -o name | grep "$HOST-$1" | tail -1)
    latest_backup_ts=${latest_backup##*@}
    latest_snapshot_ts=${2##*@}

    if [ "$latest_snapshot_ts" == "$latest_backup_ts" ];then
        log "[INFO] latest_snapshot_ts($latest_snapshot_ts)==latest_backup_ts($latest_backup_ts), NO NEED TO BACKUP($1)."
        FLAG=1
    else
        FLAG=0
    fi
}

function send_init_snapshot {
    # $1: dataset name
    # $2: latest snapshot

    backup_name="$HOST-$1"

    log "[send_init_snapshot] Send: $2"
    zfs send $2 | ssh $ZFS_REMOTE_LOGIN zfs recv -F $ZFS_REMOTE_POOL/$backup_name
    ret=$?
    if [ $ret -ne 0 ];then
        log "[ERROR] send_init_snapshot failed, CHECK DATASET ON BACKUP HOST($1)"
    fi
}

function send_incremental_snapshot {
    # $1: dataset name

    latest_snapshot=($(zfs list -t snap -H -p -s creation -o name | grep "$ZFS_POOL/$1" | tail -1))
    latest_backup=$(ssh $ZFS_REMOTE_LOGIN zfs list -t snap -H -p -s creation -o name | grep "$HOST-$1")
    if [ -z "$latest_backup" ];then
        log "[INFO] NO BACKUP FOR DATASET($1), send_init_snapshot"
        send_init_snapshot $1 $latest_snapshot
    else
        log "[send_incremental_snapshot] Send: $ZFS_POOL/$1@$latest_backup_ts -> $latest_snapshot"
        backup_name="$HOST-$1"
        zfs send -i $ZFS_POOL/$1@$latest_backup_ts $latest_snapshot | ssh $ZFS_REMOTE_LOGIN zfs recv -F $ZFS_REMOTE_POOL/$backup_name
    fi

}

# Parse command line arguments
while getopts ":t:f:n:h" opt; do
    case "$opt" in
        t)
            TYPE=${OPTARG}
            ([ "$TYPE" == "add" ] || [ "$TYPE" == "del" ]) || usage
            ;;
        f)
            ZONE_FILE=$OPTARG
            ;;
        n)
            HOSTNAME=$OPTARG
            ;;
        h|*)
            usage
            ;;
    esac
done
#shift $((OPTIND-1))

if [ "$TYPE" == "add" ];then
    if [ -z "${ZONE_FILE}" ] || [ -z "${HOSTNAME}" ];then
        usage
    fi
elif [ "$TYPE" == "del" ];then
    if [ -z "${ZONE_FILE}" ] || [ -z "${HOSTNAME}" ]; then
        usage
    fi
else
    usage
fi

# Avoid globbing
set -f
BIND9_CONF_PATH=/etc/bind
PWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
LOG="$PWD/dns.log"
HOST=$(hostname)



if [ "$TYPE" == "add" ];then
    echo "add $ZONE_FILE $HOSTNAME"
elif [ "$TYPE" == "del" ];then
    echo "del $ZONE_FILE $HOSTNAME"
else
    usage
fi



