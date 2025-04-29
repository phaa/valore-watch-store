#!/bin/bash

echo "Building the containers..."
docker compose build

echo "Upgrading the services."
docker compose up -d --build

echo "Checking the status of the containers..."
docker compose ps

echo "Project running at http://localhost:8000"

echo ""
echo "To stop the containers execute: docker compose down"