# Create a branch and connect to remote branch
BRANCH_NAME="$1"

# Create the branch
git checkout -b $BRANCH_NAME

# Connect local branch to remote branch 
git branch --set-upstream-to=origin/$BRANCH_NAME $BRANCH_NAME
