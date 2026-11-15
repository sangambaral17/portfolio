Add-Type -AssemblyName System.Drawing
$taskRoot = Split-Path -Parent $PSScriptRoot
$bitmap = New-Object System.Drawing.Bitmap 1200, 630
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$paper = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#f6f5f0'))
$ink = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#18211e'))
$blue = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#254bd8'))
$muted = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#59615b'))
$line = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml('#d7dcd2')), 1
$smallFont = New-Object System.Drawing.Font 'Arial', 13, ([System.Drawing.FontStyle]::Regular), ([System.Drawing.GraphicsUnit]::Pixel)
$labelFont = New-Object System.Drawing.Font 'Arial', 22, ([System.Drawing.FontStyle]::Bold), ([System.Drawing.GraphicsUnit]::Pixel)
$largeFont = New-Object System.Drawing.Font 'Arial', 85, ([System.Drawing.FontStyle]::Regular), ([System.Drawing.GraphicsUnit]::Pixel)
$italicFont = New-Object System.Drawing.Font 'Georgia', 85, ([System.Drawing.FontStyle]::Italic), ([System.Drawing.GraphicsUnit]::Pixel)
try {
    $graphics.FillRectangle($paper, 0, 0, 1200, 630)
    $graphics.FillRectangle($ink, 65, 60, 48, 48)
    $graphics.DrawString('SB', $labelFont, $paper, 69, 69)
    $graphics.DrawString('Sangam Baral', $labelFont, $ink, 130, 69)
    $graphics.DrawString('SOFTWARE & PRODUCT ENGINEER', $smallFont, $muted, 65, 160)
    $graphics.DrawString('Thoughtful software.', $largeFont, $ink, 57, 210)
    $graphics.DrawString('Real-world purpose.', $italicFont, $blue, 57, 318)
    $graphics.DrawLine($line, 65, 510, 1135, 510)
    $graphics.DrawString('ENGINEERING / PRODUCT / AUTOMATION / AI', $smallFont, $muted, 65, 545)
    $graphics.DrawString('sangambaral.com.np', $labelFont, $ink, 876, 538)
    $bitmap.Save((Join-Path $taskRoot 'assets/social-card.png'), [System.Drawing.Imaging.ImageFormat]::Png)
} finally {
    $graphics.Dispose()
    $bitmap.Dispose()
    $paper.Dispose()
    $ink.Dispose()
    $blue.Dispose()
    $muted.Dispose()
    $line.Dispose()
    $smallFont.Dispose()
    $labelFont.Dispose()
    $largeFont.Dispose()
    $italicFont.Dispose()
}
Write-Output 'Built 1200 x 630 social preview.'
