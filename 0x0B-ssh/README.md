                        SSH
                Requirements
        General:
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

        Tasks:
Use a private Key: Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu. Only uses ssh single-character flags.
Create an SSH key pair: A bash script that creates an RSA key pair. The name of created private key is school, number of bits in the created key are 4096, and the created key is protected by the passphrase betty.
Client configuration file:
Let me in! : Add the SSH public key below to your server so that we can connect using the ubuntu user.
Client configuration file (w/ Puppet)
