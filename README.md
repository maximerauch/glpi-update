# glpi-update
## Example
#### Command
`python3 glpi-upgrade.py -v 10.0.10 -p /var/www/instance -c 1`

#### Output

```
> Start upgrading from ^10.0 to version : 10.0.10

> Create temporary folders
        - /tmp/20211117_glpi_upgrade_10.0.10
        - /tmp/20211117_glpi_upgrade_10.0.10/backups
        - /tmp/20211117_glpi_upgrade_10.0.10/download

> Download new version : https://github.com/glpi-project/glpi/releases/download/10.0.10/glpi-10.0.10.tgz
        - Downloading: 0% [0 / 45951202] bytes
        - ...
        - Downloading: 100% [45951202 / 45951202] bytes

> Unzip new version : /tmp/20211117_glpi_upgrade_10.0.10/download/glpi.tgz

> Clean cache folders
    - /var/www/instance/files/_cache
    - /var/www/instance/files/_dumps
    - /var/www/instance/files/_sessions
    - /var/www/instance/files/_tmp
    
> Move instance to tmp folder : /tmp/20211117_glpi_upgrade_10.0.10/backups
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
> Stop upgrading to version 10.0.10
```
