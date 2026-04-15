# Update main
git checkout main
git pull origin main

# Rebase every local branch onto main and force push the rebased branches
git branch --format='%(refname:short)' | Where-Object { $_ -ne 'main' } | ForEach-Object {
    git checkout $_
    git rebase main
    git push --force-with-lease origin $_
}

# Go back to main
git checkout main
