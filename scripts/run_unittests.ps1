Write-Output "`n`nrunning mypy"

$repo_path = git rev-parse --show-toplevel
. $repo_path\.venv\Scripts\Activate.ps1
