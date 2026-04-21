$csv = Import-Csv '.\vo_script_table.csv'
$totalWords = 0; $totalPause = 0
foreach($row in $csv) {
    $totalWords += [int]$row.Word_Count_EN
    $totalPause += [double]$row.Pause_After
}
$speechTime = $totalWords / 130 * 60 + $totalPause
Write-Host "=== DE-AI v5.1 VERIFICATION ==="
Write-Host "Total VO lines: $($csv.Count)"
Write-Host "Total Word_Count_EN: $totalWords"
Write-Host "Total Pause_After: $totalPause sec"
Write-Host "Total Speech Time: $([math]::Round($speechTime,1)) sec = $([math]::Round($speechTime/60,2)) min"
Write-Host ""
Write-Host "=== PATTERN CHECK ==="
$youDont = ($csv | Where-Object { $_.VO_EN -match "You don't" }).Count
Write-Host "'You don't' occurrences: $youDont"
$weightLines = ($csv | Where-Object { $_.VO_Type -eq 'WEIGHT_LINE' }).Count
Write-Host "WEIGHT_LINE count: $weightLines"
Write-Host ""
Write-Host "=== 'You don't' lines ==="
$csv | Where-Object { $_.VO_EN -match "You don't" } | ForEach-Object {
    Write-Host "  VO $($_.VO_ID): $($_.VO_EN)"
}
