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
> Move instance to tmp folder : /tmp/20211117_glpi_upgrade_9.5.6/backups
> Copy new version sources

> Synchronizing
        - files
        - plugins
        - marketplace
        - logos
        - config/glpicrypt.key

> Fix owners and rights
> Clean tmp folders
> Stop upgrading to version 9.5.6
```
