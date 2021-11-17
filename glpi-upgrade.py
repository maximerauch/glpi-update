import argparse
import os
from datetime import date
import sys
import shutil
import wget
import tarfile

# Initialize parser
parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("-v", "--version", help = "Target version", required = True)
parser.add_argument("-p", "--path", help = "Instance folder", required = True)
parser.add_argument("-c", "--clean", help = "Clean after procedure", required = True)

# Read arguments from command line
args = parser.parse_args()

# Check if instance folder exists and is readable
if not os.path.isdir(args.path):
    print("> Error : instance folder doesn't exist or is not readable")
    sys.exit()

# Start procedure
print("\n> Start upgrading to version :", args.version)

# Initialize tmp folders
tmp_upgrade_folder_name = date.today().strftime("%Y%m%d") + "_glpi_upgrade_" + args.version
tmp_upgrade_folder_path = os.path.join('/tmp', tmp_upgrade_folder_name)
tmp_upgrade_sources_folder_path = os.path.join(tmp_upgrade_folder_path, 'sources')
tmp_upgrade_backups_folder_path = os.path.join(tmp_upgrade_folder_path, 'backups')
tmp_upgrade_download_folder_path = os.path.join(tmp_upgrade_folder_path, 'download')

# Delete tmp folders if exists
if os.path.exists(tmp_upgrade_folder_path):
    shutil.rmtree(tmp_upgrade_folder_path)

# Create tmp folders
print("\n> Create temporary folders")
print("\t-", tmp_upgrade_folder_path)
os.makedirs(tmp_upgrade_folder_path, 493)
print("\t-", tmp_upgrade_sources_folder_path)
os.makedirs(tmp_upgrade_sources_folder_path, 493)
print("\t-", tmp_upgrade_backups_folder_path)
os.makedirs(tmp_upgrade_backups_folder_path, 493)
print("\t-", tmp_upgrade_download_folder_path)
os.makedirs(tmp_upgrade_download_folder_path, 493)

# Download new version
def download_bar(current, total, width=80):
    print("\t- Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

download_github_url = "https://github.com/glpi-project/glpi/releases/download/" + args.version + "/glpi-" + args.version + ".tgz"
download_archive_path = tmp_upgrade_download_folder_path + "/glpi.tgz"
print("\n> Download new version :", download_github_url)
wget.download(download_github_url, out = download_archive_path, bar=download_bar)

# Unzip new version
print("\n> Unzip new version :", download_archive_path)
download_archive_file = tarfile.open(download_archive_path)
download_archive_file.extractall(tmp_upgrade_download_folder_path)
download_archive_file.close()

# Delete archive + move extract files
os.remove(download_archive_path)
os.system('rsync -a ' + os.path.join(tmp_upgrade_download_folder_path, 'glpi', '') + ' ' + os.path.join(tmp_upgrade_download_folder_path, ''))
shutil.rmtree(os.path.join(tmp_upgrade_download_folder_path, 'glpi'))

# Move old instance folder
print("\n> Move instance to tmp folder :", tmp_upgrade_sources_folder_path)
os.system('rsync -a ' + os.path.join(args.path, '') + ' ' + os.path.join(tmp_upgrade_sources_folder_path, ''))
shutil.rmtree(args.path)
os.makedirs(args.path, 493)

# Copy new version sources
print("\n> Copy new version sources")
os.system('rsync -a ' + os.path.join(tmp_upgrade_download_folder_path, '') + ' ' + os.path.join(args.path, ''))

# Synchronize files
print("\n> Synchronize files")
os.system('rsync -a ' + os.path.join(tmp_upgrade_sources_folder_path, 'files', '') + ' ' + os.path.join(args.path, 'files', ''))

# Synchronize plugins
print("\n> Synchronize plugins")
os.system('rsync -a ' + os.path.join(tmp_upgrade_sources_folder_path, 'plugins', '') + ' ' + os.path.join(args.path, 'plugins', ''))

# Synchronize glpicrypt.key
print("\n> Synchronize glpicrypt.key")
shutil.copyfile(os.path.join(tmp_upgrade_sources_folder_path, 'config', '') + 'glpicrypt.key', os.path.join(args.path, 'config', '') + 'glpicrypt.key')

# Fix owners
print("\n> Fix owners and rights")
os.system('chown -R www-data:www-data ' + args.path)
os.system('chmod -R 0755 ' + args.path)

# Clean tmp folders
if args.clean:
    print("\n> Clean tmp folders")
    shutil.rmtree(tmp_upgrade_folder_path)
else:
    print("\n> Skip cleaning tmp folders")

# End procedure
print("\n> Stop upgrading to version", args.version)