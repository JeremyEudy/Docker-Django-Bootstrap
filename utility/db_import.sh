docker container exec -i $(docker-compose ps -q test_db) pg_restore -U django -d plexus < /www/Plexus/Docker/config/db/sample_data.pgdump
