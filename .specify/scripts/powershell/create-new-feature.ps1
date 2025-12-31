param(
    [Parameter(Mandatory=$true)]
    [string]$Number,
    
    [Parameter(Mandatory=$true)]
    [string]$ShortName,
    
    [Parameter(Mandatory=$true)]
    [string]$FeatureDescription
)

# Create branch name
$branchName = "${Number}-${ShortName}"

# Create spec file path
$specFileName = "{0:000}-in-memory-console-app.md" -f [int]$Number
$specFilePath = "specs\phase-1\$specFileName"

# Output JSON result
$result = @{
    BRANCH_NAME = $branchName
    SPEC_FILE = $specFilePath
} | ConvertTo-Json

Write-Output $result

# Create the branch (we'll just create a placeholder since git operations might not work)
# Create the spec file with basic content
$specContent = @"
# $FeatureDescription

This is a placeholder for the feature specification.
"@

# Write the spec content to file
$specContent | Out-File -FilePath $specFilePath -Encoding UTF8