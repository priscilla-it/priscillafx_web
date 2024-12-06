#!/bin/bash

# Constants
PGADMIN_PORT=6600
PGADMIN_EMAIL="priscilla.effects@gmail.com"
PGADMIN_PASSWORD="1607"

# Function to display usage
usage() {
    echo "Usage: $0 [--pull] [--stop] [--rm]"
    echo "  --pull  Pull the pgAdmin Docker image."
    echo "  --stop  Stop the pgAdmin container if it's running."
    echo "  --rm    Remove the pgAdmin container if it exists."
    exit 1
}

# Check if the script is run with sudo
if [ "$EUID" -ne 0 ]; then
    echo "Warning: This script should be run with sudo."
fi

# Check if Docker is running, and start it if not
if ! systemctl is-active --quiet docker; then
    echo "Docker is not running. Starting Docker..."
    sudo systemctl start docker
fi

# Parse command-line arguments
PULL=false
STOP=false
RM=false

while [[ "$#" -gt 0 ]]; do
    case $1 in
    --pull) PULL=true ;;
    --stop) STOP=true ;;
    --rm) RM=true ;;
    *) usage ;;
    esac
    shift
done

# Pull the pgAdmin 4 Docker image if --pull is specified
if [ "$PULL" = true ]; then
    echo "Pulling pgAdmin 4 Docker image..."
    sudo docker pull dpage/pgadmin4
fi

# Check if the pgAdmin container exists
CONTAINER_ID=$(sudo docker ps -aq -f name=pgadmin)

if [ -n "$CONTAINER_ID" ]; then
    if [ "$STOP" = true ]; then
        echo "Stopping the pgAdmin container..."
        sudo docker stop "$CONTAINER_ID" || echo "Failed to stop pgAdmin container."
    fi

    if [ "$RM" = true ]; then
        echo "Removing the pgAdmin container..."
        sudo docker rm "$CONTAINER_ID" || echo "Failed to remove pgAdmin container."
    fi
else
    if [ "$STOP" = true ]; then
        echo "No pgAdmin container is running to stop."
    fi
fi

# Run the pgAdmin 4 container if no conflicting flags are set
if [ "$PULL" = false ] && [ "$STOP" = false ] && [ "$RM" = false ]; then
    # Check if the container is already running
    RUNNING_CONTAINER=$(sudo docker ps -q -f name=pgadmin)
    if [ -n "$RUNNING_CONTAINER" ]; then
        echo "The pgAdmin container is already running. Access it at http://localhost:$PGADMIN_PORT"
    else
        # Remove the container if it exists but is not running
        if [ -n "$CONTAINER_ID" ]; then
            echo "Removing existing stopped pgAdmin container..."
            sudo docker rm "$CONTAINER_ID"
        fi

        echo "Running pgAdmin 4 container..."
        sudo docker run -p $PGADMIN_PORT:80 \
            -e "PGADMIN_DEFAULT_EMAIL=$PGADMIN_EMAIL" \
            -e "PGADMIN_DEFAULT_PASSWORD=$PGADMIN_PASSWORD" \
            -v pgadmin_data:/var/lib/pgadmin \
            --name pgadmin \
            -d dpage/pgadmin4

        echo "pgAdmin 4 is now running. Access it at http://localhost:$PGADMIN_PORT"
    fi
fi
