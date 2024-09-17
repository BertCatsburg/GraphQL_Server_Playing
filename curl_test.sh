#!/bin/bash

curl -X POST http://localhost:8000/graphql \
-H "Content-Type: application/json" \
-d '{
    "query": "query { hello }"
}'

echo ""