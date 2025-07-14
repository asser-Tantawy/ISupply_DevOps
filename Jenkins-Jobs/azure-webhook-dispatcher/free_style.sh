#!/bin/bash
set -e
echo "Received webhook event:"
echo "Event Type:$EVENT_TYPE"
echo "Branch:$BRANCH_NAME"
echo "Repository:$REPOSITORY_NAME"
echo "Source branch :$SOURCE_BRANCH"
echo "PR ID :$PR_ID"

if [ "$EVENT_TYPE" == "git.push" ]; then
    echo "it is a push event"
	CLEAN_BRANCH=$(echo "$BRANCH_NAME" | sed -E 's/\["refs\/heads\/(.+)"\]/\1/')
else
    echo "it is a PR"
    CLEAN_BRANCH=${SOURCE_BRANCH#refs/heads/}
fi


#echo "payload is : "
TARGET_BRANCH=$(echo "$GENERIC_WEBHOOK_POST_CONTENT" | jq -r '.resource.targetRefName')
TARGET_BRANCH=${TARGET_BRANCH#refs/heads/}
echo "Target branch :$TARGET_BRANCH"

echo "Clean Branch:$CLEAN_BRANCH"


# Create webhook data directory if it doesn't exist
mkdir -p /var/jenkins_home/webhook-data
# Create a properties file with webhook data
cat > /var/jenkins_home/webhook-data/webhook-${BUILD_NUMBER}.properties << EOF
WEBHOOK_EVENT_TYPE=$EVENT_TYPE
WEBHOOK_BRANCH=$CLEAN_BRANCH
WEBHOOK_REPO=$REPOSITORY_NAME
WEBHOOK_TIMESTAMP=$(date +%s)
BUILD_TRIGGER_ID=${BUILD_NUMBER}
WEBHOOK_TARGET_BRANCH=$TARGET_BRANCH
WEBHOOK_PR_ID=$PR_ID

EOF

# Set environment variables for the multibranch pipeline
export WEBHOOK_EVENT_TYPE="$EVENT_TYPE"
export WEBHOOK_BRANCH="$CLEAN_BRANCH"
export WEBHOOK_REPO="$REPOSITORY_NAME"
export BUILD_TRIGGER_ID="${BUILD_NUMBER}"

# Trigger the multibranch pipeline
#echo "http://139.59.143.83:8080/job/mycatalog/job/$CLEAN_BRANCH/build"
curl -X POST "http://139.59.143.83:8080/job/mycatalog/job/$CLEAN_BRANCH/build" \
  --user "$JENKINS_USER:$JENKINS_PASS" \
  --data "delay=0sec"
