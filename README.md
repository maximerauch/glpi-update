# glpi-update
## Example
#### Command
`python3 glpi-upgrade.py -v 9.5.6 -p /var/www/instance -c 1`

#### Output

```
> Start upgrading to version : 9.5.6

> Create temporary folders
        - /tmp/20211117_glpi_upgrade_9.5.6
        - /tmp/20211117_glpi_upgrade_9.5.6/backups
        - /tmp/20211117_glpi_upgrade_9.5.6/download

> Download new version : https://github.com/glpi-project/glpi/releases/download/9.5.6/glpi-9.5.6.tgz
        - Downloading: 0% [0 / 45951202] bytes
        - ...
        - Downloading: 100% [45951202 / 45951202] bytes

> Unzip new version : /tmp/20211117_glpi_upgrade_9.5.6/download/glpi.tgz

> Clean cache folders
    - /var/www/instance/files/_cache
    - /var/www/instance/files/_dumps
    - /var/www/instance/files/_sessions
    - /var/www/instance/files/_tmp
    
> Move instance to tmp folder : /tmp/20211117_glpi_upgrade_9.5.6/backups
> Copy new version sources

> Synchronizing
        - files
        - plugins
        - marketplace
        - cert
        - pics/logos/logo-G-100-black.png
        - pics/logos/logo-G-100-grey.png
        - pics/logos/logo-G-100-white.png
        - pics/logos/logo-GLPI-100-black.png
        - pics/logos/logo-GLPI-100-grey.png
        - pics/logos/logo-GLPI-100-white.png
        - pics/logos/logo-GLPI-250-black.png
        - pics/logos/logo-GLPI-250-grey.png
        - pics/logos/logo-GLPI-250-white.png
        - pics/favicon.ico
        - config/config_db.php
        - config/glpicrypt.key

> Fix owners and rights
> Clean tmp folders
> Stop upgrading to version 9.5.6
```
