#!/bin/bash
# eval $(cat ./.env | sed 's/ *= */=/' | sed 's/^/export /')
export OPENAI_API_KEY=""

uvicorn main:app --host 0.0.0.0 --port 8000 
