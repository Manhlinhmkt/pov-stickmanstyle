# Automated strip builder for PV_0018
# Reads vo_script_table.csv and generates strips with exact durations

$vo = Import-Csv 'c:\Users\LinhDM\Documents\GitHub\pov-stickmanstyle\pvle\episodes\PV_0018\vo_script_table.csv'
$allLines = @()
foreach ($row in $vo) {
    $allLines += [PSCustomObject]@{
        VO_ID = $row.VO_ID
        Beat_ID = $row.Beat_ID
        Life_Phase = $row.Life_Phase
        VO_Type = $row.VO_Type
        Words = [int]$row.Word_Count_EN
        Pause = [double]$row.Pause_After
        Duration = [Math]::Round([int]$row.Word_Count_EN / 130.0 * 60 + [double]$row.Pause_After, 2)
    }
}

# Group by beat first
$beatGroups = @()
$currentBeat = $null
$currentGroup = @()
foreach ($line in $allLines) {
    if ($line.Beat_ID -ne $currentBeat) {
        if ($currentGroup.Count -gt 0) { $beatGroups += ,@($currentGroup) }
        $currentBeat = $line.Beat_ID
        $currentGroup = @($line)
    } else {
        $currentGroup += $line
    }
}
if ($currentGroup.Count -gt 0) { $beatGroups += ,@($currentGroup) }

# Now split each beat group into strips of <= 12s
$strips = @()
foreach ($bg in $beatGroups) {
    $accum = @()
    $accumWords = 0
    $accumPauses = 0.0
    
    foreach ($line in $bg) {
        $newWords = $accumWords + $line.Words
        $newPauses = $accumPauses + $line.Pause
        $newDur = [Math]::Round($newWords / 130.0 * 60 + $newPauses, 1)
        
        if ($newDur -gt 12.0 -and $accum.Count -gt 0) {
            # Close current strip
            $strips += [PSCustomObject]@{
                Lines = $accum
                Phase = $accum[0].Life_Phase
                Words = $accumWords
                Pauses = $accumPauses
            }
            # Start new strip with current line
            $accum = @($line)
            $accumWords = $line.Words
            $accumPauses = $line.Pause
        } else {
            $accum += $line
            $accumWords = $newWords
            $accumPauses = $newPauses
        }
    }
    # Close last strip in beat
    if ($accum.Count -gt 0) {
        $strips += [PSCustomObject]@{
            Lines = $accum
            Phase = $accum[0].Life_Phase
            Words = $accumWords
            Pauses = $accumPauses
        }
    }
}

# Output statistics
Write-Output "Total strips: $($strips.Count)"
$totalDur = 0
$idx = 1
foreach ($s in $strips) {
    $dur = [Math]::Round($s.Words / 130.0 * 60 + $s.Pauses, 1)
    $totalDur += $dur
    $first = $s.Lines[0].VO_ID
    $last = $s.Lines[-1].VO_ID
    $cnt = $s.Lines.Count
    $phase = $s.Phase
    $flag = ""
    if ($dur -gt 12) { $flag = " ***OVER***" }
    if ($dur -lt 3) { $flag = " ***UNDER***" }
    Write-Output ("PV_0018_{0:D3} | {1,-8} | {2,-18} | VO {3,-5} to {4,-5} | cnt={5,2} | w={6,3} p={7,4} | dur={8,5}s{9}" -f $idx, $first, $phase, $first, $last, $cnt, $s.Words, $s.Pauses, $dur, $flag)
    $idx++
}
Write-Output ""
Write-Output "Total calculated duration: $([Math]::Round($totalDur,1))s"
Write-Output "Expected: 916.5s"
