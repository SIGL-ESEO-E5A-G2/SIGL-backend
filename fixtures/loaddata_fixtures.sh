#!/bin/bash

python ../manage.py loaddata utilisateur_fixtures.json \
                             role_fixtures.json \
                             promotion_fixtures.json \
                             administrateur_fixtures.json \
                             tuteur_fixtures.json \
                             coordinatriceAlternance_fixtures.json \
                             maitreAlternance_fixtures.json \
                             apprenti_fixtures.json 