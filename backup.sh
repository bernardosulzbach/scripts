#!/usr/bin/env bash

BACKUP_PATH="/home/mafagafogigante/Backup/documents"
BACKUP_FILE_NAME="$(date +%Y-%m-%d-%H)-documents.tar.gz"
BACKUP_FULL_PATH=$BACKUP_PATH$BACKUP_FILE_NAME

DOCUMENTS="/home/mafagafogigante/Dropbox/Documents/"
SPREADSHEETS="/home/mafagafogigante/Dropbox/Spreadsheets/"
SAVES="/home/mafagafogigante/The Escapists/"

mkdir -p $BACKUP_PATH
cd $BACKUP_PATH
tar --absolute-names -zcf $BACKUP_FILE_NAME $DOCUMENTS $SPREADSHEETS $SAVES
