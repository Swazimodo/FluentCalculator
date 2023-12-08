Write-Output "`n`nrunning linter"

$repo_path = git rev-parse --show-toplevel
. $repo_path\.venv\Scripts\Activate.ps1

python -m pylint $repo_path/calc
