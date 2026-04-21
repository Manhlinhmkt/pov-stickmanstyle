$vo = Import-Csv 'c:\Users\LinhDM\Documents\GitHub\pov-stickmanstyle\pvle\episodes\PV_0018\vo_script_table.csv'
$strips = Import-Csv 'c:\Users\LinhDM\Documents\GitHub\pov-stickmanstyle\pvle\episodes\PV_0018\illustration_strip_table.csv'

$voLookup = @{}
$allVoIds = @()
foreach ($row in $vo) {
    $voLookup[$row.VO_ID] = $row
    $allVoIds += $row.VO_ID
}

$totalCalcDuration = 0.0
$coveredIds = @()
$violations = @()
$over12 = 0
$under3 = 0

foreach ($strip in $strips) {
    $startIdx = -1; $endIdx = -1
    for ($i = 0; $i -lt $allVoIds.Count; $i++) {
        if ($allVoIds[$i] -eq $strip.Start_VO_ID) { $startIdx = $i }
        if ($allVoIds[$i] -eq $strip.End_VO_ID) { $endIdx = $i }
    }
    if ($startIdx -eq -1 -or $endIdx -eq -1) {
        $violations += "Strip $($strip.Strip_ID): Cannot find VO_IDs $($strip.Start_VO_ID)-$($strip.End_VO_ID)"
        continue
    }
    $words = 0; $pauses = 0.0; $count = 0
    for ($i = $startIdx; $i -le $endIdx; $i++) {
        $coveredIds += $allVoIds[$i]
        $words += [int]$voLookup[$allVoIds[$i]].Word_Count_EN
        $pauses += [double]$voLookup[$allVoIds[$i]].Pause_After
        $count++
    }
    $calcDur = [Math]::Round($words / 130.0 * 60 + $pauses, 1)
    $csvDur = [double]$strip.Duration_Sec
    $totalCalcDuration += $calcDur
    
    if ($count -ne [int]$strip.VO_Count) {
        $violations += "$($strip.Strip_ID): VO_Count CSV=$($strip.VO_Count) Actual=$count"
    }
    if ([Math]::Abs($calcDur - $csvDur) -gt 0.5) {
        $violations += "$($strip.Strip_ID): Duration CSV=$csvDur Calc=$calcDur (w=$words p=$pauses)"
    }
    if ($calcDur -gt 12.0) { $over12++; $violations += "$($strip.Strip_ID): OVER 12s ($calcDur)" }
    if ($calcDur -lt 3.0) { $under3++; $violations += "$($strip.Strip_ID): UNDER 3s ($calcDur)" }
}

$uncovered = $allVoIds | Where-Object { $_ -notin $coveredIds }
$dupCheck = $coveredIds | Group-Object | Where-Object { $_.Count -gt 1 }

Write-Output "=== VALIDATION ==="
Write-Output "Strips: $($strips.Count)"
Write-Output "Total calc duration: $([Math]::Round($totalCalcDuration,1))s (expected 916.5s, tolerance 870.7-962.3)"
Write-Output "Over 12s: $over12"
Write-Output "Under 3s: $under3"
Write-Output "Uncovered VO_IDs: $($uncovered.Count)"
if ($uncovered.Count -gt 0 -and $uncovered.Count -le 10) { Write-Output "  Missing: $($uncovered -join ', ')" }
Write-Output "Duplicate covered: $($dupCheck.Count)"
Write-Output "Violations: $($violations.Count)"
foreach ($v in $violations) { Write-Output "  $v" }
