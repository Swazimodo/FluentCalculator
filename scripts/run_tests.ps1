$repo_path = git rev-parse --show-toplevel
# Write-Output $repo_path

& $repo_path\scripts\run_typecheck.ps1
