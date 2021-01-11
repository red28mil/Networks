!/bin/bash


pihole -b -d --regex '(^|\.)disneyplus\.com$' '(^|\.)amazon\.com$' '(^|\.)youtube\.com$' '(^|\.)netflix\.com$'


