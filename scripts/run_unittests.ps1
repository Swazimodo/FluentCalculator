Write-Output "`n`nrunning unit tests"

$repo_path = git rev-parse --show-toplevel
. $repo_path\.venv\Scripts\Activate.ps1

python -m pytest $repo_path
