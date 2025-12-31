param(
    [switch]$Json,
    [switch]$RequireTasks,
    [switch]$IncludeTasks
)

# Define the feature directory and available documents
$featureDir = "specs\phase-1"
$availableDocs = @(
    "001-in-memory-console-app.md",    # spec
    "002-implementation-plan.md",      # plan
    "003-tasks-breakdown.md",          # tasks
    "research.md",                     # research
    "data-model.md",                   # data model
    "quickstart.md",                   # quickstart
    "contracts\todo-api-contract.md"   # contracts
)

# Check if tasks.md exists
$tasksPath = "$featureDir\003-tasks-breakdown.md"
$hasTasks = Test-Path $tasksPath

if ($RequireTasks -and -not $hasTasks) {
    Write-Error "Tasks file not found at $tasksPath. Run /sp.tasks first."
    exit 1
}

if ($IncludeTasks) {
    # Read the tasks file content
    $tasksContent = Get-Content $tasksPath -Raw
}

# Output JSON result if -Json switch is used
if ($Json) {
    $result = @{
        FEATURE_DIR = $featureDir
        AVAILABLE_DOCS = $availableDocs
        HAS_TASKS = $hasTasks
        TASKS_CONTENT = if ($IncludeTasks) { $tasksContent } else { $null }
    } | ConvertTo-Json -Compress
    
    Write-Output $result
}