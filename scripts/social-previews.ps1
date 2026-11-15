Add-Type -AssemblyName System.Drawing
$taskRoot = Split-Path -Parent $PSScriptRoot
function New-PreviewCard($filename, $backgroundColor, $accentColor, $label, $firstLine, $secondLine, $footerText) {
  $bitmap = New-Object System.Drawing.Bitmap 1200, 630
  $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
  $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
  $paper = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml($backgroundColor))
  $ink = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#18211e'))
  $accent = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml($accentColor))
  $muted = New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml('#59615b'))
  $line = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml('#d7d4cb')), 1
  $smallFont = New-Object System.Drawing.Font 'Arial', 13, ([System.Drawing.FontStyle]::Regular), ([System.Drawing.GraphicsUnit]::Pixel)
  $labelFont = New-Object System.Drawing.Font 'Arial', 22, ([System.Drawing.FontStyle]::Bold), ([System.Drawing.GraphicsUnit]::Pixel)
  $largeFont = New-Object System.Drawing.Font 'Arial', 96, ([System.Drawing.FontStyle]::Regular), ([System.Drawing.GraphicsUnit]::Pixel)
  $italicFont = New-Object System.Drawing.Font 'Georgia', 96, ([System.Drawing.FontStyle]::Italic), ([System.Drawing.GraphicsUnit]::Pixel)
  try {
    $graphics.FillRectangle($paper, 0, 0, 1200, 630)
    $graphics.FillRectangle($ink, 65, 60, 48, 48)
    $graphics.DrawString('SB', $labelFont, $paper, 69, 69)
    $graphics.DrawString('Sangam Baral', $labelFont, $ink, 130, 69)
    $graphics.DrawString($label, $smallFont, $muted, 65, 160)
    $graphics.DrawString($firstLine, $largeFont, $ink, 57, 210)
    $graphics.DrawString($secondLine, $italicFont, $accent, 57, 318)
    $graphics.DrawLine($line, 65, 510, 1135, 510)
    $graphics.DrawString($footerText, $smallFont, $muted, 65, 545)
    $graphics.DrawString('sangambaral.com.np', $labelFont, $ink, 876, 538)
    $bitmap.Save((Join-Path $taskRoot ('assets/' + $filename)), [System.Drawing.Imaging.ImageFormat]::Png)
  } finally {
    $graphics.Dispose(); $bitmap.Dispose(); $paper.Dispose(); $ink.Dispose(); $accent.Dispose(); $muted.Dispose(); $line.Dispose()
    $smallFont.Dispose(); $labelFont.Dispose(); $largeFont.Dispose(); $italicFont.Dispose()
  }
}
New-PreviewCard 'social-card.png' '#f6f5f0' '#254bd8' 'ENGINEER. BUILDER. CURIOUS HUMAN.' 'Sangam' 'Baral.' 'ONE PERSON. TWO PERSPECTIVES.'
New-PreviewCard 'professional-social.png' '#f6f5f0' '#254bd8' 'THE PROFESSIONAL SIDE / SOFTWARE & PRODUCT ENGINEERING' 'Good ideas.' 'Built properly.' 'SOFTWARE / SYSTEMS / PRODUCT'
New-PreviewCard 'personal-social.png' '#f4eee5' '#a24b31' 'THE PERSONAL SIDE / CURIOUS, BY NATURE' 'Curious,' 'by nature.' 'TRAVEL / GAMES / AI / NATURE'
Write-Output 'Built three 1200 x 630 social previews.'
