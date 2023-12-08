$repo_path = git rev-parse --show-toplevel
# Write-Output $repo_path

& $repo_path\scripts\run_lint.ps1
& $repo_path\scripts\run_unittests.ps1
& $repo_path\scripts\run_typecheck.ps1
