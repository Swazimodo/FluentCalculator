Write-Output "`n`nrunning mypy"

$repo_path = git rev-parse --show-toplevel
. $repo_path\.venv\Scripts\Activate.ps1

python -m mypy $repo_path\calc $repo_path\tests `
  --check-untyped-defs `
  --disallow-any-unimported `
  --disallow-any-decorated `
  --disallow-any-explicit `
  --disallow-any-generics `
  --disallow-subclassing-any
