$csv = Import-Csv '.\vo_script_table.csv'
$totalWords = 0; $totalPause = 0
foreach($row in $csv) {
    $totalWords += [int]$row.Word_Count_EN
    $totalPause += [double]$row.Pause_After
}
$speechTime = $totalWords / 130 * 60 + $totalPause
$minStrips = [math]::Ceiling($speechTime / 12)
$targetStrips = [math]::Round($speechTime / 8)
$maxStrips = [math]::Floor($speechTime / 4)

Write-Host "=== SPEECH TIME SUMMARY ==="
Write-Host "Total VO lines: $($csv.Count)"
Write-Host "Total Word_Count_EN: $totalWords"
Write-Host "Total Pause_After: $totalPause sec"
Write-Host "Total Speech Time: $([math]::Round($speechTime,1)) sec = $([math]::Round($speechTime/60,1)) min"
Write-Host "Min strip count (max 12s each): $minStrips"
Write-Host "Target strip count (8s sweet spot): $targetStrips"
Write-Host "Max strip count (min 4s each): $maxStrips"
